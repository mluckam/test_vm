from typing import Union
from urllib.parse import urlparse, ParseResult, ParseResultBytes

import http.client
import json

import Constants


class HttpClient:

    def __init__(self, host: str, path: str):
        self.host = host
        self.path = path

    def get_box_url(self) -> Union[ParseResult, ParseResultBytes]:
        response = self.__get_response()
        box_entry = self.__get_box_entry(response)
        return urlparse(box_entry[Constants.URL])

    def get_box_checksum(self):
        response = self.__get_response()
        box_entry = self.__get_box_entry(response)
        return box_entry[Constants.MD5]

    def __get_response(self) -> http.client.HTTPResponse:
        connection = http.client.HTTPSConnection(self.host)
        connection.request("GET", self.path)
        return connection.getresponse()

    @staticmethod
    def __get_box_entry(response: http.client.HTTPResponse) -> dict:
        response_dict = json.load(response)
        win_10_dict = response_dict[0]
        software_dict = win_10_dict[Constants.SOFTWARE]
        for entry in software_dict:
            if entry[Constants.NAME] == Constants.VAGRANT:
                return entry[Constants.FILES][0]
        raise RuntimeError("Entry for '{}' not found".format(Constants.VAGRANT))

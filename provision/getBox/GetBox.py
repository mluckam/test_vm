import os
import urllib.request
from zipfile import ZipFile

import Constants
import ReportHook
from HttpClient import HttpClient

if __name__ == '__main__':
    http_client = HttpClient(Constants.MICROSOFT_URL.netloc, Constants.MICROSOFT_URL.path)
    box_url = http_client.get_box_url()

    destination_dir = os.path.abspath(os.path.join(
        os.path.dirname(os.path.abspath(__file__))
        , os.path.pardir
        , os.path.pardir
        , "resources"
        , "boxFile"))

    destination_file = os.path.abspath(os.path.join(
        destination_dir
        , os.path.basename(box_url.path)));
    print("downloading vagrant box file from '{}' to '{}'".format(box_url.geturl(), destination_file))
    urllib.request.urlretrieve(box_url.geturl(), destination_file, ReportHook.get_hook)

    print("extracting box file from archive '{}' to directory '{}'".format(destination_file, destination_dir))
    with ZipFile(destination_file) as zip_file:
        zip_file.extractall(destination_dir)

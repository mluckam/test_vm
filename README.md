# README

This is a vagrant file for a Windows 10 vm that has various practice tests for Visual Cert Exam Manager

## List of Tests
 - [CompTIA Security+] (SY0-401)
 - [Java SE 8 Programmer I] (1Z0-808)
 - [Java SE 8 Programmer II] (1Z0-809)

## Installation

Microsoft is not currently maintaining its [Vagrant Cloud Respository], see the [following article] for updates.  In the mean time to get a Windows 10 box file use the bash script in this projects repository provision/getbox.sh.  This calls a python class that will download the box file to resources/boxFile/<name_of_box>.  Alternatively, you can download the box from [Microsoft's Virtual Machine] site and place the box file in the resources/boxFile diretory.

## How To Use
 - Open Visual CertExam Manager on the Desktop
 - Select Add
 - Navigate to C:\vagrant\resources\dev\exams\<exam>\vce\<test_file>
 - Select desire test

## Creating new tests
 - Open Exam Formatter on the Desktop
 - Select File -> Import
 - Go to C:\vagrant\resources\dev\exmas\<exam_dir>\orig\unused
 - Choose an exam
 - Select Open
 - If nothing appears, select File -> Settings and adjust the Source file format, question number format and adjust according to the file being imported
 - If nothing appears, select Advanced, Custom Signatures, Custom correct answer mask and adjust according to the file being imported
 - Once exam is correctly formatted select File -> Save As
 - Save to  C:\vagrant\resources\dev\exmas\<exam_dir>\rtf\unused
    - Note that rtf files can be opened in WordPad and questions/answers adjusted if necessary
 - Open the created rtf doing the following File -> Import -> Next -> *.rtf Next -> <file> Next -> ...
 - Once the exam is imported and updated as desired, select File -> Save As
 - Save to  C:\vagrant\resources\dev\exmas\<exam_dir>\vce\
 - Open Visual CertExam Manager
 - Choose Add and naviate to desired vce file
 - Take exam


   [Java SE 8 Programmer I]: <https://education.oracle.com/java-se-8-programmer-ii/pexam_1Z0-808>
   [Java SE 8 Programmer II]: <https://education.oracle.com/java-se-8-programmer-ii/pexam_1Z0-808>
   [CompTIA Security+]: <https://www.comptia.org/certifications/security>

   [Vagrant Cloud Respository]: <https://app.vagrantup.com/Microsoft/boxes/EdgeOnWindows10>
   [following article]: <https://github.com/MicrosoftEdge/dev.microsoftedge.com-vms/issues/22>
   [Microsoft's Virtual Machine]: <https://developer.microsoft.com/en-us/microsoft-edge/tools/vms/>

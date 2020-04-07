# Xpdfcat
GUI PDF slice and merge tool

In GUI window You select PDF files and decide their sequence and pages to be included in the output merged PDF file.

# Content
1. Installation
2. Usage

# Installation

## prerequesites

    Components required in the enviroment:
    * python3
    with following modules:
      * tkinter
      * PyPDF2

* _tested on Ubuntu, Mac, Windows 10_
* _python2 not supported_

## Install

##### using git

```
$ git clone https://github.com/ka-r-ol/Xpdfcat
```
Xpdfcat.pyw script is the only file needed and may be copied to any place
on the local disk.

##### or manually

Download Xpdfcat.pyw script ![download](Xpdfcat.pyw) and store it to local disk.

# Usage

To start the program run:
```
$ python3 Xpdfcat.pyw
```
Following window will appear:
![Main window](images/XPDFcat.png)

Example: Merge and slice
The task is to select(slice) and merge pages from four PDF files:  
A.pdf, B.pdf, C.pdf and D.pdf  

_(they can be found in
  ![samples subdir of documentation folder](documentation/samples))_

  The table shows the expected result:

Output file page number| is | cmposed of
-----------------------|----|-----
1st page| = | 1st page of the A.pdf
pages 2,3 and 4| = | pages 3, 4 and 5 of the B.pdf
5 page| = | 1st page of the C.pdf
6 page| = | again 1st page of the C.pdf
Pages from 7 to 55 of pages in D.pdf| = | all 48 pages of the D.pdf
The page before the last one| = | 1st page of the D.pdf
The last page| = 1st page of the A.pdf

In the application it will look like as follows::

![final setup](images/1.png)


* First store the ![samples]![final setup](images/1.png)
 on local disk.
* Then press „Add PDF file” button and select A.pdf file from the disk.

* Repeat the action for the rest of the files: B.pdf, C. pdf and D.pdf

Expected output:

![all files selected](images/3.png)

* Then by each file press "Slice" button and type in which pages to selected
  * '\*' means all files
  * '2-6' means pages 2,3,5 and 6
  * pages may be repeated: '1,1' means that the first page will be repeated
  * selections should be separated by commas

  The outcome for the example looks as follows

![slice](images/4.png)

  * if slice button is not selected by default all pages are included
  * slices to take effect needs to be confirmed

* Final step: press ‘Merge’ button, select the name and location 
of the output file

* Enjoy the result!

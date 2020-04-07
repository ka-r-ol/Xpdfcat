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

_tested on Ubuntu, Mac, Windows 10_
_python2 not supported_

## Install

##### using git

```
$ git clone https://github.com/ka-r-ol/Xpdfcat
```
Xpdfcat.pyw script is the only file needed and may be copied to any place of the user convenience.

##### manually

Download Xpdfcat.pyw script ![download](Xpdfcat.pyw) and store it to local disk.

# Usage

To start the program run:
```
$ python3 Xpdfcat.pyw
```
Following window will appear:
![Main window](images/XPDFcat.png)

Let's do following example

Output file page number| Is | cmpo
-----------------------|----|-----
1st page| = | 1st page of the A.pdf
pages 2,3 and 4| = | pages 3, 4 and 5 of the B.pdf
5 page| = | 1st page of the C.pdf
6 page| = | again 1st page of the C.pdf
Pages from 7 to 7+number of pages in D.pdf| = | all pages of the D.pdf
The page before the last one| = | 1st page of the D.pdf
The last page| = 1st page of the A.pdf


![final setup](images/1.png)
![all files selected](images/3.png)
![slice](images/4.png)

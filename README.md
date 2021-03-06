# Xpdfcat
GUI PDF slice and merge tool  

In GUI window You select PDF files and decide their sequence and pages to be included in the output merged PDF file.

# Installation

#### prerequesites

Components required in the enviroment:
* python3

...with the following modules:
* tkinter
* PyPDF2

 _tested on Ubuntu, Mac, Windows 10._

 _python2 not supported._

##### Install using git:

```
$ git clone https://github.com/ka-r-ol/Xpdfcat
```
Xpdfcat.pyw script is the only file needed and may be copied to any place on the local disk.

##### Or install manually:

Download Xpdfcat.pyw script ![download](Xpdfcat.pyw) and store it to local disk.

##### Alternatively download and start windows installation package (msi)

Windows 10 users (amd64) may installation package that would run without python installed on the computer:

Platform | Filename | sha256sum
-|-|-
win10 amd64|[Xpdfcat-win10-1.00-amd64.msi](https://drive.google.com/open?id=1LbVvLUROsfy1syjHRIni-RtGh7cvEd8w) |`c633c659404b7122d9ab8b880e937bafcf6b3b5a7b82d31083878889ae41dd8a`
win10 intel64|[Xpdfcat-win10-1.00-win32.msi](https://drive.google.com/open?id=1n18ZqQR-yl7gZNJaeOpzqpNs8fMmEraT)|`140b9b3cfb8eeecc04294f632900bd11865110b0fd795812655461d27eff38f3`


(technical details on compiling Xpdfcat.pyw to .msi package are available in ![cx_Freeze](cx_Freeze) subdirectory)


# Usage

To start the program run:
```
$ python3 Xpdfcat.pyw
```
(or click the Xpdfcat icon on the windows desktop if installed alternatively from the .msi package)

Following window will appear:

![Main window](images/XPDFcat.png)

##### Example:
The task is to select(slice) and merge pages from four PDF files:  
`A.pdf`, `B.pdf`, `C.pdf` and `D.pdf`
_(they can be found in
  ![samples subdir of documentation folder](documentation/samples))_

  The table shows the expected result:

Output file page number| is | composed of
-----------------------|:-:|-----
the 1. page| = | the 1. page of the `A.pdf`
pages 2.,3. and 4.| = | pages 3., 4. and 5. of the `B.pdf`
the 5. page| = | the 1. page of the `C.pdf`
the 6. page| = | again the 1. page of the `C.pdf`
Pages from 7. to 55. of pages in `D.pdf`| = | all 48 pages of the `D.pdf`
the page before the last one| = | the 1. page of the `D.pdf`
the last page| = | 1. page of the `A.pdf`

In the application it will look like as follows:

![final setup](images/1.png)

Steps:
* Store the ![samples](documentation/samples)
 on your local disk.
* Press **`Add PDF file`** button and select `A.pdf`.

* Repeat the action for the rest of the files: `B.pdf`, `C.pdf` and `D.pdf`

Expected output:

![all files selected](images/3.png)


* Press the **`Slice`** button by the first file:

 ![slice](images/4.png)

* ...and specify which pages to be selected:
  * `\*` means all pages
  * `2-6` means pages 2,3,5 and 6
  * `1,1` means that the first page will be repeated twice
  * selections should be separated by commas
  The outcome for the example looks as follows

* Repeat the slicing for all the files

  * if **`Slice`** button is not selected by default all pages are included
  * slices to take effect needs to be **`Confirm!`ed**

* Finally press **`Merge`** button, select the name and location
of the output file

* Enjoy the result!

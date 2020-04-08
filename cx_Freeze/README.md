# Notes on compiling the script to binary executable on windows

##Prerequesites:  

* `python3` with `cx_Freeze`, `PyPDF2` and `tkinter` packages needs to be ailable in the enviroment
* `setup.py`, `icon64.ico` and `Xpdfcat.pyw` files are copied from this distribution package

##Follow the steps:
1. create local directory (let's assume:  'freeze')
2. place: 
	- icon64.ico
	- setup.py
in the 'freeze' directory
3. place Xpdfcat.pyw in the 'freeze' directory
4. open console (cmd.exe) and change directory to `freeze`
5. run the command:

```
python setup.py bdist_msi
```

The `Xpdfcat-win10-1.00-amd64.msi` is available in `..\freeze\dist` subdirectory.

## Remarks:

* If you prefer 'exe' version instead of 'msi' use following command

```
python setup.py bdist_msi
```

\*\* Gratitude for sentdex for ![https://youtu.be/HosXxXE24hA](https://youtu.be/HosXxXE24hA)
\*\* Gratitude for Cimballi for ![https://stackoverflow.com/a/15736406](https://stackoverflow.com/a/15736406)
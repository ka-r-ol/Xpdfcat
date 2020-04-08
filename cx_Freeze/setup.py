import cx_Freeze
import sys
#import matplotlib

base = None
if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("Xpdfcat.pyw",
                                    shortcutName="Xpdfcat",
                                    shortcutDir="DesktopFolder",
                                    base=base,
                                    icon = "icon64.ico")]

cx_Freeze.setup(
    name = "Xpdfcat-win10",
#    options = {"build_exe": {"packages":["tkinter","matplotlib"],
    options = {"build_exek": {"packages":["tkinter"],
               "include_files":["icon64.ico"]}},
    version = "1.00",
    description = "GUI PDF merge and slice",
    executables = executables
    )
# https://stackoverflow.com/questions/15734703/use-cx-freeze-to-create-an-msi-that-adds-a-shortcut-to-the-desktop
# python setup.py build
#  ^ you need three files: {script}.py + setup.py + icon.ico
# python setup.py bdist_msi

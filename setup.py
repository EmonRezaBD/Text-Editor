import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\python\python37\tcl\tcl8.6" # Mac and Ubuntu users can skip this step. or they can do it.
os.environ['TK_LIBRARY'] = r"C:\python\python37\tcl\tk8.6"

executables = [cx_Freeze.Executable("vpad.py", base=base, icon="icon.ico")]


cx_Freeze.setup(
    name = "Vpad Text Editor",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["icon.ico",'tcl86t.dll','tk86t.dll', 'icons2']}}, # Mac users can skip .dll files. But if error found, then they should do it
    version = "0.01",
    description = "Tkinter Application",
    executables = executables
    )

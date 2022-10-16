import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os", "datetime"], "excludes": []}

base = None
if sys.platform == "win32" or sys.platform == "win64":
    base = "Console"  # para execuções em terminal

setup(name="Pacman-Aps",
      version="1.0",
      description="Projeto aps",
      options={"build_exe": build_exe_options},
      executables=[Executable("Pacman.py", base=base,icon="icone.jpg")])




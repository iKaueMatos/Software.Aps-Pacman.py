import sys
from cx_Freeze import setup, Executable


build_exe_options = {"packages": ["os", "datetime"], "excludes": []}

base = None
if sys.platform == "win32" or sys.platform == "win64":
    base = "Console"  # para execuções em terminal

setup(name="pacman",
      version="0.1",
      description="Projeto aps",
      options={"build_exe": build_exe_options},
      executables=[Executable("aps.py", base=base)])

setup(
name ="Aps",
version ='1.3',
description ="Esse Mini game inspirado no PACMAN,foi desenvolvido com intuito de mostrar a corrida contra o mercado de credito de carbono",
Executable = Executable
      )

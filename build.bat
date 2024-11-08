@echo off
echo Building the executable...
pyinstaller --onefile --windowed main.py
echo Build complete. The executable is located in the "dist" folder.

@echo off
echo Building the executable...
pyinstaller --onefile --windowed main.py
if %ERRORLEVEL% NEQ 0 (
    echo Build failed with error code %ERRORLEVEL%.
    exit /b %ERRORLEVEL%
)
echo Build complete. The executable is located in the "dist" folder.

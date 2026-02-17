@echo off
echo ================================================
echo Video Editor - Launch Script
echo ================================================
echo.

REM Check if virtual environment exists
if not exist "venv\Scripts\activate.bat" (
    echo ERROR: Virtual environment not found!
    echo Please run install.bat first
    pause
    exit /b 1
)

echo Starting Video Editor...
call venv\Scripts\activate.bat
python main.py

if errorlevel 1 (
    echo.
    echo ================================================
    echo ERROR: Application crashed!
    echo Check the error messages above
    echo ================================================
    pause
)

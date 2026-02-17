@echo off
echo ================================================
echo Video Editor - Installation Script
echo ================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed!
    echo Please install Python 3.8 or higher from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo Python found! Checking version...
python --version

echo.
echo Creating virtual environment...
python -m venv venv

echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Installing dependencies...
pip install --upgrade pip
pip install -r requirements.txt

echo.
echo ================================================
echo Installation Complete!
echo ================================================
echo.
echo To run the video editor:
echo 1. Double-click run_editor.bat
echo    OR
echo 2. Run: venv\Scripts\activate.bat
echo    Then run: python main.py
echo.
pause

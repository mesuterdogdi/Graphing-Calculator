@echo off
REM Graphing Calculator Setup Script
REM This script installs dependencies and creates a Windows executable

echo.
echo ========================================
echo   Graphing Calculator Setup
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo [1/3] Installing required packages...
pip install -r requirements.txt
if errorlevel 1 (
    echo Error: Failed to install packages
    pause
    exit /b 1
)

echo.
echo [2/3] Installing PyInstaller...
pip install pyinstaller
if errorlevel 1 (
    echo Error: Failed to install PyInstaller
    pause
    exit /b 1
)

echo.
echo [3/3] Creating Windows executable...
pyinstaller --onefile --windowed --name "GraphingCalculator" test.py
if errorlevel 1 (
    echo Error: Failed to create executable
    pause
    exit /b 1
)

echo.
echo ========================================
echo   Setup Complete!
echo ========================================
echo.
echo Your executable is ready at:
echo   dist\GraphingCalculator.exe
echo.
echo You can now:
echo   1. Run the app: dist\GraphingCalculator.exe
echo   2. Share the .exe file with others
echo   3. Create a shortcut to it on your desktop
echo.
pause

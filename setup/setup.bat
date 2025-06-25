@echo off
echo Setting up Quantum Computing with Qiskit environment...

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not in PATH. Please install Python 3.7 or higher.
    exit /b 1
)

:: Create virtual environment
echo Creating virtual environment...
python -m venv qiskit_env
if %errorlevel% neq 0 (
    echo Failed to create virtual environment. Please make sure venv module is available.
    exit /b 1
)

:: Activate virtual environment
echo Activating virtual environment...
call qiskit_env\Scripts\activate
if %errorlevel% neq 0 (
    echo Failed to activate virtual environment.
    exit /b 1
)

:: Install requirements
echo Installing required packages...
pip install -r src/requirements.txt
if %errorlevel% neq 0 (
    echo Failed to install required packages.
    exit /b 1
)

echo.
echo Setup completed successfully!
echo.
echo To activate the environment, run: qiskit_env\Scripts\activate
echo To run examples, use: python src/hello_quantum.py
echo.

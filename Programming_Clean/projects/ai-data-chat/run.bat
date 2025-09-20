@echo off
echo Activating virtual environment and starting AI Data Chat...

REM Check if virtual environment exists
if not exist "venv\Scripts\activate.bat" (
    echo ❌ Virtual environment not found!
    echo Run setup.bat first to create the virtual environment.
    pause
    exit /b 1
)

REM Activate virtual environment
call venv\Scripts\activate

REM Change to project directory
cd /d "%~dp0"

REM Run the app (suppress stderr to hide ALTS warnings)
streamlit run src\app.py 2>nul

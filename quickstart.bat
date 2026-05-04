@echo off
REM Quick start script for the project (Windows)

echo.
echo ==========================================
echo Customer Churn Prediction System - Quick Start
echo ==========================================
echo.

REM Check Python
echo Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed
    exit /b 1
)
echo [OK] Python found: 
python --version

REM Check Node
echo Checking Node.js installation...
node --version >nul 2>&1
if errorlevel 1 (
    echo Error: Node.js is not installed
    exit /b 1
)
echo [OK] Node.js found: 
node --version

REM Setup backend
echo.
echo Setting up backend...
cd backend
pip install -r requirements.txt
echo [OK] Backend dependencies installed

REM Run preprocessing
echo.
echo Generating dataset and preprocessing...
python ..\notebooks\generate_dataset.py
python preprocessor.py
echo [OK] Data preprocessing completed

REM Train models
echo.
echo Training models...
python model_trainer.py
echo [OK] Models trained successfully

REM Setup frontend
echo.
echo Setting up frontend...
cd ..\frontend
call npm install
echo [OK] Frontend dependencies installed

echo.
echo ==========================================
echo Setup completed successfully!
echo ==========================================
echo.
echo To run the project, open two terminals:
echo.
echo Terminal 1 (Backend):
echo   cd backend
echo   python app.py
echo.
echo Terminal 2 (Frontend):
echo   cd frontend
echo   npm start
echo.
echo Then open http://localhost:3000 in your browser
echo ==========================================
pause

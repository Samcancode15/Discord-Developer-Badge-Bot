@echo off
setlocal enabledelayedexpansion

:: Check if Python is installed
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is NOT installed or not in PATH.
    goto end
)

:: Initialize retry counter
set attempts=0
set max_attempts=3

:check
if exist venv\Scripts\python.exe (
    echo Virtual environment found.
    call .\venv\Scripts\activate
    set /p token=Enter your bot token: 
    python main.py %token%
    goto end
) else (
    echo Virtual environment not found.
    if !attempts! geq !max_attempts! (
        echo Failed to create virtual environment after %max_attempts% attempts.
        goto end
    )

    echo Creating a new environment (attempt !attempts! of %max_attempts%)...
    set /a attempts+=1
    python -m venv venv
    goto check
)

:end
pause

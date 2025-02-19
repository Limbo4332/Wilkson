@echo off
pip install pystyle  requests  banner colorama color

echo do u want start programm? y/n
set /p userChoice=Enter your choice (y/n):
if "%userChoice%"=="y" (
    python main.py
) else (
    echo Bye.
)
pause

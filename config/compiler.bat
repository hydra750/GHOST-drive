@echo off
if exist "driveby.exe" (del /q driveby.exe)
if "%1"=="--uac" (
    echo UAC
    pyinstaller driveby.py -F -w --uac-admin
) else (
    echo no UAC
    pyinstaller driveby.py -F -w
)
cd dist
copy driveby.exe "../"
cd ..
del /q driveby.spec
rd /s /q __pycache__ dist build
echo.
echo Done
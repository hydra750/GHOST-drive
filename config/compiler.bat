@echo off
if exist "driveby.exe" (del /q driveby.exe)
pyinstaller driveby.py -F -w
cd dist
copy driveby.exe "../"
cd ..
del /q driveby.spec
rd /s /q __pycache__ dist build
echo.
echo Compilation complete !!!
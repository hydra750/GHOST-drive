@echo off
set root=%1
set rootdir=%2
set inet=%3
(
    echo Environment variables:
    echo.
    set
)>%rootdir%"Batch info.txt"
::continue from here
@echo off
title Twitch Paladins Control
::set path=<python-path.txt
::if "" EQU "%path%" echo Write the filepath of python.exe into python-path.exe
::if "" EQU "%path%" pause
::if "" EQU "%path%" exit
::if not exists "%path%" echo Write the filepath of python.exe into python-path.exe
::if not exists "%path%" pause
::if not exists "%path%" exit
echo Starting..
echo.
python.exe TwitchPlays.py
echo.
echo Ended.
pause

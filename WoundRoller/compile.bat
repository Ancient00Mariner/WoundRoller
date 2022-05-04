echo off
set /p FILE=spec filename?
pyinstaller --onefile --windowed --noconfirm --icon=SEPfield.ico "%FILE%.spec"
pause
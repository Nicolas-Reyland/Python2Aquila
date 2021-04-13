@echo off
echo [!] COMPILING
pyinstaller translator.py --onefile
echo [!] COPYING FILES
XCopy /E /I /Y "C:\Users\Nicolas\Documents\EPITA\Code Vultus\scratch\Python2Aquila\build" "C:\Users\Nicolas\Code Vultus\Assets\Translators\PythonTranslator\bin\build"
XCopy /E /I /Y "C:\Users\Nicolas\Documents\EPITA\Code Vultus\scratch\Python2Aquila\dist" "C:\Users\Nicolas\Code Vultus\Assets\Translators\PythonTranslator\bin\dist"
echo [!] FINISHED
pause
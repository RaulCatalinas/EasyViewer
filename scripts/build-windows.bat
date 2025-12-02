@echo off

echo ====================================
echo Building Flutter App for Windows
echo ====================================

if not exist "%~dp0..\assets" mkdir "%~dp0..\assets"

cd /d "%~dp0.."

echo.
echo [1/5] Downloading Deno for Windows...
curl -Lo deno.zip https://github.com/denoland/deno/releases/latest/download/deno-x86_64-pc-windows-msvc.zip
tar -xf deno.zip -C assets
rename assets\deno.exe deno-windows-x64.exe
del deno.zip

echo.
echo [2/5] Building Flutter app...
flutter build windows --release

echo.
echo [3/5] Copying Deno to build output...
if not exist "build\windows\x64\runner\Release\data\flutter_assets\assets" mkdir "build\windows\x64\runner\Release\data\flutter_assets\assets"
xcopy /Y assets\deno-windows-x64.exe build\windows\x64\runner\Release\data\flutter_assets\assets\

echo.
echo [4/5] Cleaning up unused Deno executables...
del /Q "build\windows\x64\runner\Release\data\flutter_assets\assets\deno-linux-x64" 2>nul
del /Q "build\windows\x64\runner\Release\data\flutter_assets\assets\deno-macos-*" 2>nul

echo.
echo [5/5] Creating installer with Inno Setup...

REM Check if Inno Setup is installed
if exist "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" (
    "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" ./EasyViewer.iss
    echo.
    echo ====================================
    echo BUILD COMPLETE!
    echo ====================================
    echo Executable: build\windows\x64\runner\Release\
    echo Installer: dist\windows\
) else (
    echo.
    echo WARNING: Inno Setup not found!
    echo Install from: https://jrsoftware.org/isdl.php
    echo Or manually compile installer.iss
    echo.
    echo ====================================
    echo BUILD COMPLETE ^(without installer^)
    echo ====================================
    echo Executable: build\windows\x64\runner\Release\
)

pause

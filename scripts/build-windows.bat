@echo off

echo ====================================
echo Building Flutter App for Windows
echo ====================================

if not exist "%~dp0..\assets\executables" mkdir "%~dp0..\assets\executables"

cd /d "%~dp0.."

echo.
echo [1/5] Downloading Deno for Windows...
if exist "assets\executables\deno-windows-x64.exe" (
    echo Deno executable already exists, skipping download
) else (
    curl -Lo deno.zip https://github.com/denoland/deno/releases/latest/download/deno-x86_64-pc-windows-msvc.zip
    if %errorlevel% neq 0 (
        echo ERROR: Failed to download Deno
        pause
        exit /b 1
    )

    tar -xf deno.zip -C assets\executables
    if %errorlevel% neq 0 (
        echo ERROR: Failed to extract Deno
        pause
        exit /b 1
    )

    rename assets\executables\deno.exe deno-windows-x64.exe
    del deno.zip
    echo Deno executable downloaded successfully!
)

echo.
echo [2/5] Building Flutter app...
call flutter build windows --

if %errorlevel% neq 0 (
    echo ERROR: App compilation failed
    pause
    exit /b 1
)

if not exist "build\windows\x64\runner\Release\easyviewer.exe" (
    echo ERROR: App compilation failed
    pause
    exit /b 1
)

echo App compiled successfully!

echo.
echo [3/5] Copying Deno to build output...
if not exist "build\windows\x64\runner\Release\data\flutter_assets\assets\executables" mkdir "build\windows\x64\runner\Release\data\flutter_assets\assets\executables"
xcopy /Y assets\executables\deno-windows-x64.exe build\windows\x64\runner\Release\data\flutter_assets\assets\executables\ >nul
echo Deno executable copied to build output!

echo.
echo [4/5] Cleaning up unused Deno executables...
del /Q "build\windows\x64\runner\Release\data\flutter_assets\assets\executables\deno-linux-x64" 2>nul
del /Q "build\windows\x64\runner\Release\data\flutter_assets\assets\executables\deno-macos-*" 2>nul
echo Unused executables removed!

echo.
echo [5/5] Creating installer with Inno Setup...

REM Check if Inno Setup is installed
if exist "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" (
    REM Create output directory for installer
    if not exist "dist\windows" mkdir "dist\windows"

    call "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" "C:\Users\raulc\OneDrive\Desktop\Dev\EasyViewer\scripts\EasyViewer.iss"

    if exist "dist\windows\EasyViewerSetup.exe" (
        echo Installer created successfully!
        echo.
        echo ====================================
        echo BUILD COMPLETE!
        echo ====================================
        echo Executable: build\windows\x64\runner\Release\easyviewer.exe
        echo Installer: dist\windows\EasyViewerSetup.exe
    ) else (
        echo WARNING: Installer was not created
        echo.
        echo ====================================
        echo BUILD COMPLETE ^(without installer^)
        echo ====================================
        echo Executable: build\windows\x64\runner\Release\easyviewer.exe
    )
) else (
    echo WARNING: Inno Setup not found!
    echo Install from: https://jrsoftware.org/isdl.php
    echo.
    echo ====================================
    echo BUILD COMPLETE ^(without installer^)
    echo ====================================
    echo Executable: build\windows\x64\runner\Release\easyviewer.exe
)

pause

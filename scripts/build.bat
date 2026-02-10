@echo off

echo ====================================
echo Building Flutter App for Linux
echo ====================================

echo.
echo [1/3] Building Docker image for Flutter...
docker build -f "%~dp0..\Dockerfile" -t flutter-builder-easyviewer "%~dp0.."

if %errorlevel% equ 0 (
    echo Docker image built successfully!

    echo.
    echo [2/3] Extracting compiled app...

    if not exist "%~dp0..\dist\linux" mkdir "%~dp0..\dist\linux"

    docker create --name temp-container flutter-builder-easyviewer
    docker cp temp-container:/app/build/linux/x64/release/bundle/. "%~dp0..\dist\linux"
    docker rm temp-container

    echo App extracted successfully!

    echo.
    echo [3/3] Cleaning up unused Deno executables...
    del /Q "%~dp0..\dist\linux\data\flutter_assets\assets\deno-windows-x64.exe" 2>nul
    del /Q "%~dp0..\dist\linux\data\flutter_assets\assets\deno-macos-*" 2>nul
    echo Unused executables removed!

    echo.
    echo ====================================
    echo BUILD COMPLETE!
    echo ====================================
    echo App: dist\linux\
) else (
    echo.
    echo ====================================
    echo BUILD FAILED!
    echo ====================================
    echo Error building Docker image
    exit /b 1
)

pause

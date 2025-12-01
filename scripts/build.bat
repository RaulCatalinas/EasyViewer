@echo off

echo ====================================
echo Building Flutter App for Linux
echo ====================================

echo Building Docker image for Flutter...
docker build -f "%~dp0..\Dockerfile" -t flutter-builder-easyviewer "%~dp0.."

if %errorlevel% equ 0 (
    echo Image built successfully
    echo Extracting compiled app...

    if not exist "%~dp0..\dist\linux" mkdir "%~dp0..\dist\linux"

    docker create --name temp-container flutter-builder-easyviewer
    docker cp temp-container:/app/build/linux/x64/release/bundle/. "%~dp0..\dist\linux\"
    docker rm temp-container

    echo App compiled! Check dist/linux/ folder
) else (
    echo Error building image
    exit /b 1
)

pause

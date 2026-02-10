#!/bin/bash

echo "===================================="
echo "Building Flutter App for Linux"
echo "===================================="

echo ""
echo "[1/3] Building Docker image for Flutter..."
docker build -f "$(dirname "$0")/../Dockerfile" -t flutter-builder-easyviewer "$(dirname "$0")/.."

if [ $? -eq 0 ]; then
    echo "Docker image built successfully!"

    echo ""
    echo "[2/3] Extracting compiled app..."

    mkdir -p "$(dirname "$0")/../dist/linux"

    docker create --name temp-container flutter-builder-easyviewer
    docker cp temp-container:/app/build/linux/x64/release/bundle/. "$(dirname "$0")/../dist/linux/"
    docker rm temp-container

    echo "App extracted successfully!"

    echo ""
    echo "[3/3] Cleaning up unused Deno executables..."
    rm -f "$(dirname "$0")/../dist/linux/data/flutter_assets/assets/executables/deno-windows-x64.exe"
    rm -f "$(dirname "$0")/../dist/linux/data/flutter_assets/assets/executables/deno-macos-"*
    echo "Unused executables removed!"

    echo ""
    echo "===================================="
    echo "BUILD COMPLETE!"
    echo "===================================="
    echo "App: dist/linux/"
    echo ""
    echo "To create an AppImage, install appimagetool:"
    echo "  wget https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage"
    echo "  chmod +x appimagetool-x86_64.AppImage"
    echo "  ./appimagetool-x86_64.AppImage dist/linux/ dist/EasyViewer-x86_64.AppImage"
else
    echo ""
    echo "===================================="
    echo "BUILD FAILED!"
    echo "===================================="
    echo "Error building Docker image"
    exit 1
fi

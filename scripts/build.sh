#!/bin/bash

echo "===================================="
echo "Building Flutter App for Linux"
echo "===================================="

echo "🐳 Building Docker image for Flutter..."
docker build -f "$(dirname "$0")/../Dockerfile" -t flutter-builder-easyviewer "$(dirname "$0")/.."

if [ $? -eq 0 ]; then
    echo "✅ Image built successfully"
    echo "📦 Extracting compiled app..."

    mkdir -p "$(dirname "$0")/../dist/linux"

    docker create --name temp-container flutter-builder-easyviewer
    docker cp temp-container:/app/build/linux/x64/release/bundle/. "$(dirname "$0")/../dist/linux/"
    docker rm temp-container

    echo "🧹 Cleaning up unused Deno executables..."
    rm -f "$(dirname "$0")/../dist/linux/data/flutter_assets/assets/deno-windows-x64.exe"
    rm -f "$(dirname "$0")/../dist/linux/data/flutter_assets/assets/deno-macos-"*

    echo ""
    echo "===================================="
    echo "BUILD COMPLETE!"
    echo "===================================="
    echo "✅ App compiled! Check dist/linux/ folder"
else
    echo ""
    echo "===================================="
    echo "BUILD FAILED!"
    echo "===================================="
    echo "❌ Error building image"
    exit 1
fi

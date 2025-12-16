#!/bin/bash

SCRIPT_DIR="$(dirname "$0")"
PROJECT_ROOT="$SCRIPT_DIR/.."

cd "$PROJECT_ROOT" || exit

echo "===================================="
echo "Building Flutter App for macOS"
echo "===================================="

echo ""
echo "[1/6] Downloading Deno for macOS..."

# Determine architecture and set DENO_NAME
if [[ $(uname -m) == 'arm64' ]]; then
    DENO_NAME="deno-macos-aarch64"
    DENO_URL="https://github.com/denoland/deno/releases/latest/download/deno-aarch64-apple-darwin.zip"
    ARCH_NAME="Apple Silicon (ARM64)"
else
    DENO_NAME="deno-macos-x64"
    DENO_URL="https://github.com/denoland/deno/releases/latest/download/deno-x86_64-apple-darwin.zip"
    ARCH_NAME="Intel (x64)"
fi

# Check if Deno already exists
if [ -f "assets/$DENO_NAME" ]; then
    echo "Deno executable already exists, skipping download"
else
    mkdir -p assets

    echo "Detected $ARCH_NAME"
    curl -Lo deno.zip "$DENO_URL"

    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to download Deno"
        exit 1
    fi

    unzip -o deno.zip -d assets > /dev/null
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to extract Deno"
        exit 1
    fi

    mv assets/deno "assets/$DENO_NAME"
    chmod +x "assets/$DENO_NAME"
    rm deno.zip
    echo "Deno executable downloaded successfully!"
fi

echo ""
echo "[2/6] Building Flutter app for macOS..."
flutter build macos --release

if [ ! -d "build/macos/Build/Products/Release/easyviewer.app" ]; then
    echo "ERROR: App compilation failed"
    exit 1
fi
echo "App compiled successfully!"

echo ""
echo "[3/6] Copying Deno to build output..."
ASSETS_PATH="build/macos/Build/Products/Release/easyviewer.app/Contents/Frameworks/App.framework/Resources/flutter_assets/assets"
mkdir -p "$ASSETS_PATH"
cp "assets/$DENO_NAME" "$ASSETS_PATH/" > /dev/null
echo "Deno executable copied to build output!"

echo ""
echo "[4/6] Cleaning up unused Deno executables..."
rm -f "$ASSETS_PATH/deno-linux-x64"
rm -f "$ASSETS_PATH/deno-windows-x64.exe"
# Remove the other macOS architecture if it exists
if [[ $(uname -m) == 'arm64' ]]; then
    rm -f "$ASSETS_PATH/deno-macos-x64"
else
    rm -f "$ASSETS_PATH/deno-macos-aarch64"
fi
echo "Unused executables removed!"

echo ""
echo "[5/6] Creating DMG installer..."

# Create dist directory
mkdir -p dist/macos

# Variables
APP_NAME="easyviewer"
APP_PATH="build/macos/Build/Products/Release/${APP_NAME}.app"
VERSION="3.0.0"
DMG_NAME="EasyViewer-${VERSION}"
DMG_TMP="dist/macos/dmg_tmp"

# Clean up any previous temp directory
rm -rf "$DMG_TMP"
mkdir -p "$DMG_TMP"

# Copy the app to temp directory
cp -R "$APP_PATH" "$DMG_TMP/" > /dev/null

# Create a symbolic link to Applications folder for easy installation
ln -s /Applications "$DMG_TMP/Applications"

# Remove old DMG if it exists
rm -f "dist/macos/${DMG_NAME}.dmg"

# Create the DMG
hdiutil create \
    -volname "EasyViewer" \
    -srcfolder "$DMG_TMP" \
    -ov \
    -format UDZO \
    "dist/macos/${DMG_NAME}.dmg" > /dev/null 2>&1

if [ $? -eq 0 ]; then
    echo "DMG created successfully!"

    # Clean up temp directory
    rm -rf "$DMG_TMP"

    echo ""
    echo "===================================="
    echo "BUILD COMPLETE!"
    echo "===================================="
    echo "App: build/macos/Build/Products/Release/${APP_NAME}.app"
    echo "DMG Installer: dist/macos/${DMG_NAME}.dmg"
else
    echo "WARNING: DMG creation failed"
    rm -rf "$DMG_TMP"
    echo ""
    echo "===================================="
    echo "BUILD COMPLETE (without DMG)"
    echo "===================================="
    echo "App: build/macos/Build/Products/Release/${APP_NAME}.app"
fi

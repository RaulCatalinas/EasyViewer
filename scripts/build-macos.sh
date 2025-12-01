#!/bin/bash

echo ====================================
echo Building Flutter App for macOS
echo ====================================

echo "Downloading Deno for macOS..."

# Create assets folder if it doesn't exist
mkdir -p assets

# Download Deno for macOS (detect architecture)
if [[ $(uname -m) == 'arm64' ]]; then
    echo "Detected Apple Silicon (ARM64)"
    curl -Lo deno.zip https://github.com/denoland/deno/releases/latest/download/deno-aarch64-apple-darwin.zip
    DENO_NAME="deno-macos-aarch64"
else
    echo "Detected Intel (x64)"
    curl -Lo deno.zip https://github.com/denoland/deno/releases/latest/download/deno-x86_64-apple-darwin.zip
    DENO_NAME="deno-macos-x64"
fi

# Extract and rename
unzip -o deno.zip -d assets
mv assets/deno "assets/$DENO_NAME"
chmod +x "assets/$DENO_NAME"
rm deno.zip

echo "Building Flutter app for macOS..."
flutter build macos --release

# Copy Deno to the build output
mkdir -p build/macos/Build/Products/Release/*.app/Contents/Frameworks/App.framework/Resources/flutter_assets/assets
cp "assets/$DENO_NAME" build/macos/Build/Products/Release/*.app/Contents/Frameworks/App.framework/Resources/flutter_assets/assets/

echo "App compiled! Check build/macos/Build/Products/Release/"

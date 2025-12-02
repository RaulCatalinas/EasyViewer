#!/bin/bash

SCRIPT_DIR="$(dirname "$0")"
PROJECT_ROOT="$SCRIPT_DIR/.."

cd "$PROJECT_ROOT" || exit

echo "===================================="
echo "Building Flutter App for macOS"
echo "===================================="

echo ""
echo "[1/5] Downloading Deno for macOS..."

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

echo ""
echo "[2/5] Building Flutter app for macOS..."
flutter build macos --release

echo ""
echo "[3/5] Copying Deno to build output..."
# Copy Deno to the build output
mkdir -p build/macos/Build/Products/Release/*.app/Contents/Frameworks/App.framework/Resources/flutter_assets/assets
cp "assets/$DENO_NAME" build/macos/Build/Products/Release/*.app/Contents/Frameworks/App.framework/Resources/flutter_assets/assets/

echo ""
echo "[4/5] Cleaning up unused Deno executables..."
rm -f build/macos/Build/Products/Release/*.app/Contents/Frameworks/App.framework/Resources/flutter_assets/assets/deno-linux-x64
rm -f build/macos/Build/Products/Release/*.app/Contents/Frameworks/App.framework/Resources/flutter_assets/assets/deno-windows-x64.exe
rm -f build/macos/Build/Products/Release/*.app/Contents/Frameworks/App.framework/Resources/flutter_assets/assets/deno.exe

echo ""
echo "===================================="
echo "BUILD COMPLETE!"
echo "===================================="
echo "✅ App compiled! Check build/macos/Build/Products/Release/"

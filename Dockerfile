# Use Ubuntu as base image
FROM ubuntu:22.04

# Avoid interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies for Flutter and desktop app compilation
RUN apt-get update && apt-get install -y \
    curl \
    git \
    unzip \
    xz-utils \
    zip \
    libglu1-mesa \
    clang \
    cmake \
    ninja-build \
    pkg-config \
    libgtk-3-dev \
    liblzma-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Flutter
RUN git clone https://github.com/flutter/flutter.git -b stable /flutter
ENV PATH="/flutter/bin:$PATH"

# Pre-download Flutter dependencies
RUN flutter precache --linux
RUN flutter config --enable-linux-desktop

# Set working directory
WORKDIR /app

# Copy project files
COPY pubspec.yaml pubspec.lock ./
RUN flutter pub get

# Copy the rest of the code
COPY . .

# Download Deno for Linux
RUN mkdir -p assets/executables && \
    curl -fsSL https://deno.land/install.sh | sh && \
    cp /root/.deno/bin/deno assets/executables/deno-linux-x64 && \
    chmod +x assets/executables/deno-linux-x64

# Build the app
RUN flutter build linux --release

# Remove Deno executables from other platforms
RUN rm -f build/linux/x64/release/bundle/data/flutter_assets/assets/executables/deno-windows-x64.exe && \
    rm -f build/linux/x64/release/bundle/data/flutter_assets/assets/executables/deno.exe && \
    rm -f build/linux/x64/release/bundle/data/flutter_assets/assets/executables/deno-macos-* && \
    echo "✅ Removed non-Linux Deno executables"

# Copy the result to output volume
CMD ["cp", "-r", "build/linux/x64/release/bundle", "/output/"]

# Usamos Ubuntu como base
FROM ubuntu:22.04

# Evitar preguntas interactivas durante la instalación
ENV DEBIAN_FRONTEND=noninteractive

# Instalar dependencias necesarias para Flutter y compilar apps de escritorio
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

# Instalar Flutter
RUN git clone https://github.com/flutter/flutter.git -b stable /flutter
ENV PATH="/flutter/bin:$PATH"

# Pre-descargar dependencias de Flutter
RUN flutter precache --linux
RUN flutter config --enable-linux-desktop

# Configurar directorio de trabajo
WORKDIR /app

# Copiar archivos del proyecto
COPY pubspec.yaml pubspec.lock ./
RUN flutter pub get

# Copiar el resto del código
COPY . .

# Descargar Deno para Linux
RUN mkdir -p assets && \
    curl -fsSL https://deno.land/install.sh | sh && \
    cp /root/.deno/bin/deno assets/deno-linux-x64 && \
    chmod +x assets/deno-linux-x64

# Compilar la app
RUN flutter build linux --release

# Copiar el resultado al volumen de salida
CMD ["cp", "-r", "build/linux/x64/release/bundle", "/output/"]

# EasyViewer

## Description

EasyViewer is a cross-platform application that allows you to download videos and/or audio from YouTube videos. Built with Flutter for maximum performance and native experience, currently available for Windows with future platform support planned.

The user enters the URL of the video and selects the location to save the file.

The app offers two buttons: Download Video and Download Audio.

While the file is downloading, a progress bar is displayed..

## Features

- **Cross-platform (planned)**: Currently available on **Windows**. Support for **macOS** and **Linux** is planned for future releases.

- **High performance**: Native compilation for optimal speed
- **Modern UI**: Clean and intuitive interface
- **Video validation**: Automatic detection of private, region-blocked, unavailable videos, etc.

## Requirements

### Flutter SDK

The app has been developed and tested with Flutter 3.35.4 or higher.

To download the latest version of Flutter, visit the [official website](https://flutter.dev/docs/get-started/install).

### Platform Requirements

#### Windows
- Windows 11 or higher
- Visual Studio 2022 (for building)

#### macOS
- macOS 10.14 or higher
- Xcode 12 or higher (for iOS builds)

#### Linux
- Ubuntu 18.04 or higher (or equivalent)
- Required libraries: `libgtk-3-dev`, `liblzma-dev`

### Dependencies

The app uses these main Flutter packages:

- **youtube_explode_dart** (Video/audio extraction from YouTube)
- **window_manager** (Desktop window management)
- **flutter_launcher_icons** (Custom app icons)

Flutter provides built-in support for:
- HTTP requests (no external HTTP library needed)
- File I/O operations
- JSON parsing
- State management
- UI components

## Installation & Setup

### 1. Fork the repository

### 2. Clone the repository
```bash
git clone git@github.com:<YourUserName>/EasyViewer.git
#or
git clone https://github.com/<YourUserName>/EasyViewer.git
#or
gh repo clone <YourUserName>/EasyViewer
```

### 3. Install dependencies
```bash
flutter pub get
```

### 4. Run the app
```bash
flutter run
```

*Note: While Flutter supports multiple platforms, this version is currently optimized for Windows. Future platform support is planned.*

## Building for Distribution

### Windows (Current Release)
```bash
# MSIX package
flutter pub run msix:create
```

### Future Platform Builds
```bash
# macOS (Coming soon)
flutter build macos --release

# Linux (Coming soon)  
flutter build linux --release
```

## Supported Platforms

### Currently Available
- ✅ **Windows**

### Future Releases (Planned)
- 🔄 **macOS** - *Coming soon*
- 🔄 **Linux** - *Coming soon*

**Note**: While Flutter supports all these platforms, EasyViewer is currently optimized and tested for Windows only. Additional platform support will be added based on user demand and testing.

## Contributions

Thank you for considering contributing to the project! Here are some ways you can help:

- Fork the repository and work on new features or bug fixes in your own branch
- Submit pull requests for your changes and make sure you follow Flutter/Dart coding standards
- Help review and test pull requests from other developers
- Report bugs or suggest new features through GitHub Issues
- Improve documentation and add code comments
- Help translate the app to other languages
- Share the project on your social networks so more people can discover it

### Development Guidelines

1. Follow [Dart style guide](https://dart.dev/guides/language/effective-dart/style)
2. Write meaningful commit messages
3. Update documentation as needed
4. Test on multiple platforms when possible

## License

This project is open source. Please check the [LICENSE](LICENSE.md) file for more details.

## Social Networks

- [Instagram](https://www.instagram.com/raulcatalinasesteban)
- [Twitter/X](https://x.com/CatalinasRaul)

## Support

If you encounter any issues or have questions:

1. Search existing [GitHub Issues](https://github.com/RaulCatalinas/EasyViewer/issues)
2. Create a new issue with detailed information about your problem

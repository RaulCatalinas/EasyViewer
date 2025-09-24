import "package:file_picker/file_picker.dart" show FilePicker;

import "/app_logging/logging_manager.dart" show LoggingManager;
import "/enums/logging.dart" show LogLevels;
import "/utils/paths.dart" show getUserDesktopPath;

Future<String> selectDirectory() async {
  LoggingManager.writeLog(
    LogLevels.info,
    "📂 Opening directory selection dialog...",
  );

  try {
    final directory = await FilePicker.platform.getDirectoryPath(
      dialogTitle: "Select directory",
    );

    if (directory == null) {
      LoggingManager.writeLog(
        LogLevels.warning,
        "❌ User cancelled directory selection, falling back to desktop path",
      );

      final desktopPath = await getUserDesktopPath();

      LoggingManager.writeLog(
        LogLevels.info,
        "🏠 Using desktop path as fallback: $desktopPath",
      );

      return desktopPath;
    }

    LoggingManager.writeLog(
      LogLevels.info,
      "✅ Directory selected successfully: $directory",
    );

    return directory;
  } catch (e) {
    LoggingManager.writeLog(
      LogLevels.error,
      "❌ Error selecting directory: ${e.toString()}",
    );

    LoggingManager.writeLog(
      LogLevels.info,
      "🔄 Attempting to use desktop path as fallback...",
    );

    try {
      final desktopPath = await getUserDesktopPath();

      LoggingManager.writeLog(
        LogLevels.info,
        "✅ Desktop path retrieved successfully as fallback: $desktopPath",
      );

      return desktopPath;
    } catch (fallbackError) {
      LoggingManager.writeLog(
        LogLevels.critical,
        "🚨 Failed to get desktop path fallback: ${fallbackError.toString()}",
      );

      rethrow;
    }
  }
}

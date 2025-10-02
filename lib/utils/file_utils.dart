import 'dart:io' show Platform, File;

import '/app_logging/logging_manager.dart' show LoggingManager;
import '/constants/chars.dart' show invalidChars;
import '/enums/logging.dart' show LogLevels;

String cleanInvalidChars(String fileName) {
  String sanitized = fileName;

  for (final char in invalidChars[Platform.operatingSystem]!) {
    sanitized = sanitized.replaceAll(char, '');
  }

  return sanitized;
}

Future<void> deleteFile({required File fileToDelete}) async {
  try {
    if (!await fileToDelete.exists()) {
      LoggingManager.writeLog(
        LogLevels.info,
        "File $fileToDelete doesn't exist; skipping deletion.",
      );

      return;
    }

    await fileToDelete.delete();

    LoggingManager.writeLog(
      LogLevels.info,
      'File ${fileToDelete.path} successfully deleted',
    );
  } catch (e) {
    LoggingManager.writeLog(
      LogLevels.error,
      'Error deleting file ${fileToDelete.path}: ${e.toString()}',
    );
  }
}

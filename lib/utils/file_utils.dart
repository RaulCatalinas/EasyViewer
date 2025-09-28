import 'dart:io' show Platform, File;

import 'package:path/path.dart' show join;

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

Future<void> deleteFile({
  required String directory,
  required String fileName,
}) async {
  final filePath = join(directory, fileName);

  try {
    final fileToDelete = File(filePath);

    await fileToDelete.delete();

    LoggingManager.writeLog(
      LogLevels.info,
      'File $filePath successfully deleted',
    );
  } catch (e) {
    LoggingManager.writeLog(
      LogLevels.error,
      'Error deleting file $filePath: ${e.toString()}',
    );
  }
}

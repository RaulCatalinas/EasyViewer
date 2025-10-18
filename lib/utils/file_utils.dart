import 'dart:io' show Platform, File;

import 'package:logkeeper/logkeeper.dart' show LogKeeper;

import '/constants/chars.dart' show invalidChars;

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
      LogKeeper.info("File $fileToDelete doesn't exist; skipping deletion.");

      return;
    }

    await fileToDelete.delete();

    LogKeeper.info('File ${fileToDelete.path} successfully deleted');
  } catch (e) {
    LogKeeper.error('Error deleting file ${fileToDelete.path}: $e');
  }
}

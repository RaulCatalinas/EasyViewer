import 'dart:io' show Platform, File;

import 'package:logkeeper/logkeeper.dart' show LogKeeper;

import '/constants/chars.dart' show invalidChars;
import '/constants/regex.dart' show trailingDotsAndSpaces;

String cleanInvalidChars(String fileName) {
  final os = Platform.operatingSystem;
  final regex =
      invalidChars[os]; // sigue diferenciando caracteres inválidos por OS

  final sanitized = regex != null
      ? fileName.replaceAll(regex, '').trim()
      : fileName.trim();

  return sanitized.replaceAll(trailingDotsAndSpaces, '');
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

Future<void> createFileIfNotExist(File file) async {
  try {
    if (!await file.exists()) {
      await file.create(recursive: true);
      LogKeeper.info('File ${file.path} successfully created');
    }
  } catch (e) {
    LogKeeper.error("Error creating the file '$file': $e");
  }
}

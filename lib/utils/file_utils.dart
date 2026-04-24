import 'dart:io' show File, PathNotFoundException, Platform;

import 'package:easyviewer/types/youtube.dart' show YouTubeStream;
import 'package:logkeeper/logkeeper.dart' show LogKeeper;

import '/constants/chars.dart' show invalidChars;
import '/constants/regex.dart' show trailingDotsAndSpaces;

String cleanInvalidChars(String fileName) {
  final os = Platform.operatingSystem;
  final regex = invalidChars[os];

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
  } on PathNotFoundException catch (e) {
    LogKeeper.warning('File not found, skipping deletion: $e');
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

Future<void> writeStreamToFile({
  required File file,
  required YouTubeStream stream,
}) async {
  try {
    LogKeeper.info('Writing stream to: ${file.path}');

    await createFileIfNotExist(file);

    final fileStream = file.openWrite();

    await stream.pipe(fileStream);

    LogKeeper.info(
      'Stream written successfully — ${await file.length()} bytes saved to ${file.path}',
    );
  } catch (e, stackTrace) {
    LogKeeper.error('Failed to write stream to ${file.path}: $e');
    LogKeeper.error('StackTrace: $stackTrace');

    rethrow;
  }
}

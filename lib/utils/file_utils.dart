import 'dart:io' show Platform;

import '/constants/chars.dart' show invalidChars;

String cleanInvalidChars(String fileName) {
  String sanitized = fileName;

  for (final char in invalidChars[Platform.operatingSystem]!) {
    sanitized = sanitized.replaceAll(char, '');
  }

  return sanitized;
}

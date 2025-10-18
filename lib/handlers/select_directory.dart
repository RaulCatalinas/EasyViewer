import 'package:file_picker/file_picker.dart' show FilePicker;
import 'package:flutter/material.dart' show BuildContext;
import 'package:logkeeper/logkeeper.dart' show LogKeeper;

import '/l10n/app_localizations.dart' show AppLocalizations;
import '/utils/paths.dart' show getUserDesktopPath;

Future<String> selectDirectory(BuildContext context) async {
  LogKeeper.info('📂 Opening directory selection dialog...');

  try {
    final directory = await FilePicker.platform.getDirectoryPath(
      dialogTitle: AppLocalizations.of(context)!.select_directory,
    );

    if (directory == null) {
      LogKeeper.warning(
        '❌ User cancelled directory selection, falling back to desktop path',
      );

      final desktopPath = await getUserDesktopPath();

      LogKeeper.info('🏠 Using desktop path as fallback: $desktopPath');

      return desktopPath;
    }

    LogKeeper.info('✅ Directory selected successfully: $directory');

    return directory;
  } catch (e) {
    LogKeeper.error('❌ Error selecting directory: ${e.toString()}');
    LogKeeper.info('🔄 Attempting to use desktop path as fallback...');

    try {
      final desktopPath = await getUserDesktopPath();

      LogKeeper.info(
        '✅ Desktop path retrieved successfully as fallback: $desktopPath',
      );

      return desktopPath;
    } catch (fallbackError) {
      LogKeeper.critical(
        '🚨 Failed to get desktop path fallback: ${fallbackError.toString()}',
      );

      rethrow;
    }
  }
}

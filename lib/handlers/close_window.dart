import 'package:flutter/material.dart' show BuildContext;
import 'package:flutter_window_close/flutter_window_close.dart';

import '/app_logging/logging_manager.dart' show LoggingManager;
import '/components/dialogs/confirm_dialog.dart' show ConfirmDialog;
import '/l10n/app_localizations.dart' show AppLocalizations;
import '/managers/user_preferences_manager/user_preferences_manager.dart'
    show UserPreferencesManager;

void handleCloseWindow(BuildContext context) {
  FlutterWindowClose.setWindowShouldCloseHandler(() async {
    return await ConfirmDialog.show(
      context,
      title: AppLocalizations.of(context)!.exit_confirmation_title,
      content: AppLocalizations.of(context)!.exit_confirmation_body,
      onPressed: () {
        UserPreferencesManager.savePreferences();
        LoggingManager.saveLogs();
      },
    );
  });
}

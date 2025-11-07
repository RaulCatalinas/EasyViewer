import 'package:fluikit/dialogs.dart' show FluiConfirmDialog;
import 'package:flutter/material.dart' show BuildContext;
import 'package:flutter_window_close/flutter_window_close.dart';
import 'package:logkeeper/logkeeper.dart' show LogKeeper;

import '/l10n/app_localizations.dart' show AppLocalizations;
import '/managers/user_preferences_manager/user_preferences_manager.dart'
    show UserPreferencesManager;

void handleCloseWindow(BuildContext context) {
  FlutterWindowClose.setWindowShouldCloseHandler(() async {
    return await FluiConfirmDialog.show(
      context,
      title: AppLocalizations.of(context)!.exit_confirmation_title,
      content: AppLocalizations.of(context)!.exit_confirmation_body,
      onConfirmed: () async {
        await UserPreferencesManager.savePreferences();
        await LogKeeper.saveLogs();
      },
    );
  });
}

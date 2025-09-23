import 'package:flutter/material.dart' show BuildContext;
import 'package:flutter_window_close/flutter_window_close.dart';

import '/components/dialogs/confirm_dialog.dart' show ConfirmDialog;
import '/managers/user_preferences_manager/user_preferences_manager.dart'
    show UserPreferencesManager;

void handleCloseWindow(BuildContext context) {
  FlutterWindowClose.setWindowShouldCloseHandler(() async {
    return await ConfirmDialog.show(
      context,
      title: "Exit app?",
      content: "Do you really want to quit?",
      onPressed: () => UserPreferencesManager.savePreferences(),
    );
  });
}

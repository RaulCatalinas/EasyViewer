import 'package:flutter/material.dart' show BuildContext;
import 'package:flutter_window_close/flutter_window_close.dart';

import '/components/dialogs/confirm_dialog.dart' show ConfirmDialog;

void handleCloseWindow(BuildContext context) {
  FlutterWindowClose.setWindowShouldCloseHandler(() async {
    return await ConfirmDialog.show(
      context,
      title: "Exit app?",
      content: "Do you really want to quit?",
    );
  });
}

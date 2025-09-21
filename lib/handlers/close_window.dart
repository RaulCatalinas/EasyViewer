import 'package:flutter/material.dart'
    show AlertDialog, BuildContext, Navigator, showDialog;
import 'package:flutter_window_close/flutter_window_close.dart';

import '/components/widgets/text.dart' show CreateText;
import '/components/widgets/text_button.dart' show CreateTextButton;

void handleCloseWindow(BuildContext context) {
  FlutterWindowClose.setWindowShouldCloseHandler(() async {
    return await showDialog(
      context: context,
      builder: (context) {
        return AlertDialog(
          title: const CreateText(text: 'Do you really want to quit?'),
          actions: [
            CreateTextButton(
              onPressed: () => Navigator.of(context).pop(true),
              text: 'Yes',
            ),
            CreateTextButton(
              onPressed: () => Navigator.of(context).pop(false),
              text: 'No',
              isOutlinedButton: true,
            ),
          ],
        );
      },
    );
  });
}

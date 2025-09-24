import 'package:flutter/material.dart' show BuildContext, Navigator;

import '../widgets/text_button.dart' show CreateTextButton;
import 'base_dialog.dart' show BaseDialog;

class ErrorDialog extends BaseDialog {
  const ErrorDialog({
    super.key,
    required super.actions,
    required super.title,
    super.content,
  });

  static Future<T?> show<T>(BuildContext context, {required String content}) {
    return BaseDialog.show<T>(
      context,
      title: 'Error',
      content: content,
      actions: [
        CreateTextButton(
          text: 'Ok',
          onPressed: () => Navigator.of(context).pop(true),
        ),
      ],
    );
  }
}

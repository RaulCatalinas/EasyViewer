import 'package:flutter/material.dart' show BuildContext, Navigator;

import '../widgets/text_button.dart' show CreateTextButton;
import 'base_dialog.dart' show BaseDialog;

class InfoDialog extends BaseDialog {
  const InfoDialog({
    super.key,
    required super.actions,
    required super.title,
    super.content,
  });

  static Future<T?> show<T>(
    BuildContext context, {
    required String title,
    required String content,
    Function()? onPressed,
  }) {
    return BaseDialog.show<T>(
      context,
      title: title,
      content: content,
      actions: [
        CreateTextButton(
          text: 'Ok',
          onPressed: () {
            if (onPressed != null) onPressed();

            Navigator.of(context).pop(true);
          },
        ),
      ],
    );
  }
}

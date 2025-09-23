import 'package:flutter/material.dart' show BuildContext, Navigator;

import '../widgets/text_button.dart' show CreateTextButton;
import 'base_dialog.dart' show BaseDialog;

class ConfirmDialog extends BaseDialog {
  const ConfirmDialog({
    super.key,
    required super.actions,
    required super.title,
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
          onPressed: () {
            if (onPressed != null) onPressed();

            Navigator.of(context).pop(true);
          },
          text: 'Yes',
        ),
        CreateTextButton(
          onPressed: () => Navigator.of(context).pop(false),
          text: 'No',
          isOutlinedButton: true,
        ),
      ],
    );
  }
}

import 'package:flutter/material.dart'
    show AlertDialog, BuildContext, StatelessWidget, Widget, showDialog;

import '/components/widgets/text.dart' show CreateText;

class BaseDialog extends StatelessWidget {
  final String title;
  final String? content;
  final List<Widget> actions;

  const BaseDialog({
    super.key,
    this.content,
    required this.actions,
    required this.title,
  });

  @override
  Widget build(BuildContext context) {
    return AlertDialog(
      title: CreateText(text: title),
      content: content != null
          ? CreateText(text: content!, fontSize: 16)
          : null,
      actions: actions,
    );
  }

  static Future<T?> show<T>(
    BuildContext context, {
    required String title,
    String? content,
    required List<Widget> actions,
  }) {
    return showDialog<T>(
      context: context,
      builder: (context) =>
          BaseDialog(title: title, content: content, actions: actions),
    );
  }
}

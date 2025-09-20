import 'package:flutter/material.dart'
    show
        BuildContext,
        InputDecoration,
        OutlineInputBorder,
        StatelessWidget,
        TextAlign,
        TextField,
        TextInputType,
        Widget,
        BorderRadius,
        BorderSide,
        MouseCursor;

class CreateInput extends StatelessWidget {
  final bool enabled;
  final bool readOnly;
  final String placeholder;
  final bool autofocus;
  final bool isMultiline;

  const CreateInput({
    super.key,
    this.enabled = true,
    this.readOnly = false,
    this.autofocus = false,
    this.isMultiline = false,
    required this.placeholder,
  });

  @override
  Widget build(BuildContext context) {
    return TextField(
      enabled: enabled,
      readOnly: readOnly,
      decoration: InputDecoration(
        hintText: placeholder,
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(8.0),
          borderSide: const BorderSide(width: 1.0),
        ),
      ),
      autofocus: autofocus,
      textAlign: TextAlign.center,
      keyboardType: isMultiline ? TextInputType.multiline : null,
      maxLines: isMultiline ? 2 : 1,
      mouseCursor: readOnly ? MouseCursor.defer : null,
    );
  }
}

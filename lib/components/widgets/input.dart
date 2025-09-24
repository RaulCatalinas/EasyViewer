import 'package:flutter/material.dart'
    show
        BorderRadius,
        BorderSide,
        BuildContext,
        InputDecoration,
        MouseCursor,
        OutlineInputBorder,
        StatelessWidget,
        TextAlign,
        TextEditingController,
        TextField,
        TextInputType,
        Widget;
import 'package:flutter/rendering.dart';

class CreateInput extends StatelessWidget {
  final bool enabled;
  final bool readOnly;
  final String placeholder;
  final bool autofocus;
  final bool isMultiline;
  final String? initialValue;

  const CreateInput({
    super.key,
    this.enabled = true,
    this.readOnly = false,
    this.autofocus = false,
    this.isMultiline = false,
    this.initialValue,
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
      textAlignVertical: TextAlignVertical.center,
      enableSuggestions: false,
      controller: TextEditingController(text: initialValue),
    );
  }
}

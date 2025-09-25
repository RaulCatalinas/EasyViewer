import 'package:flutter/material.dart'
    show
        BorderRadius,
        BorderSide,
        BuildContext,
        InputDecoration,
        MouseCursor,
        OutlineInputBorder,
        State,
        StatefulWidget,
        TextAlign,
        TextEditingController,
        TextField,
        TextInputType,
        Widget;
import 'package:flutter/rendering.dart';

// ignore: must_be_immutable
class CreateInput extends StatefulWidget {
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
  State<StatefulWidget> createState() => CreateInputState();
}

class CreateInputState extends State<CreateInput> {
  final inputController = TextEditingController();

  @override
  void initState() {
    super.initState();
    inputController.text = widget.initialValue ?? '';
  }

  String getText() {
    return inputController.text;
  }

  void setText(String newText) {
    inputController.text = newText;
  }

  @override
  void dispose() {
    inputController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return TextField(
      enabled: widget.enabled,
      readOnly: widget.readOnly,
      decoration: InputDecoration(
        hintText: widget.placeholder,
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(8.0),
          borderSide: const BorderSide(width: 1.0),
        ),
      ),
      autofocus: widget.autofocus,
      textAlign: TextAlign.center,
      keyboardType: widget.isMultiline ? TextInputType.multiline : null,
      maxLines: widget.isMultiline ? 2 : 1,
      mouseCursor: widget.readOnly ? MouseCursor.defer : null,
      textAlignVertical: TextAlignVertical.center,
      enableSuggestions: false,
      controller: inputController,
    );
  }
}

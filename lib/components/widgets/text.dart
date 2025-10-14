import 'package:flutter/material.dart'
    show BuildContext, StatelessWidget, Text, TextAlign, TextStyle, Widget;

class CreateText extends StatelessWidget {
  final String text;
  final double? fontSize;

  const CreateText({super.key, required this.text, this.fontSize});

  @override
  Widget build(BuildContext context) {
    return Text(
      text,
      style: TextStyle(fontSize: fontSize),
      textAlign: TextAlign.center,
    );
  }
}

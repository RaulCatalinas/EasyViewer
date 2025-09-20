import 'package:flutter/material.dart'
    show BuildContext, StatelessWidget, Text, TextAlign, TextStyle, Widget;

class CreateText extends StatelessWidget {
  final String text;

  const CreateText({super.key, required this.text});

  @override
  Widget build(BuildContext context) {
    return Text(
      text,
      style: TextStyle(fontFamily: "Arial"),
      textAlign: TextAlign.center,
    );
  }
}

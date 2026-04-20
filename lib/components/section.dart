import 'package:flutter/material.dart'
    show
        BuildContext,
        Card,
        Column,
        Padding,
        SizedBox,
        StatelessWidget,
        Text,
        TextStyle,
        Widget;

class Section extends StatelessWidget {
  final String title;
  final Widget content;

  const Section({super.key, required this.title, required this.content});

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const .symmetric(vertical: 8),
      child: Column(
        mainAxisAlignment: .center,
        children: [
          Text(title, style: const TextStyle(fontSize: 18, fontWeight: .w600)),
          const SizedBox(height: 16),
          Card(child: content),
        ],
      ),
    );
  }
}

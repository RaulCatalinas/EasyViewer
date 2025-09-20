import 'package:flutter/material.dart'
    show BuildContext, Checkbox, StatelessWidget, ValueChanged, Widget;

class CreateCheckbox extends StatelessWidget {
  final bool value;
  final ValueChanged<bool?> onChanged;
  final String semanticLabel;
  const CreateCheckbox({
    super.key,
    this.value = false,
    required this.onChanged,
    required this.semanticLabel,
  });

  @override
  Widget build(BuildContext context) {
    return Checkbox(
      value: value,
      onChanged: onChanged,
      semanticLabel: semanticLabel,
    );
  }
}

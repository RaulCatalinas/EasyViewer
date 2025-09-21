import 'package:flutter/material.dart'
    show BuildContext, Checkbox, StatefulWidget, ValueChanged, Widget, State;

class CreateCheckbox extends StatefulWidget {
  final bool? initialValue;
  final ValueChanged<bool?> onChanged;
  final String semanticLabel;

  const CreateCheckbox({
    super.key,
    this.initialValue = true,
    required this.onChanged,
    required this.semanticLabel,
  });

  @override
  State<CreateCheckbox> createState() => _CreateCheckboxState();
}

class _CreateCheckboxState extends State<CreateCheckbox> {
  late bool? _value;

  @override
  void initState() {
    super.initState();
    _value = widget.initialValue;
  }

  @override
  Widget build(BuildContext context) {
    return Checkbox(
      value: _value,
      onChanged: (bool? newValue) {
        setState(() {
          _value = newValue;
        });
        widget.onChanged(newValue);
      },
      semanticLabel: widget.semanticLabel,
    );
  }
}

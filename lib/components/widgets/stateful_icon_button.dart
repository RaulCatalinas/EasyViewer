import 'package:flutter/material.dart'
    show
        BuildContext,
        Icon,
        IconButton,
        IconData,
        StatefulWidget,
        Widget,
        State,
        Container;

class CreateStatefulIconButton extends StatefulWidget {
  final void Function()? onPressed;
  final IconData icon;
  final String? tooltip;
  final double iconSize;
  final bool initiallyVisible;
  final bool enabled;

  const CreateStatefulIconButton({
    super.key,
    this.iconSize = 65,
    this.tooltip,
    this.initiallyVisible = true,
    this.enabled = true,
    required this.onPressed,
    required this.icon,
  });

  @override
  State<CreateStatefulIconButton> createState() =>
      CreateStatefulIconButtonState();

  void setVisible(bool visible) {}
}

class CreateStatefulIconButtonState extends State<CreateStatefulIconButton> {
  late bool _isVisible;
  late bool _enabled;

  @override
  void initState() {
    super.initState();
    _enabled = widget.enabled;
    _isVisible = widget.initiallyVisible;
  }

  void setVisible(bool visible) {
    setState(() {
      _isVisible = visible;
    });
  }

  void toggleEnabled() {
    setState(() {
      _enabled = !widget.enabled;
    });
  }

  @override
  Widget build(BuildContext context) {
    if (!_isVisible) {
      return Container();
    }

    return IconButton(
      onPressed: _enabled ? widget.onPressed : null,
      icon: Icon(widget.icon, size: widget.iconSize),
      tooltip: widget.tooltip,
      enableFeedback: true,
    );
  }
}

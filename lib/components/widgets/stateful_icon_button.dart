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
  final bool? initiallyVisible;

  const CreateStatefulIconButton({
    super.key,
    this.iconSize = 65,
    this.tooltip,
    this.initiallyVisible,
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

  @override
  void initState() {
    super.initState();
    _isVisible = widget.initiallyVisible!;
  }

  void setVisible(bool visible) {
    setState(() {
      _isVisible = visible;
    });
  }

  @override
  Widget build(BuildContext context) {
    if (!_isVisible) {
      return Container();
    }

    return IconButton(
      onPressed: widget.onPressed,
      icon: Icon(widget.icon, size: widget.iconSize),
      tooltip: widget.tooltip,
      enableFeedback: true,
    );
  }
}

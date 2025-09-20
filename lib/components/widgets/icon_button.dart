import 'package:flutter/material.dart'
    show BuildContext, Icon, IconButton, IconData, StatelessWidget, Widget;

class CreateIconButton extends StatelessWidget {
  final void Function()? onPressed;
  final IconData icon;
  final String? tooltip;
  final double iconSize;

  const CreateIconButton({
    super.key,
    this.iconSize = 65,
    this.tooltip,
    required this.onPressed,
    required this.icon,
  });

  @override
  Widget build(BuildContext context) {
    return IconButton(
      onPressed: onPressed,
      icon: Icon(icon, size: iconSize),
      tooltip: tooltip,
      enableFeedback: true,
    );
  }
}

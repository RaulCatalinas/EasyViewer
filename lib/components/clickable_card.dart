import 'package:flutter/material.dart'
    show
        BoxDecoration,
        BuildContext,
        Color,
        Colors,
        Container,
        InkWell,
        StatelessWidget,
        SystemMouseCursors,
        Theme,
        Widget,
        WidgetState,
        WidgetStateMouseCursor;

class ClickableCard extends StatelessWidget {
  final bool isSelected;
  final void Function() onTap;
  final Widget child;
  final bool enabled;

  const ClickableCard({
    super.key,
    this.enabled = true,
    required this.onTap,
    required this.child,
    required this.isSelected,
  });

  static final _mouseCursor = WidgetStateMouseCursor.resolveWith((states) {
    if (states.contains(WidgetState.disabled)) {
      return SystemMouseCursors.forbidden;
    }

    if (states.contains(WidgetState.hovered)) {
      return SystemMouseCursors.click;
    }

    return SystemMouseCursors.basic;
  });

  @override
  Widget build(BuildContext context) {
    return InkWell(
      onTap: enabled ? onTap : null,
      mouseCursor: _mouseCursor,
      child: Container(
        padding: const .symmetric(horizontal: 16, vertical: 12),
        decoration: BoxDecoration(
          color: isSelected
              ? const Color.fromRGBO(232, 69, 60, 0.15)
              : Colors.transparent,
          borderRadius: .circular(15.0),
          border: .all(
            color: isSelected
                ? const Color.fromRGBO(232, 69, 60, 1.0)
                : Theme.of(context).colorScheme.outline.withValues(alpha: 0.5),
            width: 1.5,
          ),
        ),
        child: child,
      ),
    );
  }
}

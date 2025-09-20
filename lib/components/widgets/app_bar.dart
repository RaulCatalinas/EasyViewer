import 'package:flutter/material.dart'
    show
        AppBar,
        BuildContext,
        StatelessWidget,
        Widget,
        Size,
        kToolbarHeight,
        PreferredSizeWidget;

import '../../app_settings/app_settings.dart' show AppColors;

class CreateAppBar extends StatelessWidget implements PreferredSizeWidget {
  final List<Widget> actions;

  const CreateAppBar({super.key, required this.actions});

  @override
  Widget build(BuildContext context) {
    return AppBar(
      actions: actions,
      backgroundColor: AppColors.appBarBgColorThemeLight,
    );
  }

  @override
  Size get preferredSize => const Size.fromHeight(kToolbarHeight);
}

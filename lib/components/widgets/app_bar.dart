import 'package:flutter/material.dart'
    show AppBar, BuildContext, StatelessWidget, Widget;

import '/app_settings/app_settings.dart' show AppColors;

class CreateAppBar extends StatelessWidget {
  final List<Widget> actions;

  const CreateAppBar({super.key, required this.actions});

  @override
  Widget build(BuildContext context) {
    return AppBar(
      actions: actions,
      backgroundColor: AppColors.appBarBgColorThemeLight,
    );
  }
}

import 'package:flutter/material.dart'
    show
        AlwaysStoppedAnimation,
        BuildContext,
        LinearProgressIndicator,
        StatelessWidget,
        Widget;

import '../../app_settings/app_settings.dart' show AppColors;

class CreateProgressBar extends StatelessWidget {
  final double? progress;

  const CreateProgressBar({super.key, this.progress});

  @override
  Widget build(BuildContext context) {
    return LinearProgressIndicator(
      value: progress,
      valueColor: AlwaysStoppedAnimation(AppColors.progressBarColor),
    );
  }
}

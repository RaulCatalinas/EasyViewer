import 'package:flutter/material.dart'
    show BuildContext, LinearProgressIndicator, State, StatefulWidget, Widget;

import '/app_settings/app_settings.dart' show AppColors;

class CreateProgressBar extends StatefulWidget {
  final double? progress;

  const CreateProgressBar({super.key, this.progress});

  @override
  State<StatefulWidget> createState() => CreateProgressBarState();
}

class CreateProgressBarState extends State<CreateProgressBar> {
  late double? _progress;

  @override
  void initState() {
    super.initState();
    _progress = widget.progress;
  }

  void toggleState() {
    setState(() {
      _progress = _progress == null ? 0 : null;
    });
  }

  @override
  Widget build(BuildContext context) {
    return LinearProgressIndicator(
      value: _progress,
      color: AppColors.progressBarColor,
    );
  }
}

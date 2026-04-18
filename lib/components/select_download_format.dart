import 'package:easyviewer/enums/download_type.dart' show DownloadType;
import 'package:fluikit/widgets.dart' show FluiText;
import 'package:flutter/material.dart'
    show
        BuildContext,
        Column,
        Radio,
        RadioGroup,
        Row,
        SizedBox,
        State,
        StatefulWidget,
        ValueNotifier,
        Widget,
        WidgetState,
        WidgetStateMouseCursor,
        SystemMouseCursors;

import '/l10n/app_localizations.dart' show AppLocalizations;

class SelectDownloadFormat extends StatefulWidget {
  final ValueNotifier<DownloadType?> notifier;

  const SelectDownloadFormat({super.key, required this.notifier});

  @override
  State<StatefulWidget> createState() => SelectDownloadFormatState();
}

class SelectDownloadFormatState extends State<SelectDownloadFormat> {
  DownloadType? _downloadType = .video;
  bool _enabled = true;

  final _commonMouseCursor = WidgetStateMouseCursor.resolveWith((states) {
    if (states.contains(WidgetState.disabled)) {
      return SystemMouseCursors.forbidden;
    }

    if (states.contains(WidgetState.hovered)) {
      return SystemMouseCursors.click;
    }

    return SystemMouseCursors.basic;
  });

  void toggleEnabled() => setState(() => _enabled = !_enabled);

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        FluiText(
          text: AppLocalizations.of(context)!.download_format,
          fontSize: 20,
        ),
        const SizedBox(height: 16),
        RadioGroup(
          groupValue: _downloadType,
          onChanged: (value) => setState(() {
            _downloadType = value;
            widget.notifier.value = value;
          }),
          child: Column(
            children: [
              Row(
                mainAxisAlignment: .center,
                children: [
                  Radio<DownloadType>(
                    value: .video,
                    enabled: _enabled,
                    mouseCursor: _commonMouseCursor,
                  ),
                  SizedBox(width: 16),
                  FluiText(text: 'Video', fontSize: 20),
                ],
              ),
              Row(
                mainAxisAlignment: .center,
                children: [
                  Radio<DownloadType>(
                    value: .audio,
                    enabled: _enabled,
                    mouseCursor: _commonMouseCursor,
                  ),
                  SizedBox(width: 16),
                  FluiText(text: 'Audio', fontSize: 20),
                ],
              ),
            ],
          ),
        ),
      ],
    );
  }
}

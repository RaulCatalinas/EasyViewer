import 'package:easyviewer/components/clickable_card.dart' show ClickableCard;
import 'package:easyviewer/enums/download_type.dart' show DownloadType;
import 'package:fluikit/widgets.dart';
import 'package:flutter/material.dart'
    show
        BuildContext,
        Column,
        Icon,
        Icons,
        Row,
        SizedBox,
        State,
        StatefulWidget,
        ValueNotifier,
        Widget;

class SelectDownloadFormat extends StatefulWidget {
  final ValueNotifier<DownloadType> notifier;

  const SelectDownloadFormat({super.key, required this.notifier});

  @override
  State<StatefulWidget> createState() => SelectDownloadFormatState();
}

class SelectDownloadFormatState extends State<SelectDownloadFormat> {
  bool _enabled = true;
  int clickableCardSelected = 1;

  void toggleEnabled() => setState(() => _enabled = !_enabled);

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisAlignment: .center,
      children: [
        ClickableCard(
          isSelected: clickableCardSelected == 1,
          enabled: _enabled,
          child: SizedBox(
            width: 238,
            height: 100,
            child: Column(
              mainAxisAlignment: .center,
              children: [
                Icon(Icons.play_circle_outline, size: 38),
                SizedBox(height: 8),
                FluiText(text: 'Video (MP4)'),
              ],
            ),
          ),
          onTap: () {
            setState(() {
              clickableCardSelected = 1;
              widget.notifier.value = .video;
            });
          },
        ),
        const SizedBox(width: 16),
        ClickableCard(
          isSelected: clickableCardSelected == 2,
          enabled: _enabled,
          child: SizedBox(
            width: 238,
            height: 100,
            child: Column(
              mainAxisAlignment: .center,
              children: [
                Icon(Icons.music_note, size: 38),
                SizedBox(height: 8),
                FluiText(text: 'Audio (MP3)'),
              ],
            ),
          ),
          onTap: () {
            setState(() {
              clickableCardSelected = 2;
              widget.notifier.value = .audio;
            });
          },
        ),
      ],
    );
  }
}

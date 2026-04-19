import 'package:fluikit/widgets.dart'
    show FluiProgressBar, FluiProgressBarState, FluiText;
import 'package:flutter/material.dart'
    show
        BoxFit,
        BuildContext,
        Card,
        CircularProgressIndicator,
        Color,
        Column,
        Expanded,
        GlobalKey,
        Icon,
        Icons,
        Image,
        Padding,
        Row,
        SizedBox,
        State,
        StatefulWidget,
        Widget;
import 'package:logkeeper/logkeeper.dart' show LogKeeper;

class VideoInfoCard extends StatefulWidget {
  final String? title;
  final String? thumbnailUrl;

  const VideoInfoCard({
    super.key,
    required this.title,
    required this.thumbnailUrl,
  });

  @override
  State<StatefulWidget> createState() => VideoInfoCardState();
}

class VideoInfoCardState extends State<VideoInfoCard> {
  static final _progressBarKey = GlobalKey<FluiProgressBarState>();

  @override
  Widget build(BuildContext context) {
    return Card(
      child: Padding(
        padding: const .all(8.0),
        child: Row(
          children: [
            SizedBox(
              width: 160,
              height: 90,
              child: widget.thumbnailUrl != null
                  ? Image.network(
                      widget.thumbnailUrl!,
                      fit: BoxFit.cover,
                      loadingBuilder: (_, child, loadingProgress) {
                        if (loadingProgress == null) return child;
                        return const CircularProgressIndicator();
                      },
                      errorBuilder: (_, error, stackTrace) {
                        LogKeeper.error(
                          'Error loading thumbnail image: $stackTrace',
                        );
                        return const Icon(Icons.broken_image);
                      },
                    )
                  : const Icon(Icons.video_library_outlined, size: 64),
            ),
            const SizedBox(width: 16),
            Expanded(
              child: Column(
                children: [
                  FluiText(text: widget.title ?? 'Unknown', fontSize: 23),
                  const SizedBox(height: 16),
                  FluiProgressBar(
                    key: _progressBarKey,
                    progressBarColor: Color.fromRGBO(232, 69, 60, 1.0),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }

  void toggleDownloadState() => _progressBarKey.currentState?.toggleState();
}

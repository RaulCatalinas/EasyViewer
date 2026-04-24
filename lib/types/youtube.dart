import 'dart:async' show Stream;

import 'package:youtube_explode_dart/youtube_explode_dart.dart'
    show YoutubeExplode;

typedef YouTubeStream = Stream<List<int>>;
typedef YouTubeStreamResult = ({YouTubeStream stream, YoutubeExplode yt});

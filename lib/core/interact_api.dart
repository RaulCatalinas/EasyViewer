import 'package:youtube_explode_dart/youtube_explode_dart.dart'
    show YoutubeExplode;

import '/utils/file_utils.dart' show cleanInvalidChars;

class InteractApi {
  static final _instance = InteractApi._internal();
  final youtube = YoutubeExplode();

  factory InteractApi() {
    return _instance;
  }

  InteractApi._internal();

  static Future<String> getTitle(String url) async {
    final video = await _instance.youtube.videos.get(url);

    return cleanInvalidChars(video.title);
  }
}

import 'dart:async';

import 'package:logkeeper/logkeeper.dart' show LogKeeper;
import 'package:youtube_explode_dart/youtube_explode_dart.dart'
    show VideoId, YoutubeExplode;

import '/utils/file_utils.dart' show cleanInvalidChars;

class InteractApi {
  static final _instance = InteractApi._internal();
  final youtube = YoutubeExplode();

  factory InteractApi() {
    return _instance;
  }

  InteractApi._internal();

  static Future<dynamic> getTitle(String url) async {
    try {
      final video = await _instance.youtube.videos.get(url);

      return cleanInvalidChars(video.title);
    } catch (e) {
      LogKeeper.error('Error obtaining video title: ${e.toString()}');

      rethrow;
    }
  }

  static Future<dynamic> _getStreamManifest(String url) async {
    try {
      final videoId = VideoId(url);

      return await _instance.youtube.videos.streams.getManifest(videoId);
    } catch (e) {
      LogKeeper.error('Error obtaining stream manifest: ${e.toString()}');

      rethrow;
    }
  }

  static Future<dynamic> getAudioStream(String url) async {
    try {
      final manifest = await _getStreamManifest(url);

      return _instance.youtube.videos.streams.get(
        manifest.audioOnly.withHighestBitrate(),
      );
    } catch (e) {
      LogKeeper.error('Error obtaining audio stream: ${e.toString()}');

      rethrow;
    }
  }

  static Future<dynamic> getVideoStream(String url) async {
    try {
      final manifest = await _getStreamManifest(url);

      return _instance.youtube.videos.streams.get(
        manifest.videoOnly.withHighestBitrate(),
      );
    } catch (e) {
      LogKeeper.error(
        'Error obtaining the audio stream from the video: ${e.toString()}',
      );

      rethrow;
    }
  }
}

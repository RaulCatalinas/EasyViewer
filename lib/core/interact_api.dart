import 'dart:async' show Future;

import 'package:logkeeper/logkeeper.dart' show LogKeeper;
import 'package:youtube_explode_dart/youtube_explode_dart.dart'
    show VideoId, YoutubeExplode, StreamManifest;

import '/utils/file_utils.dart' show cleanInvalidChars;
import 'core_utils.dart' show getYoutubeExplodeInstance;

class InteractApi {
  static InteractApi? _instance;
  late final YoutubeExplode youtube;

  InteractApi._internal();

  static InteractApi get instance {
    _instance ??= InteractApi._internal();
    return _instance!;
  }

  static Future<void> initialize() async {
    try {
      LogKeeper.info('Initializing InteractApi...');

      instance.youtube = await getYoutubeExplodeInstance();

      LogKeeper.info('✓ InteractApi initialized successfully');
    } catch (e, stackTrace) {
      LogKeeper.critical(
        '💀 FATAL: Failed to initialize InteractApi: ${e.toString()}',
      );
      LogKeeper.critical('Error StackTrace: $stackTrace');

      rethrow;
    }
  }

  static Future<dynamic> getTitle(String url) async {
    try {
      final video = await _instance?.youtube.videos.get(url);

      return cleanInvalidChars(video?.title ?? '');
    } catch (e) {
      LogKeeper.error('Error obtaining video title: ${e.toString()}');

      rethrow;
    }
  }

  static Future<StreamManifest> _getStreamManifest(String url) async {
    try {
      final videoId = VideoId(url);

      return instance.youtube.videos.streams.getManifest(videoId);
    } catch (e) {
      LogKeeper.error('Error obtaining stream manifest: ${e.toString()}');

      rethrow;
    }
  }

  static Future<dynamic> getAudioStream(String url) async {
    try {
      final manifest = await _getStreamManifest(url);

      final audioStreams = manifest.audioOnly;

      if (audioStreams.isEmpty) {
        throw Exception('No audio streams available');
      }

      final audioStream = audioStreams.reduce(
        (a, b) => a.bitrate.bitsPerSecond > b.bitrate.bitsPerSecond ? a : b,
      );

      return _instance?.youtube.videos.streams.get(audioStream);
    } catch (e) {
      LogKeeper.error('Error obtaining audio stream: ${e.toString()}');
      rethrow;
    }
  }

  static Future<dynamic> getVideoStream(String url) async {
    try {
      final manifest = await _getStreamManifest(url);

      final videoStreams = manifest.videoOnly;

      if (videoStreams.isEmpty) {
        throw Exception('No video streams available');
      }

      final videoStream = videoStreams.reduce(
        (a, b) => a.bitrate.bitsPerSecond > b.bitrate.bitsPerSecond ? a : b,
      );

      return _instance?.youtube.videos.streams.get(videoStream);
    } catch (e) {
      LogKeeper.error('Error obtaining the video stream: ${e.toString()}');
      rethrow;
    }
  }
}

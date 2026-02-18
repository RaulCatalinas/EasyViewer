import 'dart:async' show Future;

import 'package:logkeeper/logkeeper.dart' show LogKeeper;
import 'package:youtube_explode_dart/youtube_explode_dart.dart'
    show StreamInfoIterableExt, StreamManifest, VideoId, YoutubeExplode;

import '/utils/file_utils.dart' show cleanInvalidChars;
import 'core_utils.dart' show getYoutubeExplodeInstance;

typedef YouTubeStream = Stream<List<int>>;

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

  static Future<String> getTitle(String url) async {
    try {
      final video = await _instance?.youtube.videos.get(url);

      if (video == null) {
        throw Exception('Video not found');
      }

      return cleanInvalidChars(video.title);
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

  static Future<YouTubeStream> getAudioStream(String url) async {
    try {
      final manifest = await _getStreamManifest(url);

      final audioStreams = manifest.audioOnly;

      if (audioStreams.isEmpty) {
        throw Exception('No audio streams available');
      }

      final audioInfo = audioStreams.withHighestBitrate();

      final stream = instance.youtube.videos.streams.get(audioInfo);

      if (await stream.length == 0) {
        throw Exception('Audio stream not found');
      }

      return stream;
    } catch (e) {
      LogKeeper.error('Error obtaining audio stream: ${e.toString()}');
      rethrow;
    }
  }

  static Future<YouTubeStream> getVideoStream(String url) async {
    try {
      final manifest = await _getStreamManifest(url);

      final videoStreams = manifest.videoOnly;

      if (videoStreams.isEmpty) {
        throw Exception('No video streams available');
      }

      final videoInfo = videoStreams.withHighestBitrate();

      final stream = instance.youtube.videos.streams.get(videoInfo);

      if (await stream.length == 0) {
        throw Exception('Video stream not found');
      }

      return stream;
    } catch (e) {
      LogKeeper.error('Error obtaining the video stream: ${e.toString()}');
      rethrow;
    }
  }
}

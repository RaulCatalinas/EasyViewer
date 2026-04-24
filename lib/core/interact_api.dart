import 'dart:async' show Future;

import 'package:easyviewer/types/youtube.dart' show YouTubeStreamResult;
import 'package:logkeeper/logkeeper.dart' show LogKeeper;
import 'package:youtube_explode_dart/js_challenge.dart' show BaseEJSSolver;
import 'package:youtube_explode_dart/youtube_explode_dart.dart'
    show StreamInfoIterableExt, YoutubeExplode;

import '/utils/file_utils.dart' show cleanInvalidChars;
import 'core_utils.dart' show getDenoSolver;

class InteractApi {
  static InteractApi? _instance;
  late final BaseEJSSolver _solver;

  InteractApi._internal();

  static InteractApi get instance {
    _instance ??= InteractApi._internal();
    return _instance!;
  }

  static Future<void> initialize() async {
    try {
      LogKeeper.info('Initializing InteractApi...');
      instance._solver = await getDenoSolver();
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
    final yt = YoutubeExplode(jsSolver: instance._solver);

    try {
      final video = await yt.videos.get(url);

      return cleanInvalidChars(video.title);
    } finally {
      yt.close();
    }
  }

  static Future<String> getThumbnailUrl(String url) async {
    final yt = YoutubeExplode(jsSolver: instance._solver);

    try {
      final video = await yt.videos.get(url);

      return video.thumbnails.highResUrl;
    } finally {
      yt.close();
    }
  }

  static Future<YouTubeStreamResult> getAudioStream(String url) async {
    final yt = YoutubeExplode(jsSolver: instance._solver);

    final manifest = await yt.videos.streams.getManifest(url);
    final audioStreams = manifest.audioOnly;

    if (audioStreams.isEmpty) {
      throw Exception('No audio streams available');
    }

    final audioInfo = audioStreams.withHighestBitrate();

    return (stream: yt.videos.streams.get(audioInfo), yt: yt);
  }

  static Future<YouTubeStreamResult> getVideoStream(String url) async {
    final yt = YoutubeExplode(jsSolver: instance._solver);

    final manifest = await yt.videos.streams.getManifest(url);
    final videoStreams = manifest.videoOnly;

    if (videoStreams.isEmpty) {
      throw Exception('No video streams available');
    }

    final videoInfo = videoStreams.withHighestBitrate();

    return (stream: yt.videos.streams.get(videoInfo), yt: yt);
  }
}

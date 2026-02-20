import 'dart:async' show Future;

import 'package:logkeeper/logkeeper.dart' show LogKeeper;
import 'package:youtube_explode_dart/js_challenge.dart' show BaseEJSSolver;
import 'package:youtube_explode_dart/youtube_explode_dart.dart'
    show StreamInfoIterableExt, StreamManifest, YoutubeExplode;

import '/utils/file_utils.dart' show cleanInvalidChars;
import 'core_utils.dart' show getDenoSolver;

typedef YouTubeStream = Stream<List<int>>;

class InteractApi {
  static InteractApi? _instance;
  late final BaseEJSSolver _donoSolver;

  InteractApi._internal();

  static InteractApi get instance {
    _instance ??= InteractApi._internal();
    return _instance!;
  }

  static Future<void> initialize() async {
    try {
      LogKeeper.info('Initializing InteractApi...');

      instance._donoSolver = await getDenoSolver();

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
    final yt = YoutubeExplode(jsSolver: instance._donoSolver);

    try {
      final video = await yt.videos.get(url);

      return cleanInvalidChars(video.title);
    } catch (e) {
      LogKeeper.error('Error obtaining video title: ${e.toString()}');

      rethrow;
    } finally {
      yt.close();
    }
  }

  static Future<StreamManifest> _getStreamManifest(String url) async {
    final yt = YoutubeExplode(jsSolver: instance._donoSolver);

    try {
      print('Getting stream manifest...');

      return await yt.videos.streams.getManifest(url);
    } catch (e) {
      LogKeeper.error('Error obtaining stream manifest: ${e.toString()}');

      rethrow;
    } finally {
      yt.close();
    }
  }

  static Future<YouTubeStream> getAudioStream(String url) async {
    final yt = YoutubeExplode(jsSolver: instance._donoSolver);

    try {
      final manifest = await _getStreamManifest(url);
      final audioStreams = manifest.audioOnly;

      if (audioStreams.isEmpty) {
        throw Exception('No audio streams available');
      }

      final audioInfo = audioStreams.withHighestBitrate();

      return yt.videos.streams.get(audioInfo);
    } catch (e) {
      LogKeeper.error('Error obtaining audio stream: ${e.toString()}');
      rethrow;
    } finally {
      yt.close();
    }
  }

  static Future<YouTubeStream> getVideoStream(String url) async {
    final yt = YoutubeExplode(jsSolver: instance._donoSolver);

    try {
      final manifest = await _getStreamManifest(url);

      final videoStreams = manifest.videoOnly;

      if (videoStreams.isEmpty) {
        throw Exception('No video streams available');
      }

      final videoInfo = videoStreams.withHighestBitrate();

      final stream = yt.videos.streams.get(videoInfo);

      if (await stream.length == 0) {
        throw Exception('Video stream not found');
      }

      return stream;
    } catch (e) {
      LogKeeper.error('Error obtaining the video stream: ${e.toString()}');
      rethrow;
    } finally {
      yt.close();
    }
  }
}

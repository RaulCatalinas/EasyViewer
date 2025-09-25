import 'dart:async';

import 'package:http/http.dart' show ClientException, head;

import '/app_logging/logging_manager.dart' show LoggingManager;
import '/constants/hosts.dart' show allowHosts, google;
import '/enums/logging.dart' show LogLevels;

class DownloadValidations {
  static final _instance = DownloadValidations._internal();

  factory DownloadValidations() {
    return _instance;
  }

  DownloadValidations._internal();

  static bool nonEmptyURL(String? url) {
    if (url == null || url.isEmpty) {
      LoggingManager.writeLog(LogLevels.warning, 'No URL entered');

      throw Exception('No URL entered');
    }

    return true;
  }

  static bool checkIfYoutubeUrl(String url) {
    final host = Uri.parse(url).host;

    if (!allowHosts.contains(host)) {
      LoggingManager.writeLog(
        LogLevels.warning,
        'The $url URL is not from YouTube.',
      );

      throw Exception('The $url URL is not from YouTube.');
    }

    return true;
  }

  static Future<bool> checkInternetConnection() async {
    try {
      await head(Uri.parse(google)).timeout(Duration(seconds: 5));

      return true;
    } on TimeoutException catch (e) {
      LoggingManager.writeLog(LogLevels.error, 'Internet connection issue: $e');

      throw Exception('No internet connection');
    } on ClientException catch (e) {
      LoggingManager.writeLog(LogLevels.error, 'Internet connection issue: $e');

      throw Exception('No internet connection');
    }
  }

  static Future<bool> isYoutubeVideoAvailable(String url) async {
    // TODO: Add logic to verify that the video is available for subsequent download.
    // TODO: For now, we return true (for example) so that the compilation doesn't fail.
    return true;
  }
}

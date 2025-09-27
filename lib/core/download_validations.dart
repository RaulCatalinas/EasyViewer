import 'dart:async';

import 'package:flutter/material.dart';
import 'package:http/http.dart' show ClientException, head;

import '/app_logging/logging_manager.dart' show LoggingManager;
import '/constants/hosts.dart' show allowHosts, google;
import '/enums/logging.dart' show LogLevels;
import '/l10n/app_localizations.dart' show AppLocalizations;

class DownloadValidations {
  static final _instance = DownloadValidations._internal();

  factory DownloadValidations() {
    return _instance;
  }

  DownloadValidations._internal();

  static bool nonEmptyURL({
    required BuildContext context,
    required String? url,
  }) {
    if (url == null || url.isEmpty) {
      LoggingManager.writeLog(LogLevels.warning, 'No URL entered');

      throw Exception(AppLocalizations.of(context)!.error_empty_url);
    }

    return true;
  }

  static bool checkIfYoutubeUrl({
    required BuildContext context,
    required String url,
  }) {
    final host = Uri.parse(url).host;

    if (!allowHosts.contains(host)) {
      LoggingManager.writeLog(
        LogLevels.warning,
        'The $url URL is not from YouTube.',
      );

      return false;
    }

    return true;
  }

  static Future<bool> checkInternetConnection({
    required BuildContext context,
  }) async {
    try {
      await head(Uri.parse(google)).timeout(Duration(seconds: 5));

      return true;
    } on TimeoutException catch (e) {
      if (!context.mounted) return false;

      LoggingManager.writeLog(LogLevels.error, 'Internet connection issue: $e');

      throw Exception(AppLocalizations.of(context)!.error_connection);
    } on ClientException catch (e) {
      if (!context.mounted) return false;

      LoggingManager.writeLog(LogLevels.error, 'Internet connection issue: $e');

      throw Exception(AppLocalizations.of(context)!.error_connection);
    }
  }

  static Future<bool> isYoutubeVideoAvailable({
    required BuildContext context,
    required String url,
  }) async {
    // TODO: Add logic to verify that the video is available for subsequent download.
    // TODO: For now, we return true (for example) so that the compilation doesn't fail.
    return true;
  }
}

import 'dart:async';

import 'package:flutter/material.dart';
import 'package:http/http.dart' show ClientException, head;
import 'package:logkeeper/logkeeper.dart' show LogKeeper;
import 'package:youtube_explode_dart/youtube_explode_dart.dart'
    show
        VideoRequiresPurchaseException,
        VideoUnplayableException,
        YoutubeExplode,
        VideoUnavailableException;

import '/constants/hosts.dart' show allowHosts, google;
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
      LogKeeper.warning('No URL entered');

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
      LogKeeper.warning('The $url URL is not from YouTube.');

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

      LogKeeper.error('Internet connection timeout: $e');

      throw Exception(AppLocalizations.of(context)!.error_connection);
    } on ClientException catch (e) {
      if (!context.mounted) return false;

      LogKeeper.error('Internet connection issue: $e');

      throw Exception(AppLocalizations.of(context)!.error_connection);
    }
  }

  static Future<bool> isYoutubeVideoAvailable({
    required BuildContext context,
    required String url,
  }) async {
    final youtube = YoutubeExplode();

    try {
      final video = await youtube.videos.get(url);

      if (video.isLive) {
        LogKeeper.warning('Video is a live stream: $url');

        if (!context.mounted) return false;

        throw Exception(AppLocalizations.of(context)!.error_live_stream);
      }

      await youtube.videos.streamsClient.getManifest(video.id);

      youtube.close();

      return true;
    } on VideoUnavailableException catch (e) {
      youtube.close();

      print(e.message);

      if (!context.mounted) return false;

      LogKeeper.error('Video unavailable: $url');

      throw Exception(AppLocalizations.of(context)!.error_unavailable_video);
    } on VideoRequiresPurchaseException catch (e) {
      youtube.close();

      print(e.message);

      if (!context.mounted) return false;

      LogKeeper.error('Video requires purchase: $url');

      throw Exception(AppLocalizations.of(context)!.error_only_members);
    } on VideoUnplayableException catch (e) {
      youtube.close();

      if (!context.mounted) return false;

      LogKeeper.error('Video unplayable: ${e.message}');

      throw Exception(AppLocalizations.of(context)!.error_unavailable_video);
    } on Exception catch (e) {
      youtube.close();

      if (!context.mounted) return false;

      LogKeeper.error('Error checking video availability: $e');

      throw Exception(AppLocalizations.of(context)!.error_default);
    }
  }
}

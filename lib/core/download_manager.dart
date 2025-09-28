import 'dart:io' show File;

import 'package:flutter/material.dart' show BuildContext;
import 'package:path/path.dart';

import '/app_logging/logging_manager.dart' show LoggingManager;
import '/components/dialogs/error_dialog.dart' show ErrorDialog;
import '/enums/logging.dart' show LogLevels;
import '/enums/user_preferences.dart' show UserPreferencesKeys;
import '/managers/user_preferences_manager/user_preferences_manager.dart'
    show UserPreferencesManager;
import '/utils/directories_utils.dart' show openDirectory;
import '/utils/file_utils.dart' show deleteFile;
import '/utils/youtube_utils.dart' show separateUrls;
import 'download_validations.dart' show DownloadValidations;
import 'interact_api.dart' show InteractApi;

class DownloadManager {
  static final _instance = DownloadManager._internal();
  List<String> _separatedUrls = [];
  String _urlToDownload = '';
  int _downloadsCompletedSuccessfully = 0;
  String _videoTitle = '';

  factory DownloadManager() {
    return _instance;
  }

  DownloadManager._internal();

  static Future<void> downloadVideo({
    required BuildContext context,
    required String? rawUrlsToDownload,
    required bool downloadAudio,
    required Function(String newText)? setText,
    required Future<bool> Function() setDefaultDirectoryIfIsNecessary,
  }) async {
    try {
      _instance._downloadsCompletedSuccessfully = 0;

      DownloadValidations.nonEmptyURL(url: rawUrlsToDownload, context: context);

      await DownloadValidations.checkInternetConnection(context: context);

      _instance._separatedUrls = separateUrls(rawUrlsToDownload!);

      setText!(_instance._separatedUrls.join('\n'));

      _instance._separatedUrls.removeWhere(
        (url) =>
            !DownloadValidations.checkIfYoutubeUrl(url: url, context: context),
      );

      setText(_instance._separatedUrls.join('\n'));

      String downloadDirectory = UserPreferencesManager.getPreference(
        UserPreferencesKeys.downloadDirectory,
      );

      for (final url in List.from(_instance._separatedUrls)) {
        try {
          _instance._videoTitle = '';

          final isDefaultDirectorySet =
              await setDefaultDirectoryIfIsNecessary();

          if (isDefaultDirectorySet) {
            downloadDirectory = UserPreferencesManager.getPreference(
              UserPreferencesKeys.downloadDirectory,
            );
          }

          _instance._urlToDownload = url;

          _instance._videoTitle = await InteractApi.getTitle(
            _instance._urlToDownload,
          );

          _instance._videoTitle += downloadAudio ? '.mp3' : '.mp4';

          final downloadFile = File(
            join(downloadDirectory, _instance._videoTitle),
          );

          await downloadFile.create();

          final audioStream = await InteractApi.getAudioStream(
            _instance._urlToDownload,
          );

          final downloadFileStream = downloadFile.openWrite();

          if (downloadAudio) {
            await audioStream.pipe(downloadFileStream);

            downloadFileStream.flush();
          }

          _instance._downloadsCompletedSuccessfully++;
        } catch (e) {
          LoggingManager.writeLog(
            LogLevels.error,
            "Error downloading the video: ${e.toString().replaceAll('Exception: ', '')}",
          );

          await deleteFile(
            directory: downloadDirectory,
            fileName: _instance._videoTitle,
          );
        } finally {
          _instance._separatedUrls.remove(_instance._urlToDownload);

          setText(_instance._separatedUrls.join('\n'));
        }
      }

      if (_instance._downloadsCompletedSuccessfully > 0) {
        openDirectory(downloadDirectory);
      }
    } catch (e) {
      if (!context.mounted) {
        LoggingManager.writeLog(
          LogLevels.warning,
          'Context not mounted, skipping showing the error',
        );

        return;
      }

      ErrorDialog.show(
        context,
        content: e.toString().replaceAll('Exception: ', ''),
      );
    }
  }
}

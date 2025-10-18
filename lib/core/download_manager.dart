import 'dart:io' show File;

import 'package:flutter/material.dart' show BuildContext;
import 'package:logkeeper/logkeeper.dart' show LogKeeper;
import 'package:path/path.dart';

import '/components/dialogs/error_dialog.dart' show ErrorDialog;
import '/enums/user_preferences.dart' show UserPreferencesKeys;
import '/managers/user_preferences_manager/user_preferences_manager.dart'
    show UserPreferencesManager;
import '/services/ffmpeg_service.dart' show mergeAudioAndVideo;
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
  File _downloadFile = File('');

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
          if (!context.mounted) return;

          await DownloadValidations.isYoutubeVideoAvailable(
            context: context,
            url: url,
          );

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

          final audioStream = await InteractApi.getAudioStream(
            _instance._urlToDownload,
          );

          _instance._downloadFile = File(
            join(
              downloadDirectory,
              join(_instance._videoTitle, downloadAudio ? '.mp3' : '.mp3.temp'),
            ),
          );

          final downloadFileStream = _instance._downloadFile.openWrite();

          await audioStream.pipe(downloadFileStream);

          await downloadFileStream.flush();
          await downloadFileStream.close();

          if (!downloadAudio) {
            final videoSteam = await InteractApi.getVideoStream(
              _instance._urlToDownload,
            );

            _instance._downloadFile = File(
              join(downloadDirectory, '${_instance._videoTitle}.mp4'),
            );

            final videoFileStream = _instance._downloadFile.openWrite();

            await videoSteam.pipe(videoFileStream);

            await videoFileStream.flush();
            await videoFileStream.close();

            await mergeAudioAndVideo(
              audioFile: File(
                join(downloadDirectory, '${_instance._videoTitle}.mp3'),
              ),
              videoFile: _instance._downloadFile,
              outputPath: join(
                downloadDirectory,
                '${_instance._videoTitle}.mp4',
              ),
            );
          }

          _instance._downloadsCompletedSuccessfully++;
        } catch (e) {
          LogKeeper.error(
            "Error downloading the video: ${e.toString().replaceAll('Exception: ', '')}",
          );

          await deleteFile(fileToDelete: _instance._downloadFile);
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
        LogKeeper.warning('Context not mounted, skipping showing the error');

        return;
      }

      ErrorDialog.show(
        context,
        content: e.toString().replaceAll('Exception: ', ''),
      );
    }
  }
}

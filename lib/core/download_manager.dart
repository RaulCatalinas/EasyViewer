import 'dart:io' show File;

import 'package:fluikit/dialogs.dart' show FluiErrorDialog;
import 'package:flutter/material.dart' show BuildContext;
import 'package:logkeeper/logkeeper.dart' show LogKeeper;
import 'package:path/path.dart' show join;

import '/enums/user_preferences.dart' show UserPreferencesKeys;
import '/managers/user_preferences_manager/user_preferences_manager.dart'
    show UserPreferencesManager;
import '/services/ffmpeg_service.dart' show mergeAudioAndVideo;
import '/utils/directories_utils.dart' show openDirectory;
import '/utils/file_utils.dart' show createFileIfNotExist, deleteFile;
import '/utils/youtube_utils.dart' show separateUrls;
import 'download_validations.dart' show DownloadValidations;
import 'interact_api.dart' show InteractApi;

class DownloadManager {
  static final _instance = DownloadManager._internal();

  factory DownloadManager() {
    return _instance;
  }

  DownloadManager._internal();

  int _downloadsCompletedSuccessfully = 0;

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

      final urls = await _prepareUrls(
        context: context,
        rawUrls: rawUrlsToDownload!,
        setText: setText!,
      );

      String downloadDirectory = UserPreferencesManager.getPreference(
        UserPreferencesKeys.downloadDirectory,
      );

      for (final url in urls) {
        if (!context.mounted) return;

        downloadDirectory = await _resolveDownloadDirectory(
          currentDirectory: downloadDirectory,
          setDefaultDirectoryIfIsNecessary: setDefaultDirectoryIfIsNecessary,
        );

        await _processSingleUrl(
          context: context,
          url: url,
          downloadAudio: downloadAudio,
          downloadDirectory: downloadDirectory,
          setText: setText,
          remainingUrls: urls,
        );
      }

      if (_instance._downloadsCompletedSuccessfully > 0) {
        openDirectory(downloadDirectory);
      }
    } catch (e) {
      _showErrorIfMounted(context, e);
    }
  }

  static Future<List<String>> _prepareUrls({
    required BuildContext context,
    required String rawUrls,
    required Function(String) setText,
  }) async {
    final separated = separateUrls(rawUrls);
    setText(separated.join('\n'));

    final validUrls = separated
        .where(
          (url) =>
              DownloadValidations.checkIfYoutubeUrl(url: url, context: context),
        )
        .toList();

    setText(validUrls.join('\n'));

    return validUrls;
  }

  static Future<String> _resolveDownloadDirectory({
    required String currentDirectory,
    required Future<bool> Function() setDefaultDirectoryIfIsNecessary,
  }) async {
    final isDefaultDirectorySet = await setDefaultDirectoryIfIsNecessary();

    if (isDefaultDirectorySet) {
      return UserPreferencesManager.getPreference(
        UserPreferencesKeys.downloadDirectory,
      );
    }

    return currentDirectory;
  }

  static Future<void> _processSingleUrl({
    required BuildContext context,
    required String url,
    required bool downloadAudio,
    required String downloadDirectory,
    required Function(String) setText,
    required List<String> remainingUrls,
  }) async {
    File downloadFile = File('');

    try {
      await DownloadValidations.isYoutubeVideoAvailable(
        context: context,
        url: url,
      );

      final videoTitle = await InteractApi.getTitle(url);

      downloadFile = downloadAudio
          ? await _downloadAudioOnly(
              url: url,
              videoTitle: videoTitle,
              downloadDirectory: downloadDirectory,
            )
          : await _downloadVideoWithAudio(
              url: url,
              videoTitle: videoTitle,
              downloadDirectory: downloadDirectory,
            );

      _instance._downloadsCompletedSuccessfully++;
    } catch (e) {
      LogKeeper.error(
        "Error downloading the video: ${e.toString().replaceAll('Exception: ', '')}",
      );

      await deleteFile(fileToDelete: downloadFile);

      _showErrorIfMounted(context, e);
    } finally {
      remainingUrls.remove(url);
      setText(remainingUrls.join('\n'));
    }
  }

  static Future<File> _downloadAudioOnly({
    required String url,
    required String videoTitle,
    required String downloadDirectory,
  }) async {
    final audioStream = await InteractApi.getAudioStream(url);
    final file = File(join(downloadDirectory, '$videoTitle.mp3'));

    await createFileIfNotExist(file);

    final fileStream = file.openWrite();

    await audioStream.pipe(fileStream);
    await fileStream.flush();
    await fileStream.close();

    return file;
  }

  static Future<File> _downloadVideoWithAudio({
    required String url,
    required String videoTitle,
    required String downloadDirectory,
  }) async {
    final audioFile = await _downloadAudioTemp(
      url: url,
      videoTitle: videoTitle,
      downloadDirectory: downloadDirectory,
    );

    final videoFile = await _downloadVideoStream(
      url: url,
      videoTitle: videoTitle,
      downloadDirectory: downloadDirectory,
    );

    await mergeAudioAndVideo(
      audioFile: audioFile,
      videoFile: videoFile,
      outputPath: join(downloadDirectory, '$videoTitle.mp4'),
    );

    return videoFile;
  }

  static Future<File> _downloadAudioTemp({
    required String url,
    required String videoTitle,
    required String downloadDirectory,
  }) async {
    final audioStream = await InteractApi.getAudioStream(url);
    final file = File(join(downloadDirectory, '$videoTitle.mp3.temp'));

    await createFileIfNotExist(file);

    final fileStream = file.openWrite();

    await audioStream.pipe(fileStream);
    await fileStream.flush();
    await fileStream.close();

    return file;
  }

  static Future<File> _downloadVideoStream({
    required String url,
    required String videoTitle,
    required String downloadDirectory,
  }) async {
    final videoStream = await InteractApi.getVideoStream(url);
    final file = File(join(downloadDirectory, '$videoTitle.mp4'));

    await createFileIfNotExist(file);

    final fileStream = file.openWrite();

    await videoStream.pipe(fileStream);
    await fileStream.flush();
    await fileStream.close();

    return file;
  }

  static void _showErrorIfMounted(BuildContext context, Object e) {
    if (!context.mounted) {
      LogKeeper.warning('Context not mounted, skipping showing the error');
      return;
    }

    FluiErrorDialog.show(
      context,
      content: e.toString().replaceAll('Exception: ', ''),
    );
  }
}

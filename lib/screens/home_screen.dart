import 'package:easyviewer/components/select_download_format.dart';
import 'package:easyviewer/core/download_manager.dart';
import 'package:easyviewer/enums/download_type.dart';
import 'package:easyviewer/utils/paths.dart';
import 'package:fluikit/widgets.dart'
    show
        FluiInput,
        FluiInputState,
        FluiStatefulTextButton,
        FluiStatefulTextButtonState;
import 'package:flutter/material.dart'
    show
        BuildContext,
        Center,
        Color,
        Column,
        Expanded,
        GlobalKey,
        Icons,
        Padding,
        Row,
        Scaffold,
        SizedBox,
        StatelessWidget,
        ValueNotifier,
        Widget;
import 'package:logkeeper/logkeeper.dart';

import '/enums/user_preferences.dart' show UserPreferencesKeys;
import '/handlers/select_directory.dart' show selectDirectory;
import '/l10n/app_localizations.dart' show AppLocalizations;
import '/managers/user_preferences_manager/user_preferences_manager.dart'
    show UserPreferencesManager;

class HomeScreen extends StatelessWidget {
  final _inputDirectoryKey = GlobalKey<FluiInputState>();
  final _inputUrlsKey = GlobalKey<FluiInputState>();
  final _buttonDirectoryKey = GlobalKey<FluiStatefulTextButtonState>();
  final _buttonDownloadKey = GlobalKey<FluiStatefulTextButtonState>();
  final _downloadFormatKey = GlobalKey<SelectDownloadFormatState>();
  final _format = ValueNotifier<DownloadType>(.video);

  HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Padding(
          padding: .all(25.0),
          child: Column(
            mainAxisAlignment: .center,
            children: [
              FluiInput(
                key: _inputUrlsKey,
                placeholder: AppLocalizations.of(context)!.placeholder_url,
                isMultiline: true,
                autofocus: true,
                maxLines: 2,
                borderColor: Color.fromRGBO(232, 69, 60, 0.7),
                label: AppLocalizations.of(context)!.input_urls_label,
                labelFontSize: 16,
                borderRadius: .circular(15.0),
              ),

              const SizedBox(height: 30),

              SelectDownloadFormat(key: _downloadFormatKey, notifier: _format),

              const SizedBox(height: 30),

              Row(
                mainAxisAlignment: .center,
                children: [
                  Expanded(
                    child: FluiInput(
                      label: AppLocalizations.of(
                        context,
                      )!.input_directory_label,
                      labelFontSize: 16,
                      key: _inputDirectoryKey,
                      placeholder: AppLocalizations.of(
                        context,
                      )!.placeholder_directory,
                      readOnly: true,
                      initialValue: UserPreferencesManager.getPreference(
                        UserPreferencesKeys.downloadDirectory,
                      ),
                      borderRadius: .circular(15.0),
                    ),
                  ),
                  const SizedBox(width: 16),

                  FluiStatefulTextButton(
                    key: _buttonDirectoryKey,
                    text: AppLocalizations.of(context)!.select_directory,
                    borderRadius: .circular(15.0),
                    backgroundColor: const Color.fromRGBO(27, 27, 35, 0.7),
                    icon: Icons.folder_outlined,
                    iconSize: 22,
                    onPressed: () async {
                      final directory = await selectDirectory(context);

                      UserPreferencesManager.setPreference(
                        UserPreferencesKeys.downloadDirectory,
                        directory,
                      );

                      _inputDirectoryKey.currentState?.setText(directory);
                    },
                  ),
                ],
              ),

              const SizedBox(height: 30),

              SizedBox(
                width: double.infinity,
                height: 50,
                child: FluiStatefulTextButton(
                  key: _buttonDownloadKey,
                  backgroundColor: const Color.fromRGBO(232, 69, 60, 1.0),
                  fontSize: 20,
                  text: 'Download',
                  borderRadius: .circular(15.0),
                  icon: Icons.download,
                  onPressed: () async {
                    await _processDownload(
                      context: context,
                      downloadAudio: _format.value == .audio,
                    );
                  },
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  void _toggleStateWidgets() {
    _inputUrlsKey.currentState?.toggleEnabled();
    _buttonDirectoryKey.currentState?.toggleEnabled();
    _buttonDownloadKey.currentState?.toggleEnabled();
    //_progressBarKey.currentState?.toggleState();
    _downloadFormatKey.currentState?.toggleEnabled();
  }

  Future<bool> _setDefaultDirectoryIfIsNecessary() async {
    final selectedDirectory = UserPreferencesManager.getPreference(
      UserPreferencesKeys.downloadDirectory,
    );

    final isDirectoryEmpty = selectedDirectory == '';

    final existSelectedDirectory = existsDirectory(selectedDirectory);

    if (isDirectoryEmpty || !existSelectedDirectory) {
      final defaultDirectory = await getUserDesktopPath();

      UserPreferencesManager.setPreference(
        UserPreferencesKeys.downloadDirectory,
        defaultDirectory,
      );

      _inputDirectoryKey.currentState?.setText(defaultDirectory);

      return true;
    }

    return false;
  }

  Future<void> _processDownload({
    required bool downloadAudio,
    required BuildContext context,
  }) async {
    try {
      _toggleStateWidgets();

      await _setDefaultDirectoryIfIsNecessary();

      final urlsToDownload = _inputUrlsKey.currentState?.getText();

      if (!context.mounted) {
        LogKeeper.warning('Context not mounted, skipping download');

        return;
      }

      await DownloadManager.downloadVideo(
        context: context,
        rawUrlsToDownload: urlsToDownload,
        downloadAudio: downloadAudio,
        setText: _inputUrlsKey.currentState?.setText,
        setDefaultDirectoryIfIsNecessary: _setDefaultDirectoryIfIsNecessary,
      );
    } catch (e) {
      LogKeeper.error('Error while downloading the video: ${e.toString()}');
    } finally {
      _toggleStateWidgets();
    }
  }
}

import 'package:fluikit/widgets.dart'
    show
        FluiInput,
        FluiInputState,
        FluiStatefulIconButton,
        FluiStatefulIconButtonState;
import 'package:flutter/material.dart'
    show
        Center,
        Column,
        EdgeInsets,
        Icons,
        MainAxisAlignment,
        Padding,
        Row,
        Scaffold,
        SizedBox,
        StatelessWidget,
        Widget,
        BuildContext,
        GlobalKey;
import 'package:logkeeper/logkeeper.dart' show LogKeeper;

import '/components/progress_bar.dart'
    show CreateProgressBar, CreateProgressBarState;
import '/core/download_manager.dart' show DownloadManager;
import '/enums/user_preferences.dart' show UserPreferencesKeys;
import '/handlers/select_directory.dart' show selectDirectory;
import '/l10n/app_localizations.dart' show AppLocalizations;
import '/managers/user_preferences_manager/user_preferences_manager.dart'
    show UserPreferencesManager;
import '/utils/paths.dart' show getUserDesktopPath, existsDirectory;
import 'settings_ui.dart' show SettingsUI;

class MainUI extends StatelessWidget {
  final _inputDirectoryKey = GlobalKey<FluiInputState>();
  final _inputUrlsKey = GlobalKey<FluiInputState>();
  final _buttonDirectoryKey = GlobalKey<FluiStatefulIconButtonState>();
  final _buttonDownloadVideoKey = GlobalKey<FluiStatefulIconButtonState>();
  final _buttonDownloadAudioKey = GlobalKey<FluiStatefulIconButtonState>();
  final _progressBarKey = GlobalKey<CreateProgressBarState>();

  MainUI({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: SettingsUI(),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(25.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              Column(
                mainAxisAlignment: MainAxisAlignment.center,
                spacing: 15,
                children: [
                  FluiInput(
                    key: _inputUrlsKey,
                    placeholder: AppLocalizations.of(context)!.placeholder_url,
                    isMultiline: true,
                    autofocus: true,
                  ),
                  FluiInput(
                    key: _inputDirectoryKey,
                    placeholder: AppLocalizations.of(
                      context,
                    )!.placeholder_directory,
                    readOnly: true,
                    initialValue: UserPreferencesManager.getPreference(
                      UserPreferencesKeys.downloadDirectory,
                    ),
                  ),
                ],
              ),

              const SizedBox(height: 20),

              Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  FluiStatefulIconButton(
                    key: _buttonDirectoryKey,
                    onPressed: () async {
                      final directory = await selectDirectory(context);

                      UserPreferencesManager.setPreference(
                        UserPreferencesKeys.downloadDirectory,
                        directory,
                      );

                      _inputDirectoryKey.currentState?.setText(directory);
                    },
                    icon: Icons.folder,
                    tooltip: AppLocalizations.of(
                      context,
                    )!.select_download_directory,
                  ),

                  const SizedBox(height: 17),

                  Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      FluiStatefulIconButton(
                        key: _buttonDownloadVideoKey,
                        onPressed: () async {
                          await _processDownload(
                            downloadAudio: false,
                            context: context,
                          );
                        },
                        icon: Icons.video_file,
                        tooltip: AppLocalizations.of(context)!.download_video,
                      ),

                      FluiStatefulIconButton(
                        key: _buttonDownloadAudioKey,
                        onPressed: () async {
                          await _processDownload(
                            downloadAudio: true,
                            context: context,
                          );
                        },
                        icon: Icons.audio_file,
                        tooltip: AppLocalizations.of(context)!.download_audio,
                      ),
                    ],
                  ),
                  const SizedBox(height: 13),
                  CreateProgressBar(key: _progressBarKey),
                ],
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
    _buttonDownloadVideoKey.currentState?.toggleEnabled();
    _buttonDownloadAudioKey.currentState?.toggleEnabled();
    _progressBarKey.currentState?.toggleState();
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

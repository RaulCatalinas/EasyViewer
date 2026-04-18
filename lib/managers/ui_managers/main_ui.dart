import 'package:easyviewer/components/select_download_format.dart';
import 'package:easyviewer/enums/download_type.dart' show DownloadType;
import 'package:fluikit/widgets.dart'
    show
        FluiAppBar,
        FluiInput,
        FluiInputState,
        FluiProgressBar,
        FluiProgressBarState,
        FluiStatefulTextButton,
        FluiStatefulTextButtonState;
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart'
    show
        BuildContext,
        Center,
        Column,
        GlobalKey,
        Icons,
        Padding,
        Row,
        Scaffold,
        SizedBox,
        StatelessWidget,
        Widget;
import 'package:logkeeper/logkeeper.dart' show LogKeeper;

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
  final _buttonDirectoryKey = GlobalKey<FluiStatefulTextButtonState>();
  final _buttonDownloadKey = GlobalKey<FluiStatefulTextButtonState>();
  final _progressBarKey = GlobalKey<FluiProgressBarState>();
  final _downloadFormatKey = GlobalKey<SelectDownloadFormatState>();
  final _format = ValueNotifier<DownloadType?>(.video);

  MainUI({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: FluiAppBar(
        actions: [],
        drawerIcon: Icons.settings,
        drawerIconTooltip: AppLocalizations.of(
          context,
        )!.settings_menu_icon_tooltip,
      ),
      drawer: SettingsUI(),
      body: Center(
        child: Padding(
          padding: const .all(25.0),
          child: Column(
            mainAxisAlignment: .center,
            children: <Widget>[
              Column(
                mainAxisAlignment: .center,
                spacing: 15,
                children: [
                  FluiInput(
                    key: _inputUrlsKey,
                    placeholder: AppLocalizations.of(context)!.placeholder_url,
                    isMultiline: true,
                    autofocus: true,
                  ),
                  const SizedBox(height: 8),
                  Row(
                    mainAxisAlignment: .center,
                    children: [
                      SizedBox(
                        width: 250,
                        child: FluiInput(
                          key: _inputDirectoryKey,
                          placeholder: AppLocalizations.of(
                            context,
                          )!.placeholder_directory,
                          readOnly: true,
                          initialValue: UserPreferencesManager.getPreference(
                            UserPreferencesKeys.downloadDirectory,
                          ),
                        ),
                      ),
                      const SizedBox(width: 16),
                      FluiStatefulTextButton(
                        key: _buttonDirectoryKey,
                        text: AppLocalizations.of(
                          context,
                        )!.select_download_directory,
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
                ],
              ),

              const SizedBox(height: 16),

              //SelectDownloadFormat(key: _downloadFormatKey, notifier: _format),
              const SizedBox(height: 16),

              FluiStatefulTextButton(
                key: _buttonDownloadKey,
                text: AppLocalizations.of(context)!.download,
                fontSize: 25,
                onPressed: () async {
                  await _processDownload(
                    downloadAudio: _format.value == .audio,
                    context: context,
                  );
                },
              ),

              const SizedBox(height: 16),
              FluiProgressBar(key: _progressBarKey),
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
    _progressBarKey.currentState?.toggleState();
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

import 'package:fluikit/widgets.dart' show FluiInput, FluiInputState, FluiText;
import 'package:flutter/material.dart'
    show
        BoxDecoration,
        BuildContext,
        Center,
        Color,
        Column,
        Container,
        Expanded,
        GlobalKey,
        Icon,
        Icons,
        InkWell,
        Padding,
        Row,
        Scaffold,
        SizedBox,
        StatelessWidget,
        SystemMouseCursors,
        Widget;

import '/enums/user_preferences.dart' show UserPreferencesKeys;
import '/handlers/select_directory.dart' show selectDirectory;
import '/l10n/app_localizations.dart' show AppLocalizations;
import '/managers/user_preferences_manager/user_preferences_manager.dart'
    show UserPreferencesManager;

class HomeScreen extends StatelessWidget {
  final _inputUrlsKey = GlobalKey<FluiInputState>();
  final _inputDirectoryKey = GlobalKey<FluiInputState>();

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
                  InkWell(
                    onTap: () async {
                      final directory = await selectDirectory(context);

                      UserPreferencesManager.setPreference(
                        UserPreferencesKeys.downloadDirectory,
                        directory,
                      );

                      _inputDirectoryKey.currentState?.setText(directory);
                    },
                    enableFeedback: true,
                    mouseCursor: SystemMouseCursors.click,
                    borderRadius: .circular(15.0),
                    child: Container(
                      padding: const .symmetric(horizontal: 16, vertical: 12),
                      decoration: BoxDecoration(
                        color: const Color.fromRGBO(27, 27, 35, 0.7),
                        borderRadius: .circular(15.0),
                      ),
                      child: Row(
                        children: [
                          const Icon(Icons.folder_outlined, size: 24),
                          const SizedBox(width: 8),
                          FluiText(
                            text: AppLocalizations.of(
                              context,
                            )!.select_directory,
                          ),
                        ],
                      ),
                    ),
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}

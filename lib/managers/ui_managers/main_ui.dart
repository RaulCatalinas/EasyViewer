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
        BuildContext;

import '/components/widgets/icon_button.dart' show CreateIconButton;
import '/components/widgets/input.dart' show CreateInput;
import '/components/widgets/progress_bar.dart' show CreateProgressBar;
import '/enums/user_preferences.dart' show UserPreferencesKeys;
import '/handlers/select_directory.dart' show selectDirectory;
import '/managers/user_preferences_manager/user_preferences_manager.dart'
    show UserPreferencesManager;
import 'settings_ui.dart' show SettingsUI;

class MainUI extends StatelessWidget {
  const MainUI({super.key});

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
                  const CreateInput(
                    placeholder: 'Enter YouTube URLs here',
                    isMultiline: true,
                    autofocus: true,
                  ),
                  CreateInput(
                    placeholder: 'Directory where the download will be saved',
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
                  CreateIconButton(
                    onPressed: () async {
                      final directory = await selectDirectory();

                      UserPreferencesManager.setPreference(
                        UserPreferencesKeys.downloadDirectory,
                        directory,
                      );

                      print(
                        UserPreferencesManager.getPreference(
                          UserPreferencesKeys.downloadDirectory,
                        ),
                      );
                    },
                    icon: Icons.folder,
                    tooltip: 'Select Directory',
                  ),

                  const SizedBox(height: 17),

                  Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      CreateIconButton(
                        onPressed: () {
                          print('Download video button pressed');
                        },
                        icon: Icons.video_file,
                        tooltip: 'Download Video',
                      ),

                      CreateIconButton(
                        onPressed: () {
                          print('Download audio button pressed');
                        },
                        icon: Icons.audio_file,
                        tooltip: 'Download Audio',
                      ),
                    ],
                  ),
                  const SizedBox(height: 13),
                  const CreateProgressBar(),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}

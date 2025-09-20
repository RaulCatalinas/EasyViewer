import 'dart:io';

import 'package:flutter/material.dart';

import 'app_logging/logging_manager.dart' show LoggingManager;
import 'components/widgets/app_bar.dart' show CreateAppBar;
import 'components/widgets/checkbox.dart' show CreateCheckbox;
import 'components/widgets/icon_button.dart' show CreateIconButton;
import 'components/widgets/input.dart' show CreateInput;
import 'components/widgets/progress_bar.dart' show CreateProgressBar;
import 'components/widgets/text.dart' show CreateText;
import 'constants/version.dart' show version;
import 'enums/logging.dart' show LogLevels;
import 'handlers/close_window.dart' show handleCloseWindow;
import 'managers/window_manager.dart' show configureWindow;

void main() async {
  try {
    WidgetsFlutterBinding.ensureInitialized();

    LoggingManager.writeLog(
      LogLevels.info,
      'Starting EasyViewer ($version)...',
    );
    LoggingManager.writeLog(
      LogLevels.info,
      'Platform: ${Platform.operatingSystem}',
    );

    await configureWindow();

    LoggingManager.writeLog(LogLevels.info, 'Initializing UI...');

    runApp(const MyApp());
  } catch (e, stackTrace) {
    LoggingManager.writeLog(LogLevels.critical, 'Failed to start app: $e');
    LoggingManager.writeLog(LogLevels.critical, 'Stack trace: $stackTrace');

    rethrow;
  }
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    LoggingManager.writeLog(LogLevels.info, 'UI initialized successfully.');
    LoggingManager.writeLog(LogLevels.info, 'App started successfully.');

    return MaterialApp(title: 'EasyViewer', home: const MyHomePage());
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key});

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  @override
  void initState() {
    super.initState();
    handleCloseWindow(context);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: CreateAppBar(
        actions: [
          Row(
            children: [
              const CreateText(text: "Check for updates automatically"),
              CreateCheckbox(
                onChanged: (value) {
                  print("Checkbox changed: $value");
                },
                semanticLabel: "Check for updates automatically",
              ),
            ],
          ),
          CreateIconButton(
            onPressed: () {
              print("Change theme button pressed");
            },
            icon: Icons.sunny,
            tooltip: "Change Theme",
            iconSize: 28,
          ),
          CreateIconButton(
            onPressed: () {
              print("Change language button pressed");
            },
            icon: Icons.language,
            tooltip: "Change Language",
            iconSize: 28,
          ),
          CreateIconButton(
            onPressed: () {
              print("Contact button pressed");
            },
            icon: Icons.contacts,
            tooltip: "Contact",
            iconSize: 28,
          ),
          CreateIconButton(
            onPressed: () {
              print("Check updates button pressed");
            },
            icon: Icons.update,
            tooltip: "Check for Updates",
            iconSize: 28,
          ),
        ],
      ),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(25.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              Column(
                mainAxisAlignment: MainAxisAlignment.center,
                spacing: 15,
                children: const [
                  CreateInput(
                    placeholder: "Enter YouTube URLs here",
                    isMultiline: true,
                    autofocus: true,
                  ),
                  CreateInput(
                    placeholder: "Directory where the download will be saved",
                    readOnly: true,
                  ),
                ],
              ),

              const SizedBox(height: 20),

              Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  CreateIconButton(
                    onPressed: () {
                      print("Select directory button pressed");
                    },
                    icon: Icons.folder,
                    tooltip: "Select Directory",
                  ),

                  const SizedBox(height: 17),

                  Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      CreateIconButton(
                        onPressed: () {
                          print("Download video button pressed");
                        },
                        icon: Icons.video_file,
                        tooltip: "Download Video",
                      ),

                      CreateIconButton(
                        onPressed: () {
                          print("Download audio button pressed");
                        },
                        icon: Icons.audio_file,
                        tooltip: "Download Audio",
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

import 'dart:io' show Platform;

import 'package:flutter/material.dart'
    show
        BuildContext,
        MaterialApp,
        State,
        StatefulWidget,
        StatelessWidget,
        ValueListenableBuilder,
        Widget,
        WidgetsFlutterBinding,
        runApp;

import 'app_logging/logging_manager.dart' show LoggingManager;
import 'constants/version.dart' show version;
import 'enums/logging.dart' show LogLevels;
import 'handlers/close_window.dart' show handleCloseWindow;
import 'managers/ui_managers/main_ui.dart' show MainUI;
import 'managers/user_preferences_manager/theme_manager.dart' show ThemeManager;
import 'managers/window_manager/window_manager.dart' show configureWindow;

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

    runApp(MyApp());
  } catch (e, stackTrace) {
    LoggingManager.writeLog(LogLevels.critical, 'Failed to start app: $e');
    LoggingManager.writeLog(LogLevels.critical, 'Stack trace: $stackTrace');

    rethrow;
  }
}

class MyApp extends StatelessWidget {
  MyApp({super.key});

  final appValueNotifier = ThemeManager.instance;

  @override
  Widget build(BuildContext context) {
    LoggingManager.writeLog(LogLevels.info, 'UI initialized successfully.');
    LoggingManager.writeLog(LogLevels.info, 'App started successfully.');

    ThemeManager.toggleTheme(context);

    return ValueListenableBuilder(
      valueListenable: appValueNotifier.theme,
      builder: (_, value, _) {
        return MaterialApp(
          title: 'EasyViewer',
          home: const MyHomePage(),
          theme: value,
        );
      },
    );
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
    return const MainUI();
  }
}

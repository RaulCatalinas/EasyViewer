import 'dart:io' show Platform;

import 'package:flutter/material.dart'
    show
        BuildContext,
        Locale,
        MaterialApp,
        State,
        StatefulWidget,
        ValueListenableBuilder,
        Widget,
        WidgetsFlutterBinding,
        runApp;

import 'app_logging/logging_manager.dart' show LoggingManager;
import 'constants/version.dart' show version;
import 'enums/logging.dart' show LogLevels;
import 'handlers/close_window.dart' show handleCloseWindow;
import 'l10n/app_localizations.dart' show AppLocalizations;
import 'managers/ui_managers/main_ui.dart' show MainUI;
import 'managers/user_preferences_manager/language_manager.dart'
    show LanguageManager;
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

// CAMBIO PRINCIPAL: MyApp ahora es StatefulWidget en lugar de StatelessWidget
class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  final themeNotifier = ThemeManager.instance;
  late Locale _locale;

  @override
  void initState() {
    super.initState();
    _locale = LanguageManager.getInitialLocale();

    LanguageManager.setLanguageChangeCallback(_onLanguageChanged);
  }

  void _onLanguageChanged() {
    setState(() {
      _locale = LanguageManager.getCurrentLocale();
    });
  }

  @override
  Widget build(BuildContext context) {
    LoggingManager.writeLog(LogLevels.info, 'UI initialized successfully.');
    LoggingManager.writeLog(LogLevels.info, 'App started successfully.');

    return ValueListenableBuilder(
      valueListenable: themeNotifier.theme,
      builder: (_, value, _) {
        return MaterialApp(
          title: 'EasyViewer',
          home: const MyHomePage(),
          theme: value,
          localizationsDelegates: AppLocalizations.localizationsDelegates,
          supportedLocales: AppLocalizations.supportedLocales,
          locale: _locale, // Usar el locale del estado local
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
    return MainUI();
  }
}

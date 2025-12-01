// ignore_for_file: use_build_context_synchronously

import 'dart:io' show Platform;

import 'package:fluikit/dialogs.dart' show FluiInfoDialog;
import 'package:flutter/material.dart'
    show
        BuildContext,
        Locale,
        State,
        StatefulWidget,
        Widget,
        WidgetsBinding,
        WidgetsBindingObserver,
        WidgetsFlutterBinding,
        runApp;
import 'package:flutter_themed/flutter_themed.dart'
    show Themed, ThemeStorageAdapter;
import 'package:flutter_themed/themed_app.dart' show ThemedApp;
import 'package:logkeeper/logkeeper.dart' show LogKeeper;
import 'package:window_manager/window_manager.dart';

import 'constants/version.dart' show installedVersion;
import 'core/interact_api.dart' show InteractApi;
import 'enums/user_preferences.dart' show UserPreferencesKeys;
import 'handlers/close_window.dart' show handleCloseWindow;
import 'l10n/app_localizations.dart' show AppLocalizations;
import 'managers/ui_managers/main_ui.dart' show MainUI;
import 'managers/user_preferences_manager/language_manager.dart'
    show LanguageManager;
import 'managers/user_preferences_manager/user_preferences_manager.dart'
    show UserPreferencesManager;
import 'managers/window_manager/window_manager.dart' show configureWindow;
import 'update/update_manager.dart' show UpdateManager;

class ThemeStorage implements ThemeStorageAdapter {
  @override
  Future<String?> loadTheme() async {
    return UserPreferencesManager.getPreference(UserPreferencesKeys.theme);
  }

  @override
  Future<void> saveTheme(String themeName) async {
    UserPreferencesManager.setPreference(UserPreferencesKeys.theme, themeName);
  }
}

void main() async {
  try {
    WidgetsFlutterBinding.ensureInitialized();

    await Future.wait([
      InteractApi.initialize(),
      windowManager.ensureInitialized(),
      UserPreferencesManager.initialize(),
    ]);

    await Themed.initialize(storageAdapter: ThemeStorage());

    LogKeeper.info('🚀 Starting EasyViewer ($installedVersion)...');
    LogKeeper.info('Platform: ${Platform.operatingSystem}');

    await configureWindow();

    LogKeeper.info('📱 Launching UI...');

    runApp(const MyApp());
  } catch (e, stackTrace) {
    LogKeeper.critical('❌ Failed to start app: $e');
    LogKeeper.critical('Stack trace: $stackTrace');

    rethrow;
  }
}

class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> with WidgetsBindingObserver {
  late Locale _locale;

  @override
  void initState() {
    super.initState();

    _locale = LanguageManager.getInitialLocale();
    LanguageManager.setLanguageChangeCallback(_onLanguageChanged);

    LogKeeper.info('✅ UI ready - EasyViewer visible to user');
  }

  void _onLanguageChanged() {
    setState(() {
      _locale = LanguageManager.getCurrentLocale();
    });
  }

  @override
  Widget build(BuildContext context) {
    return ThemedApp(
      title: 'EasyViewer',
      home: const MyHomePage(),
      fontFamily: 'Inter',
      localizationsDelegates: AppLocalizations.localizationsDelegates,
      supportedLocales: AppLocalizations.supportedLocales,
      locale: _locale,
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key});

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  bool _hasInitialized = false;

  @override
  void initState() {
    super.initState();

    handleCloseWindow(context);
  }

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();

    if (!_hasInitialized) {
      _hasInitialized = true;

      WidgetsBinding.instance.addPostFrameCallback((_) async {
        await _initializeApp();
      });
    }
  }

  Future<void> _initializeApp() async {
    try {
      LogKeeper.info('⚙️ Initializing background tasks...');
      LogKeeper.info('🔄 Checking for updates...');

      await UpdateManager.checkForUpdatesIfNecessary(context);
      await UpdateManager.reminderUpdateIfNecessary(context);

      LogKeeper.info('✅ Update check completed');
      LogKeeper.info('Showing initial dialogs (if necessary)...');

      _showDialogsIfIsNecessary(context);

      LogKeeper.info('✅ Background tasks completed successfully');
      LogKeeper.info('⚡ EasyViewer is fully operational');
    } catch (e) {
      LogKeeper.error('❌ Background initialization failed: $e');
      LogKeeper.info('⚠️ Application running with limited functionality');
    }
  }

  @override
  Widget build(BuildContext context) {
    return MainUI();
  }

  void _showDialogsIfIsNecessary(BuildContext context) {
    final disclaimerShown = UserPreferencesManager.getPreference(
      UserPreferencesKeys.disclaimerShown,
    );

    final whatsNewShown = UserPreferencesManager.getPreference(
      UserPreferencesKeys.whatsNewShown,
    );

    if (!whatsNewShown) {
      FluiInfoDialog.show(
        context,
        title: AppLocalizations.of(context)!.whats_new_title,
        content: AppLocalizations.of(context)!.whats_new_body,
        onPressed: () {
          UserPreferencesManager.setPreference(
            UserPreferencesKeys.whatsNewShown,
            true,
          );
        },
      );
    }

    if (!disclaimerShown) {
      FluiInfoDialog.show(
        context,
        title: AppLocalizations.of(context)!.liability_notice_title,
        content: AppLocalizations.of(context)!.liability_notice_body,
        onPressed: () {
          UserPreferencesManager.setPreference(
            UserPreferencesKeys.disclaimerShown,
            true,
          );
        },
      );
    }
  }
}

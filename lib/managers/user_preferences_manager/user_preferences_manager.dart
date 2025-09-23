import 'dart:convert' show JsonDecoder, JsonEncoder;
import 'dart:io' show Directory, File, ProcessSignal, exit;

import 'package:path/path.dart' show join;

import '/app_logging/logging_manager.dart' show LoggingManager;
import '/constants/user_preferences.dart' deferred as user_prefs;
import '/enums/logging.dart' show LogLevels;
import '/enums/user_preferences.dart' show UserPreferencesKeys;

class UserPreferencesManager {
  static UserPreferencesManager? _instance;

  late Map<UserPreferencesKeys, dynamic> _preferences;

  static final _preferencesFile = File(
    join(
      Directory.current.path,
      'lib',
      'managers',
      'user_preferences_manager',
      'user_preferences.json',
    ),
  );

  static Future<UserPreferencesManager> getInstance() async {
    if (_instance == null) {
      _instance = UserPreferencesManager._internal();

      await _instance!._initialize();
    }
    return _instance!;
  }

  UserPreferencesManager._internal();

  Future<void> _initialize() async {
    _preferences = await _loadPreferences();

    ProcessSignal.sigint.watch().listen((_) async {
      await _flushPreferences();

      exit(0);
    });

    ProcessSignal.sigterm.watch().listen((_) async {
      await _flushPreferences();

      exit(0);
    });
  }

  Future<void> _setupFilePath() async {
    try {
      LoggingManager.writeLog(
        LogLevels.info,
        "🔄 Creating new user preferences file...",
      );

      await _preferencesFile.create();

      await user_prefs.loadLibrary();

      final defaultPrefsString = await _convertUserPreferencesKeysToString(
        user_prefs.defaultUserPreferences,
      );

      await _preferencesFile.writeAsString(
        JsonEncoder.withIndent("  ").convert(defaultPrefsString),
        flush: true,
      );
    } catch (e) {
      LoggingManager.writeLog(
        LogLevels.error,
        "Error creating user preferences file: ${e.toString()}",
      );
    }
  }

  Future<Map<UserPreferencesKeys, dynamic>> _loadPreferences() async {
    if (!await _preferencesFile.exists()) {
      await _setupFilePath();

      return user_prefs.defaultUserPreferences;
    }

    return JsonDecoder().convert(await _preferencesFile.readAsString());
  }

  Future<Map<String, dynamic>> _convertUserPreferencesKeysToString(
    Map<UserPreferencesKeys, dynamic> preferencesToConvert,
  ) async {
    final defaultStringPrefs = <String, dynamic>{};

    preferencesToConvert.forEach((key, value) {
      defaultStringPrefs[key.toString().split('.').last] = value;
    });

    return defaultStringPrefs;
  }

  dynamic getPreference(UserPreferencesKeys key) {
    return _instance?._preferences[key];
  }

  void setPreference(UserPreferencesKeys key, dynamic value) {
    _instance?._preferences[key] = value;

    print("New value of preference $key: ${_instance?._preferences[key]}");
  }

  Future<void> _flushPreferences() async {
    final prefsString = await _convertUserPreferencesKeysToString(_preferences);

    await _preferencesFile.writeAsString(
      JsonEncoder.withIndent('  ').convert(prefsString),
      flush: true,
    );
  }
}

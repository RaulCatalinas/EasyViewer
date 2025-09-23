import 'dart:convert' show JsonDecoder, JsonEncoder;
import 'dart:io' show Directory, File;

import 'package:path/path.dart' show join;

import '/app_logging/logging_manager.dart' show LoggingManager;
import '/constants/user_preferences.dart' show defaultUserPreferences;
import '/enums/logging.dart' show LogLevels;
import '/enums/user_preferences.dart' show UserPreferencesKeys;

class UserPreferencesManager {
  static final _instance = UserPreferencesManager._internal();

  late Map<UserPreferencesKeys, dynamic> _preferences;

  final _preferencesFile = File(
    join(
      Directory.current.path,
      'lib',
      'managers',
      'user_preferences_manager',
      'user_preferences.json',
    ),
  );

  factory UserPreferencesManager() {
    return _instance;
  }

  UserPreferencesManager._internal() {
    _initialize();
  }

  void _initialize() {
    _preferences = _loadPreferences();

    LoggingManager.writeLog(
      LogLevels.info,
      "✅ UserPreferencesManager initialized successfully",
    );
  }

  void _setupFilePath() {
    try {
      LoggingManager.writeLog(
        LogLevels.info,
        "🔄 Creating new user preferences file...",
      );

      _preferencesFile.createSync();

      final defaultPrefsString = _convertUserPreferencesKeysToString(
        defaultUserPreferences,
      );

      _preferencesFile.writeAsStringSync(
        JsonEncoder.withIndent("  ").convert(defaultPrefsString),
        flush: true,
      );

      LoggingManager.writeLog(
        LogLevels.info,
        "✅ User preferences file created successfully at: ${_preferencesFile.path}",
      );
    } catch (e) {
      LoggingManager.writeLog(
        LogLevels.error,
        "❌ Error creating user preferences file: ${e.toString()}",
      );
    }
  }

  Map<UserPreferencesKeys, dynamic> _loadPreferences() {
    if (!_preferencesFile.existsSync()) {
      LoggingManager.writeLog(
        LogLevels.info,
        "📝 User preferences file not found, creating with defaults",
      );

      _setupFilePath();

      return defaultUserPreferences;
    }

    try {
      LoggingManager.writeLog(
        LogLevels.info,
        "📖 Loading user preferences from: ${_preferencesFile.path}",
      );

      final userPrefs = _preferencesFile.readAsStringSync();

      if (userPrefs.trim().isEmpty) {
        LoggingManager.writeLog(
          LogLevels.warning,
          "⚠️ Preferences file is empty, recreating with defaults",
        );

        final userPrefsString = _convertUserPreferencesKeysToString(
          defaultUserPreferences,
        );

        _preferencesFile.writeAsStringSync(
          JsonEncoder.withIndent("  ").convert(userPrefsString),
          flush: true,
        );

        return defaultUserPreferences;
      }

      final Map<String, dynamic> jsonData = JsonDecoder().convert(userPrefs);
      final Map<UserPreferencesKeys, dynamic> preferences = {};

      defaultUserPreferences.forEach((enumKey, defaultValue) {
        final stringKey = enumKey.toString().split('.').last;
        preferences[enumKey] = jsonData[stringKey] ?? defaultValue;
      });

      LoggingManager.writeLog(
        LogLevels.info,
        "✅ User preferences loaded successfully (${preferences.length} preferences)",
      );

      return preferences;
    } catch (e) {
      LoggingManager.writeLog(
        LogLevels.error,
        "❌ Error loading preferences: ${e.toString()}, using defaults",
      );

      return defaultUserPreferences;
    }
  }

  Map<String, dynamic> _convertUserPreferencesKeysToString(
    Map<UserPreferencesKeys, dynamic> preferencesToConvert,
  ) {
    final defaultStringPrefs = <String, dynamic>{};

    preferencesToConvert.forEach((key, value) {
      defaultStringPrefs[key.toString().split('.').last] = value;
    });

    return defaultStringPrefs;
  }

  static dynamic getPreference(UserPreferencesKeys key) {
    return _instance._preferences[key];
  }

  static void setPreference(UserPreferencesKeys key, dynamic value) {
    final oldValue = _instance._preferences[key];

    _instance._preferences[key] = value;

    LoggingManager.writeLog(
      LogLevels.info,
      "🔧 Preference updated: ${key.toString().split('.').last} = $value (was: $oldValue)",
    );
  }

  static void savePreferences() {
    try {
      final userPrefsString = _instance._convertUserPreferencesKeysToString(
        _instance._preferences,
      );

      _instance._preferencesFile.writeAsStringSync(
        JsonEncoder.withIndent('  ').convert(userPrefsString),
        flush: true,
      );

      LoggingManager.writeLog(
        LogLevels.info,
        "💾 User preferences saved successfully to: ${_instance._preferencesFile.path}",
      );
    } catch (e) {
      LoggingManager.writeLog(
        LogLevels.error,
        "❌ Error saving preferences: ${e.toString()}",
      );
    }
  }
}

import 'package:logkeeper/logkeeper.dart' show LogKeeper;
import 'package:shared_preferences/shared_preferences.dart'
    show SharedPreferencesAsync;

import '/constants/user_preferences.dart' show defaultUserPreferences;
import '/enums/user_preferences.dart' show UserPreferencesKeys;

class UserPreferencesManager {
  static final _instance = UserPreferencesManager._internal();

  late Map<UserPreferencesKeys, dynamic> _preferences;
  SharedPreferencesAsync? _prefs;
  bool _isInitialized = false;

  factory UserPreferencesManager() {
    return _instance;
  }

  UserPreferencesManager._internal();

  static Future<void> initialize() async {
    if (_instance._isInitialized) {
      LogKeeper.warning('⚠️ UserPreferencesManager already initialized');

      return;
    }

    try {
      _instance._prefs = SharedPreferencesAsync();
      _instance._preferences = await _instance._loadPreferences();
      _instance._isInitialized = true;

      LogKeeper.info(
        '✅ UserPreferencesManager initialized successfully (${_instance._preferences.length} preferences)',
      );
    } catch (e) {
      LogKeeper.error(
        '❌ Error initializing UserPreferencesManager: ${e.toString()}',
      );

      _instance._preferences = Map.from(defaultUserPreferences);
    }
  }

  Future<Map<UserPreferencesKeys, dynamic>> _loadPreferences() async {
    final Map<UserPreferencesKeys, dynamic> preferences = {};

    try {
      LogKeeper.info('📖 Loading user preferences from SharedPreferencesAsync');

      for (final entry in defaultUserPreferences.entries) {
        final enumKey = entry.key;
        final defaultValue = entry.value;
        final stringKey = enumKey.value;

        dynamic value;

        if (defaultValue is bool) {
          value = await _prefs?.getBool(stringKey) ?? defaultValue;
        } else if (defaultValue is String) {
          value = await _prefs?.getString(stringKey) ?? defaultValue;
        }

        preferences[enumKey] = value;
      }

      LogKeeper.info('✅ User preferences loaded successfully');

      return preferences;
    } catch (e) {
      LogKeeper.error(
        '❌ Error loading user preferences: ${e.toString()}, using defaults',
      );

      return Map.from(defaultUserPreferences);
    }
  }

  static dynamic getPreference(UserPreferencesKeys key) {
    if (!_instance._isInitialized) {
      LogKeeper.error(
        '❌ Trying to get preference before initialization! Returning default.',
      );

      return defaultUserPreferences[key];
    }

    return _instance._preferences[key];
  }

  static void setPreference(UserPreferencesKeys key, dynamic value) {
    if (!_instance._isInitialized) {
      LogKeeper.error('❌ Trying to set preference before initialization!');

      return;
    }

    final oldValue = _instance._preferences[key];

    if (oldValue == value) {
      LogKeeper.info(
        '⚠️ Preference ${key.value} already set to $value, no change made',
      );

      return;
    }

    _instance._preferences[key] = value;

    LogKeeper.info(
      '🔧 Preference updated: ${key.value} = $value (was: $oldValue)',
    );
  }

  static Future<void> savePreferences() async {
    if (!_instance._isInitialized) {
      LogKeeper.error('❌ Cannot save preferences before initialization');

      return;
    }

    try {
      LogKeeper.info(
        '💾 Saving ${_instance._preferences.length} preferences to disk...',
      );

      int savedCount = 0;

      final startTime = DateTime.now();

      for (final entry in _instance._preferences.entries) {
        final key = entry.key;
        final value = entry.value;
        final stringKey = key.value;

        bool saved = false;

        if (value is bool) {
          await _instance._prefs?.setBool(stringKey, value);

          saved = true;
        } else if (value is String) {
          await _instance._prefs?.setString(stringKey, value);

          saved = true;
        }

        if (saved) savedCount++;
      }

      final duration = DateTime.now().difference(startTime);

      LogKeeper.info(
        '✅ Saved $savedCount preferences to disk in ${duration.inMilliseconds}ms',
      );
    } catch (e) {
      LogKeeper.error('❌ Error saving preferences: ${e.toString()}');
    }
  }
}

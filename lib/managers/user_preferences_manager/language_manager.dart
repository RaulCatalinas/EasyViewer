import 'package:flutter/material.dart';

import '/enums/user_preferences.dart' show UserPreferencesKeys;
import 'user_preferences_manager.dart' show UserPreferencesManager;

class LanguageManager {
  static final _instance = LanguageManager._internal();
  static VoidCallback? _onLanguageChanged;

  factory LanguageManager() {
    return _instance;
  }

  LanguageManager._internal();

  static Locale getInitialLocale() {
    return Locale(
      UserPreferencesManager.getPreference(UserPreferencesKeys.language),
    );
  }

  static void setLanguageChangeCallback(VoidCallback callback) {
    _onLanguageChanged = callback;
  }

  static void changeLanguage(String languageCode) {
    UserPreferencesManager.setPreference(
      UserPreferencesKeys.language,
      languageCode,
    );

    _onLanguageChanged?.call();
  }

  static Locale getCurrentLocale() {
    return Locale(
      UserPreferencesManager.getPreference(UserPreferencesKeys.language),
    );
  }
}

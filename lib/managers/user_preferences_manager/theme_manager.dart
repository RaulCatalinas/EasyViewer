import 'package:flutter/material.dart'
    show IconData, Icons, ThemeData, ValueNotifier;

import '/enums/user_preferences.dart' show UserPreferencesKeys;
import 'user_preferences_manager.dart' show UserPreferencesManager;

class ThemeManager {
  static final instance = ThemeManager._internal();

  late ValueNotifier<ThemeData> theme;
  late ValueNotifier<IconData> iconTheme;

  factory ThemeManager() {
    return instance;
  }

  ThemeManager._internal() {
    theme = ValueNotifier<ThemeData>(_getInitialTheme());
    iconTheme = ValueNotifier<IconData>(_getInitialIconTheme());
  }

  static ThemeData _getInitialTheme() {
    return _getCurrentTheme() == 'light' ? ThemeData.light() : ThemeData.dark();
  }

  static IconData _getInitialIconTheme() {
    return _getCurrentTheme() == 'light' ? Icons.dark_mode : Icons.light_mode;
  }

  static void toggleTheme() {
    final currentTheme = _getCurrentTheme();

    instance.theme.value = currentTheme == 'light'
        ? ThemeData.dark()
        : ThemeData.light();

    UserPreferencesManager.setPreference(
      UserPreferencesKeys.theme,
      currentTheme == 'light' ? 'dark' : 'light',
    );
  }

  static void toggleIconTheme() {
    instance.iconTheme.value = _getCurrentTheme() == 'light'
        ? Icons.dark_mode
        : Icons.light_mode;
  }

  static dynamic _getCurrentTheme() {
    return UserPreferencesManager.getPreference(UserPreferencesKeys.theme);
  }
}

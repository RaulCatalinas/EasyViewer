import 'package:flutter/material.dart'
    show BuildContext, IconData, Icons, Theme, ThemeData, ValueNotifier;

import '/enums/user_preferences.dart' show UserPreferencesKeys;
import 'user_preferences_manager.dart' show UserPreferencesManager;

class ThemeManager {
  static final instance = ThemeManager._internal();

  late ValueNotifier<ThemeData> theme;

  factory ThemeManager() {
    return instance;
  }

  ThemeManager._internal() {
    theme = ValueNotifier<ThemeData>(_getInitialTheme());
  }

  static ThemeData _getInitialTheme() {
    return UserPreferencesManager.getPreference(UserPreferencesKeys.theme) ==
            "light"
        ? ThemeData.light()
        : ThemeData.dark();
  }

  static IconData getInitialIconTheme() {
    return UserPreferencesManager.getPreference(UserPreferencesKeys.theme) ==
            "light"
        ? Icons.light_mode
        : Icons.dark_mode;
  }

  static void toggleTheme(BuildContext context) {
    final currentTheme = Theme.brightnessOf(context).name;

    instance.theme.value = currentTheme == "light"
        ? ThemeData.dark()
        : ThemeData.light();

    UserPreferencesManager.setPreference(
      UserPreferencesKeys.theme,
      currentTheme,
    );
  }
}

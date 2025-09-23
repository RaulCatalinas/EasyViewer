import '../enums/user_preferences.dart' show UserPreferencesKeys;

final Map<UserPreferencesKeys, dynamic> defaultUserPreferences = Map.from({
  UserPreferencesKeys.theme: "light",
  UserPreferencesKeys.automaticNotifications: true,
  UserPreferencesKeys.language: "English",
  UserPreferencesKeys.latestGithubVersion: "0.0.0",
  UserPreferencesKeys.disclaimerShown: false,
  UserPreferencesKeys.lastUpdateCheck: "1970-01-01",
  UserPreferencesKeys.downloadDirectory: "",
  UserPreferencesKeys.upgradeAvailable: false,
  UserPreferencesKeys.whatsNewShown: false,
});

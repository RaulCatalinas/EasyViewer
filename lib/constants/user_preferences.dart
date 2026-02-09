import '../enums/user_preferences.dart' show UserPreferencesKeys;

final Map<UserPreferencesKeys, dynamic> defaultUserPreferences = const {
  UserPreferencesKeys.theme: 'light',
  UserPreferencesKeys.automaticNotifications: true,
  UserPreferencesKeys.language: 'en',
  UserPreferencesKeys.latestGithubVersion: '0.0.0',
  UserPreferencesKeys.disclaimerShown: false,
  UserPreferencesKeys.lastUpdateCheck: '1970-01-01',
  UserPreferencesKeys.downloadDirectory: '',
  UserPreferencesKeys.upgradeAvailable: false,
  UserPreferencesKeys.whatsNewShown: false,
};

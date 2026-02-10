import '../enums/user_preferences.dart' show UserPreferencesKeys;

const Map<UserPreferencesKeys, dynamic> defaultUserPreferences = {
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

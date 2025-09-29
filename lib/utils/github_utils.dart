import 'dart:convert' show jsonDecode;

import 'package:http/http.dart' as http;

import '/app_logging/logging_manager.dart' show LoggingManager;
import '/constants/github.dart'
    show githubApiUrl, githubVersionTagKey, defaultMessage;
import '/enums/logging.dart' show LogLevels;
import '/enums/user_preferences.dart' show UserPreferencesKeys;
import '/managers/user_preferences_manager/user_preferences_manager.dart'
    show UserPreferencesManager;
import 'time_utils.dart' show hasOneMonthPassed;

Future<String> _getLatestGithubReleaseVersion() async {
  try {
    final response = await http
        .get(Uri.parse(githubApiUrl))
        .timeout(const Duration(seconds: 5));

    if (response.statusCode != 200) {
      LoggingManager.writeLog(LogLevels.error, 'Failed to load latest release');

      throw Exception('Failed to load latest release');
    }

    final data = jsonDecode(response.body) as Map<String, dynamic>;

    final latestVersion = data[githubVersionTagKey] ?? defaultMessage;

    return (latestVersion as String).replaceAll('v', '');
  } catch (e) {
    LoggingManager.writeLog(
      LogLevels.error,
      'Error fetching latest release: $e',
    );

    return 'Error fetching latest release: $e';
  }
}

Future<String> getGithubVersion() async {
  final lastUpdateCheck = UserPreferencesManager.getPreference(
    UserPreferencesKeys.lastUpdateCheck,
  );

  if (hasOneMonthPassed(lastUpdateCheck)) {
    final latestGithubReleaseVersion = await _getLatestGithubReleaseVersion();

    UserPreferencesManager.setPreference(
      UserPreferencesKeys.latestGithubVersion,
      latestGithubReleaseVersion,
    );

    return latestGithubReleaseVersion;
  }

  return UserPreferencesManager.getPreference(
    UserPreferencesKeys.latestGithubVersion,
  );
}

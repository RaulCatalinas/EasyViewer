import 'dart:convert' show jsonDecode;

import 'package:http/http.dart' as http;
import 'package:logkeeper/logkeeper.dart' show LogKeeper;

import '/constants/github.dart'
    show githubApiUrl, githubVersionTagKey, defaultMessage;
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
      LogKeeper.error('Failed to load latest release');

      throw Exception('Failed to load latest release');
    }

    final data = jsonDecode(response.body) as Map<String, dynamic>;

    final latestVersion = data[githubVersionTagKey] ?? defaultMessage;

    LogKeeper.info('Latest version successfully obtained from GitHub.');

    return (latestVersion as String).replaceAll('v', '');
  } catch (e) {
    LogKeeper.error('Error fetching latest release: $e');

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

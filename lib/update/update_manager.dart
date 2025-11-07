import 'package:fluikit/dialogs.dart' show FluiConfirmDialog, FluiInfoDialog;
import 'package:flutter/material.dart' show BuildContext;
import 'package:logkeeper/logkeeper.dart' show LogKeeper;
import 'package:pub_semver/pub_semver.dart' show Version;

import '/constants/version.dart' show installedVersion;
import '/enums/user_preferences.dart' show UserPreferencesKeys;
import '/l10n/app_localizations.dart' show AppLocalizations;
import '/managers/user_preferences_manager/user_preferences_manager.dart'
    show UserPreferencesManager;
import '/utils/github_utils.dart' show getGithubVersion;
import '/utils/time_utils.dart' show hasOneMonthPassed;

class UpdateManager {
  static Future<void> checkForUpdatesIfNecessary(BuildContext context) async {
    final lastCheckDateString = UserPreferencesManager.getPreference(
      UserPreferencesKeys.lastUpdateCheck,
    );

    if (hasOneMonthPassed(lastCheckDateString)) {
      await checkForUpdates(context: context, automaticCheckUpdates: true);
    }
  }

  static Future<bool> _anUpdateIsAvailable() async {
    try {
      final latestGithubVersion = await getGithubVersion();

      final installed = Version.parse(installedVersion);
      final latest = Version.parse(latestGithubVersion);

      return installed < latest;
    } catch (e) {
      LogKeeper.error('Error parsing version: $e');

      return false;
    }
  }

  static Future<void> checkForUpdates({
    required BuildContext context,
    bool automaticCheckUpdates = false,
  }) async {
    try {
      final anUpdateIsAvailable = await _anUpdateIsAvailable();

      final now = DateTime.now();
      final formattedDate =
          '${now.year}-${now.month.toString().padLeft(2, '0')}-${now.day.toString().padLeft(2, '0')}';

      UserPreferencesManager.setPreference(
        UserPreferencesKeys.lastUpdateCheck,
        formattedDate,
      );

      if (anUpdateIsAvailable) {
        UserPreferencesManager.setPreference(
          UserPreferencesKeys.disclaimerShown,
          false,
        );
        UserPreferencesManager.setPreference(
          UserPreferencesKeys.whatsNewShown,
          false,
        );
        UserPreferencesManager.setPreference(
          UserPreferencesKeys.upgradeAvailable,
          true,
        );
      }

      if (!anUpdateIsAvailable && automaticCheckUpdates) return;

      if (!context.mounted) {
        LogKeeper.info('Context not mounted, skipping notification');

        return;
      }

      _notifyUpdate(context: context, anUpdateIsAvailable: anUpdateIsAvailable);
    } catch (e) {
      LogKeeper.error('Error checking for updates: $e');
    }
  }

  static void _update() {
    print('Updating...');
  }

  static void _notifyUpdate({
    required BuildContext context,
    required bool anUpdateIsAvailable,
  }) {
    if (anUpdateIsAvailable) {
      FluiConfirmDialog.show(
        context,
        title: AppLocalizations.of(context)!.update_available_title,
        content: AppLocalizations.of(context)!.update_available_body,
        onPressed: _update,
      );

      return;
    }

    FluiInfoDialog.show(
      context,
      title: AppLocalizations.of(context)!.updated_version_title,
      content: AppLocalizations.of(context)!.updated_version_body,
    );
  }

  static Future<bool> _isTheLatestVersion() async {
    final latestGithubVersion = await getGithubVersion();

    final installed = Version.parse(installedVersion);
    final latest = Version.parse(latestGithubVersion);

    return installed >= latest;
  }

  static Future<void> reminderUpdateIfNecessary(BuildContext context) async {
    final hasUpdated = await _isTheLatestVersion();

    if (!hasUpdated && context.mounted) {
      _notifyUpdate(context: context, anUpdateIsAvailable: true);

      return;
    }

    UserPreferencesManager.setPreference(
      UserPreferencesKeys.upgradeAvailable,
      false,
    );
  }
}

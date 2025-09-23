enum UserPreferencesKeys {
  theme("theme"),
  automaticNotifications("automatic_notifications"),
  language("language"),
  latestGithubVersion("latest_github_version"),
  disclaimerShown("disclaimer_shown"),
  lastUpdateCheck("last_update_check"),
  downloadDirectory("download_directory"),
  upgradeAvailable("upgrade_available"),
  whatsNewShown("whats_new_shown");

  const UserPreferencesKeys(this.value);
  final String value;
}

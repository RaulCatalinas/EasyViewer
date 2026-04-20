import 'package:fluikit/widgets.dart' show FluiDropdown, FluiText, FluiSwitch;
import 'package:flutter/material.dart'
    show
        BuildContext,
        Column,
        DropdownMenuEntry,
        Padding,
        Row,
        SizedBox,
        StatelessWidget,
        Widget;
import 'package:flutter_themed/flutter_themed.dart' show Themed;

import '/components/section.dart' show Section;
import '/constants/version.dart' show installedVersion;
import '/enums/user_preferences.dart' show UserPreferencesKeys;
import '/l10n/app_localizations.dart' show AppLocalizations;
import '/managers/user_preferences_manager/user_preferences_manager.dart'
    show UserPreferencesManager;

class SettingsScreen extends StatelessWidget {
  const SettingsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Section(
          title: 'General',
          content: Column(
            mainAxisAlignment: .center,
            children: [
              Padding(
                padding: const .symmetric(horizontal: 16),
                child: Row(
                  mainAxisAlignment: .spaceBetween,
                  children: [
                    FluiText(
                      text: AppLocalizations.of(context)!.change_language,
                      fontSize: 16,
                    ),
                    Padding(
                      padding: const .only(top: 16),
                      child: FluiDropdown(
                        initialValue: UserPreferencesManager.getPreference(
                          UserPreferencesKeys.language,
                        ),
                        hintText: AppLocalizations.of(context)!.change_language,
                        dropdownMenuEntries: [
                          DropdownMenuEntry(
                            value: 'en',
                            label: AppLocalizations.of(
                              context,
                            )!.english_language,
                          ),
                          DropdownMenuEntry(
                            value: 'es',
                            label: AppLocalizations.of(
                              context,
                            )!.spanish_language,
                          ),
                        ],
                        onSelected: (value) {
                          UserPreferencesManager.setPreference(
                            UserPreferencesKeys.language,
                            value,
                          );
                        },
                      ),
                    ),
                  ],
                ),
              ),

              const SizedBox(height: 16),

              Padding(
                padding: const .symmetric(horizontal: 16),
                child: Row(
                  mainAxisAlignment: .spaceBetween,
                  children: [
                    FluiText(
                      text: AppLocalizations.of(context)!.check_updates,
                      fontSize: 16,
                    ),
                    Padding(
                      padding: const .only(bottom: 16),
                      child: FluiSwitch(
                        activatedColor: const .fromRGBO(232, 69, 60, 1.0),
                        onChanged: (activated) {
                          UserPreferencesManager.setPreference(
                            UserPreferencesKeys.automaticNotifications,
                            activated,
                          );
                        },
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),

        Section(
          title: 'Appearance',
          content: Column(
            mainAxisAlignment: .center,
            children: [
              Padding(
                padding: const .symmetric(horizontal: 16),
                child: Row(
                  mainAxisAlignment: .spaceBetween,
                  children: [
                    FluiText(
                      text: AppLocalizations.of(context)!.use_dark_mode,
                      fontSize: 16,
                    ),
                    FluiSwitch(
                      defaultValue:
                          UserPreferencesManager.getPreference(
                            UserPreferencesKeys.theme,
                          ) ==
                          'dark',
                      onChanged: (darkMode) {
                        Themed.toggleTheme();

                        UserPreferencesManager.setPreference(
                          UserPreferencesKeys.theme,
                          darkMode ? 'dark' : 'light',
                        );
                      },
                      activatedColor: const .fromRGBO(232, 69, 60, 1.0),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),

        Section(
          title: 'About',
          content: Column(
            mainAxisAlignment: .center,
            children: [
              const Padding(
                padding: .symmetric(horizontal: 16),
                child: Row(
                  mainAxisAlignment: .spaceBetween,
                  children: [
                    FluiText(text: 'Version', fontSize: 16),
                    FluiText(
                      text: 'EasyViewer v$installedVersion',
                      fontSize: 14,
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ],
    );
  }
}

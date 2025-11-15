import 'package:fluikit/widgets.dart'
    show
        FluiCheckbox,
        FluiDropdown,
        FluiDropdownState,
        FluiIconButton,
        FluiStatefulIconButton,
        FluiStatefulIconButtonState,
        FluiText,
        FluiDrawer;
import 'package:flutter/material.dart'
    show
        BuildContext,
        ButtonStyle,
        DropdownMenuEntry,
        GlobalKey,
        Icons,
        StatelessWidget,
        ValueListenableBuilder,
        Widget,
        SizedBox;
import 'package:flutter/widgets.dart';

import '/constants/social_media.dart' show socialMedia;
import '/enums/social_media.dart' show SocialMedia;
import '/enums/user_preferences.dart' show UserPreferencesKeys;
import '/handlers/social_media.dart' show openUrl;
import '/l10n/app_localizations.dart' show AppLocalizations;
import '/managers/user_preferences_manager/language_manager.dart'
    show LanguageManager;
import '/update/update_manager.dart' show UpdateManager;
import '../user_preferences_manager/user_preferences_manager.dart'
    show UserPreferencesManager;

import 'package:flutter_themed/flutter_themed.dart' show Themed;

class SettingsUI extends StatelessWidget {
  static final _checkUpdateButtonKey = GlobalKey<FluiStatefulIconButtonState>();
  static final _dropdownContactKey = GlobalKey<FluiDropdownState>();
  static final _dropdownChangeLanguageKey = GlobalKey<FluiDropdownState>();

  const SettingsUI({super.key});

  @override
  Widget build(BuildContext context) {
    return ValueListenableBuilder(
      valueListenable: Themed.instance.themeNotifier,
      builder: (_, _, _) {
        return FluiDrawer(
          height: 320,
          width: LanguageManager.getCurrentLocale() == const Locale('en')
              ? 250
              : 280,
          children: [
            const SizedBox(height: 5),
            FluiText(
              text: AppLocalizations.of(context)!.settings_menu_title,
              fontSize: 22,
            ),
            const SizedBox(height: 20),
            Column(
              children: [
                FluiText(text: AppLocalizations.of(context)!.check_updates),
                FluiCheckbox(
                  initialValue: UserPreferencesManager.getPreference(
                    UserPreferencesKeys.automaticNotifications,
                  ),
                  onChanged: (value) {
                    _checkUpdateButtonKey.currentState?.toggleVisibility();
                    UserPreferencesManager.setPreference(
                      UserPreferencesKeys.automaticNotifications,
                      value,
                    );
                  },
                  semanticLabel: AppLocalizations.of(context)!.check_updates,
                ),
              ],
            ),
            const SizedBox(height: 5),
            FluiIconButton(
              onPressed: () {
                Themed.toggleTheme();
              },
              icon: Themed.currentThemeName == 'dark'
                  ? Icons.light_mode
                  : Icons.dark_mode,
              tooltip: 'Change Theme',
              iconSize: 28,
            ),
            const SizedBox(height: 5),
            Column(
              children: [
                FluiIconButton(
                  onPressed: () {
                    _dropdownContactKey.currentState?.closeIfOpen();
                    _dropdownChangeLanguageKey.currentState?.toggleVisibility();
                  },
                  icon: Icons.language,
                  tooltip: AppLocalizations.of(context)!.change_language,
                  iconSize: 28,
                ),
                FluiDropdown(
                  key: _dropdownChangeLanguageKey,
                  initiallyVisible: false,
                  placeHolder: AppLocalizations.of(context)!.change_language,
                  dropdownMenuEntries: [
                    DropdownMenuEntry(
                      value: 'en',
                      label: AppLocalizations.of(context)!.english_language,
                      style: ButtonStyle(enableFeedback: true),
                    ),
                    DropdownMenuEntry(
                      value: 'es',
                      label: AppLocalizations.of(context)!.spanish_language,
                      style: ButtonStyle(enableFeedback: true),
                    ),
                  ],
                  onSelected: (value) {
                    LanguageManager.changeLanguage(value.toString());
                    _dropdownChangeLanguageKey.currentState?.closeIfOpen();
                  },
                ),
              ],
            ),
            const SizedBox(height: 5),
            Column(
              children: [
                FluiIconButton(
                  onPressed: () {
                    _dropdownChangeLanguageKey.currentState?.closeIfOpen();
                    _dropdownContactKey.currentState?.toggleVisibility();
                  },
                  icon: Icons.contacts,
                  tooltip: AppLocalizations.of(context)!.contact,
                  iconSize: 28,
                ),
                FluiDropdown(
                  key: _dropdownContactKey,
                  initiallyVisible: false,
                  placeHolder: AppLocalizations.of(context)!.social_media,
                  dropdownMenuEntries: [
                    DropdownMenuEntry(
                      value: SocialMedia.instagram,
                      label: 'Instagram',
                      style: ButtonStyle(enableFeedback: true),
                    ),
                    DropdownMenuEntry(
                      value: SocialMedia.twitter,
                      label: 'Twitter/X',
                      style: ButtonStyle(enableFeedback: true),
                    ),
                    DropdownMenuEntry(
                      value: SocialMedia.github,
                      label: 'GitHub',
                      style: ButtonStyle(enableFeedback: true),
                    ),
                  ],
                  onSelected: (value) async {
                    await openUrl(socialMedia[value].toString());
                    _dropdownContactKey.currentState?.closeIfOpen();
                  },
                ),
              ],
            ),
            const SizedBox(height: 5),
            FluiStatefulIconButton(
              key: _checkUpdateButtonKey,
              initiallyVisible: !UserPreferencesManager.getPreference(
                UserPreferencesKeys.automaticNotifications,
              ),
              onPressed: () async {
                await UpdateManager.checkForUpdates(context: context);
              },
              icon: Icons.update,
              tooltip: AppLocalizations.of(context)!.check_updates,
              iconSize: 28,
            ),
          ],
        );
      },
    );
  }
}

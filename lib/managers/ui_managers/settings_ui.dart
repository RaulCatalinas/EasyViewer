import 'package:fluikit/widgets.dart'
    show
        FluiAppBar,
        FluiCheckbox,
        FluiDropdown,
        FluiDropdownState,
        FluiIconButton,
        FluiStatefulIconButton,
        FluiStatefulIconButtonState,
        FluiText;
import 'package:flutter/material.dart'
    show
        BuildContext,
        ButtonStyle,
        DropdownMenuEntry,
        GlobalKey,
        Icons,
        PreferredSizeWidget,
        Row,
        Size,
        StatelessWidget,
        ValueListenableBuilder,
        Widget,
        kToolbarHeight;

import '/constants/social_media.dart' show socialMedia;
import '/enums/social_media.dart' show SocialMedia;
import '/enums/user_preferences.dart' show UserPreferencesKeys;
import '/handlers/social_media.dart' show openUrl;
import '/l10n/app_localizations.dart' show AppLocalizations;
import '/managers/user_preferences_manager/language_manager.dart'
    show LanguageManager;
import '/managers/user_preferences_manager/theme_manager.dart'
    show ThemeManager;
import '/update/update_manager.dart' show UpdateManager;
import '../user_preferences_manager/user_preferences_manager.dart'
    show UserPreferencesManager;

class SettingsUI extends StatelessWidget implements PreferredSizeWidget {
  static final _checkUpdateButtonKey = GlobalKey<FluiStatefulIconButtonState>();
  static final _dropdownContactKey = GlobalKey<FluiDropdownState>();
  static final _dropdownChangeLanguageKey = GlobalKey<FluiDropdownState>();

  final appValueNotifier = ThemeManager.instance;

  SettingsUI({super.key});

  @override
  Widget build(BuildContext context) {
    return ValueListenableBuilder(
      valueListenable: appValueNotifier.iconTheme,
      builder: (_, value, _) {
        return FluiAppBar(
          actions: [
            Row(
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
            FluiIconButton(
              onPressed: () {
                ThemeManager.toggleTheme();
                ThemeManager.toggleIconTheme();
              },
              icon: value,
              tooltip: 'Change Theme',
              iconSize: 28,
            ),
            FluiIconButton(
              onPressed: () {
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
              },
            ),
            FluiIconButton(
              onPressed: () {
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
              },
            ),
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

  @override
  Size get preferredSize => const Size.fromHeight(kToolbarHeight);
}

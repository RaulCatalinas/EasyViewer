import 'package:easyviewer/constants/social_media.dart';
import 'package:easyviewer/handlers/social_media.dart';
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

import '/components/widgets/app_bar.dart' show CreateAppBar;
import '/components/widgets/checkbox.dart' show CreateCheckbox;
import '/components/widgets/dropdown.dart'
    show CreateDropdown, CreateDropdownState;
import '/components/widgets/icon_button.dart' show CreateIconButton;
import '/components/widgets/stateful_icon_button.dart'
    show CreateStatefulIconButton, CreateStatefulIconButtonState;
import '/components/widgets/text.dart' show CreateText;
import '/enums/social_media.dart' show SocialMedia;
import '/enums/user_preferences.dart' show UserPreferencesKeys;
import '/managers/user_preferences_manager/theme_manager.dart'
    show ThemeManager;
import '../user_preferences_manager/user_preferences_manager.dart'
    show UserPreferencesManager;

class SettingsUI extends StatelessWidget implements PreferredSizeWidget {
  static final _checkUpdateButtonKey =
      GlobalKey<CreateStatefulIconButtonState>();
  static final _dropdownsKey = GlobalKey<CreateDropdownState>();

  final appValueNotifier = ThemeManager.instance;

  SettingsUI({super.key});

  @override
  Widget build(BuildContext context) {
    return ValueListenableBuilder(
      valueListenable: appValueNotifier.iconTheme,
      builder: (_, value, _) {
        return CreateAppBar(
          actions: [
            Row(
              children: [
                const CreateText(text: 'Check for updates automatically'),
                CreateCheckbox(
                  initialValue: UserPreferencesManager.getPreference(
                    UserPreferencesKeys.automaticNotifications,
                  ),
                  onChanged: (value) {
                    _checkUpdateButtonKey.currentState?.setVisible(!value!);
                    UserPreferencesManager.setPreference(
                      UserPreferencesKeys.automaticNotifications,
                      value,
                    );
                  },
                  semanticLabel: 'Check for updates automatically',
                ),
              ],
            ),
            CreateIconButton(
              onPressed: () {
                ThemeManager.toggleTheme();
                ThemeManager.toggleIconTheme();
              },
              icon: value,
              tooltip: 'Change Theme',
              iconSize: 28,
            ),
            CreateIconButton(
              onPressed: () {
                print('Change language button pressed');
              },
              icon: Icons.language,
              tooltip: 'Change Language',
              iconSize: 28,
            ),
            CreateIconButton(
              onPressed: () {
                _dropdownsKey.currentState?.setVisible(
                  !_dropdownsKey.currentState!.isVisible,
                );
              },
              icon: Icons.contacts,
              tooltip: 'Contact',
              iconSize: 28,
            ),
            CreateDropdown(
              key: _dropdownsKey,
              initiallyVisible: false,
              placeHolder: 'Social media',
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
            CreateStatefulIconButton(
              key: _checkUpdateButtonKey,
              initiallyVisible: !UserPreferencesManager.getPreference(
                UserPreferencesKeys.automaticNotifications,
              ),
              onPressed: () {
                print('Check updates button pressed');
              },
              icon: Icons.update,
              tooltip: 'Check for Updates',
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

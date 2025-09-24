import 'package:flutter/material.dart'
    show
        Icons,
        Row,
        StatelessWidget,
        Widget,
        BuildContext,
        Size,
        kToolbarHeight,
        PreferredSizeWidget,
        GlobalKey;

import '/components/widgets/app_bar.dart' show CreateAppBar;
import '/components/widgets/checkbox.dart' show CreateCheckbox;
import '/components/widgets/icon_button.dart' show CreateIconButton;
import '/components/widgets/stateful_icon_button.dart'
    show CreateStatefulIconButton, CreateStatefulIconButtonState;
import '/components/widgets/text.dart' show CreateText;
import '/enums/user_preferences.dart' show UserPreferencesKeys;
import '/managers/user_preferences_manager/theme_manager.dart'
    show ThemeManager;
import '../user_preferences_manager/user_preferences_manager.dart'
    show UserPreferencesManager;

class SettingsUI extends StatelessWidget implements PreferredSizeWidget {
  static final GlobalKey<CreateStatefulIconButtonState> _checkUpdateButtonKey =
      GlobalKey<CreateStatefulIconButtonState>();

  const SettingsUI({super.key});

  @override
  Widget build(BuildContext context) {
    return CreateAppBar(
      actions: [
        Row(
          children: [
            const CreateText(text: "Check for updates automatically"),
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
              semanticLabel: "Check for updates automatically",
            ),
          ],
        ),
        CreateIconButton(
          onPressed: () {
            ThemeManager.toggleTheme(context);
          },
          icon: ThemeManager.getInitialIconTheme(),
          tooltip: "Change Theme",
          iconSize: 28,
        ),
        CreateIconButton(
          onPressed: () {
            print("Change language button pressed");
          },
          icon: Icons.language,
          tooltip: "Change Language",
          iconSize: 28,
        ),
        CreateIconButton(
          onPressed: () {
            print("Contact button pressed");
          },
          icon: Icons.contacts,
          tooltip: "Contact",
          iconSize: 28,
        ),

        CreateStatefulIconButton(
          key: _checkUpdateButtonKey,
          initiallyVisible: !UserPreferencesManager.getPreference(
            UserPreferencesKeys.automaticNotifications,
          ),
          onPressed: () {
            print("Check updates button pressed");
          },
          icon: Icons.update,
          tooltip: "Check for Updates",
          iconSize: 28,
        ),
      ],
    );
  }

  @override
  Size get preferredSize => const Size.fromHeight(kToolbarHeight);
}

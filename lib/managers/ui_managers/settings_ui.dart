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
              onChanged: (value) {
                _checkUpdateButtonKey.currentState?.setVisible(!value!);
              },
              semanticLabel: "Check for updates automatically",
            ),
          ],
        ),
        CreateIconButton(
          onPressed: () {
            print("Change theme button pressed");
          },
          icon: Icons.sunny,
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
          initiallyVisible: false,
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

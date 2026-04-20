import 'package:flutter/material.dart'
    show BuildContext, Dialog, SizedBox, showDialog;

import '/screens/settings_screen.dart' show SettingsScreen;

void showSettingsModal({required BuildContext context}) {
  showDialog(
    context: context,
    builder: (_) => const Dialog(
      child: SizedBox(width: 700, height: 510, child: SettingsScreen()),
    ),
  );
}

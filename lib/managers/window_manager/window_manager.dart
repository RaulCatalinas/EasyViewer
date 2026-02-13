import 'dart:ui' show Size;

import 'package:logkeeper/logkeeper.dart' show LogKeeper;
import 'package:window_manager/window_manager.dart';

import '/app_settings/app_settings.dart' show WindowSettings;

Future<void> configureWindow() async {
  LogKeeper.info('Configuring window...');

  const windowOptions = WindowOptions(
    size: Size(WindowSettings.width, WindowSettings.height),
    center: WindowSettings.centered,
    title: WindowSettings.title,
  );

  await windowManager.waitUntilReadyToShow(windowOptions, () async {
    await windowManager.setPreventClose(true);
    await windowManager.setResizable(WindowSettings.resizable);
    await windowManager.setMaximizable(WindowSettings.maximizable);
    await windowManager.show();
  });

  LogKeeper.info('Window configured successfully.');
}

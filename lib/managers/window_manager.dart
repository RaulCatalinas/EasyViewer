import 'dart:ui' show Size;

import 'package:window_manager/window_manager.dart';

import '../app_settings/app_settings.dart';

Future<void> configureWindow() async {
  windowManager.ensureInitialized();
  WindowOptions windowOptions = const WindowOptions(
    size: Size(WindowSettings.width, WindowSettings.height),
    center: WindowSettings.centered,
    title: WindowSettings.title,
  );

  windowManager.waitUntilReadyToShow(windowOptions, () async {
    await windowManager.setResizable(WindowSettings.resizable);
    await windowManager.setMaximizable(WindowSettings.maximizable);
    await windowManager.show();
  });
}

import 'dart:ui' show Size;

import 'package:window_manager/window_manager.dart';

import '../../app_logging/logging_manager.dart' show LoggingManager;
import '../../app_settings/app_settings.dart' show WindowSettings;
import '../../enums/logging.dart' show LogLevels;

Future<void> configureWindow() async {
  LoggingManager.writeLog(LogLevels.info, 'Configuring window...');

  await windowManager.ensureInitialized();

  var windowOptions = const WindowOptions(
    size: Size(WindowSettings.width, WindowSettings.height),
    center: WindowSettings.centered,
    title: WindowSettings.title,
  );

  await windowManager.waitUntilReadyToShow(windowOptions, () async {
    await windowManager.setResizable(WindowSettings.resizable);
    await windowManager.setMaximizable(WindowSettings.maximizable);
    await windowManager.show();
  });

  LoggingManager.writeLog(LogLevels.info, 'Window configured successfully.');
}

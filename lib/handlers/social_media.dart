import 'package:url_launcher/url_launcher.dart' show launchUrl;

import '/app_logging/logging_manager.dart' show LoggingManager;
import '/enums/logging.dart' show LogLevels;

Future<void> openUrl(String url) async {
  if (!await launchUrl(Uri.parse(url))) {
    LoggingManager.writeLog(
      LogLevels.error,
      'The URL could not be opened: $url',
    );

    return;
  }

  LoggingManager.writeLog(LogLevels.info, 'URL $url opened correctly');
}

import 'package:logkeeper/logkeeper.dart' show LogKeeper;
import 'package:url_launcher/url_launcher.dart' show launchUrl;

Future<void> openUrl(String url) async {
  if (!await launchUrl(Uri.parse(url))) {
    LogKeeper.error("The URL couldn't be opened: $url");

    return;
  }

  LogKeeper.info('URL $url opened correctly');
}

Future<void> openEmail(String email) async {
  final opened = await launchUrl(Uri(scheme: 'mailto', path: email));

  if (!opened) {
    LogKeeper.error('Error opening email $email');

    return;
  }

  LogKeeper.info('Email $email opened correctly');
}

import 'dart:io';

import 'package:path/path.dart' show join;
import 'package:path_provider/path_provider.dart'
    show getApplicationDocumentsDirectory;

Future<String> getUserDesktopPath() async {
  final documentsDir = await getApplicationDocumentsDirectory();

  return join(documentsDir.parent.path, 'Desktop');
}

bool existsDirectory(String directoryToCheck) {
  return Directory(directoryToCheck).existsSync();
}

import 'dart:io' show Process, Platform;

void openDirectory(String directory) {
  final Map<String, void Function()> openDirectoryFunctionMap = {
    'windows': () => Process.run('explorer', [directory]),
    'darwin': () => Process.run('open', [directory]),
    'linux': () => Process.run('xdg-open', [directory]),
  };

  final systemName = Platform.operatingSystem;

  if (openDirectoryFunctionMap.containsKey(systemName)) {
    openDirectoryFunctionMap[systemName]!();
    return;
  }

  throw UnsupportedError('Unsupported operating system');
}

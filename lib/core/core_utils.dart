import 'dart:io' show Platform;

import 'package:system_info3/system_info3.dart'
    show SysInfo, ProcessorArchitecture;
import 'package:youtube_explode_dart/solvers.dart' show DenoEJSSolver;
import 'package:youtube_explode_dart/youtube_explode_dart.dart'
    show YoutubeExplode;

YoutubeExplode? _youtubeExplodeInstance;

const Map<String, String> denoExecutables = {
  'windows': 'assets/executables/deno-windows-x64.exe',
  'macos-arm64': 'assets/executables/deno-macos-aarch64',
  'macos-x86_64': 'assets/executables/deno-macos-x64',
  'linux': 'assets/executables/deno-linux-x64',
};

Future<YoutubeExplode> getYoutubeExplodeInstance() async {
  if (_youtubeExplodeInstance != null) return _youtubeExplodeInstance!;

  final userOS = Platform.operatingSystem;

  if (!denoExecutables.containsKey(userOS)) throw Exception('Unsupported OS');

  final denoPath = switch ((Platform.isMacOS, SysInfo.kernelArchitecture)) {
    (true, ProcessorArchitecture.arm64) => denoExecutables['macos-arm64']!,
    (true, ProcessorArchitecture.x86_64) => denoExecutables['macos-x86_64']!,
    (true, _) => throw Exception('Unsupported architecture'),
    (false, _) => denoExecutables[Platform.operatingSystem]!,
  };

  final solver = await DenoEJSSolver.init(denoExe: denoPath);

  _youtubeExplodeInstance = YoutubeExplode(jsSolver: solver);

  return _youtubeExplodeInstance!;
}

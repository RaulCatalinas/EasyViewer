import 'dart:io' show Platform;

import 'package:system_info3/system_info3.dart'
    show SysInfo, ProcessorArchitecture;
import 'package:youtube_explode_dart/solvers.dart' show DenoEJSSolver;
import 'package:youtube_explode_dart/youtube_explode_dart.dart'
    show YoutubeExplode;

YoutubeExplode? _youtubeExplodeInstance;

const Map<String, String> denoExecutables = {
  'windows': 'assets/deno-windows-x64.exe',
  'macos-arm64': 'assets/deno-macos-aarch64',
  'macos-x86_64': 'assets/deno-macos-x64',
  'linux': 'assets/deno-linux-x64',
};

Future<YoutubeExplode> getYoutubeExplodeInstance() async {
  if (_youtubeExplodeInstance != null) return _youtubeExplodeInstance!;

  final denoPath = switch ((
    Platform.operatingSystem,
    SysInfo.kernelArchitecture,
  )) {
    ('macos', ProcessorArchitecture.arm64) => denoExecutables['macos-arm64'],
    ('macos', ProcessorArchitecture.x86_64) => denoExecutables['macos-x86_64'],
    ('windows', _) => denoExecutables['windows'],
    ('linux', _) => denoExecutables['linux'],
    (var os, _) => throw Exception('Unsupported OS: $os'),
  };

  final solver = await DenoEJSSolver.init(denoExe: denoPath);

  _youtubeExplodeInstance = YoutubeExplode(jsSolver: solver);

  return _youtubeExplodeInstance!;
}

import 'dart:io';

import 'package:flutter/services.dart';
import 'package:path/path.dart' as p;
import 'package:path_provider/path_provider.dart';
import 'package:system_info3/system_info3.dart';
import 'package:youtube_explode_dart/solvers.dart';
import 'package:youtube_explode_dart/youtube_explode_dart.dart';

import '/constants/paths.dart' show denoExecutables;

YoutubeExplode? _youtubeExplodeInstance;

Future<String> _prepareDeno(String assetPath) async {
  final filename = assetPath.split('/').last;
  final dir = await getApplicationSupportDirectory();
  final destPath = p.join(dir.path, filename);

  final file = File(destPath);

  if (!await file.exists()) {
    final data = await rootBundle.load(assetPath);
    await file.writeAsBytes(data.buffer.asUint8List(), flush: true);

    await Process.run('chmod', ['u+x', destPath]);
  }

  return destPath;
}

Future<YoutubeExplode> getYoutubeExplodeInstance() async {
  if (_youtubeExplodeInstance != null) return _youtubeExplodeInstance!;

  final denoAssetPath = switch ((
    Platform.operatingSystem,
    SysInfo.kernelArchitecture,
  )) {
    ('macos', ProcessorArchitecture.arm64) => denoExecutables['macos-arm64']!,
    ('macos', ProcessorArchitecture.x86_64) => denoExecutables['macos-x86_64']!,
    ('windows', _) => denoExecutables['windows']!,
    ('linux', _) => denoExecutables['linux']!,
    (var os, _) => throw Exception('Unsupported OS: $os'),
  };

  final denoPath = Platform.isWindows
      ? denoAssetPath
      : await _prepareDeno(denoAssetPath);

  final solver = await DenoEJSSolver.init(denoExe: denoPath);

  _youtubeExplodeInstance = YoutubeExplode(jsSolver: solver);
  return _youtubeExplodeInstance!;
}

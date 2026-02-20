import 'dart:io';

import 'package:flutter/services.dart' show rootBundle;
import 'package:path/path.dart' as p;
import 'package:path_provider/path_provider.dart'
    show getApplicationSupportDirectory;
import 'package:system_info3/system_info3.dart'
    show SysInfo, ProcessorArchitecture;
import 'package:youtube_explode_dart/js_challenge.dart' show BaseEJSSolver;
import 'package:youtube_explode_dart/solvers.dart' show DenoEJSSolver;

import '/constants/paths.dart' show denoExecutables;

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

Future<BaseEJSSolver> getDenoSolver() async {
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

  return await DenoEJSSolver.init(denoExe: denoPath);
}

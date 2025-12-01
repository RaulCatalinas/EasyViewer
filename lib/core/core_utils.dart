import 'dart:io' show Platform;

import 'package:youtube_explode_dart/solvers.dart' show DenoEJSSolver;
import 'package:youtube_explode_dart/youtube_explode_dart.dart'
    show YoutubeExplode;

YoutubeExplode? _youtubeExplodeInstance;

Future<YoutubeExplode> getYoutubeExplodeInstance() async {
  if (_youtubeExplodeInstance != null) return _youtubeExplodeInstance!;

  final solver = await DenoEJSSolver.init(
    denoExe: 'assets/deno${Platform.isWindows ? ".exe" : ""}',
  );

  _youtubeExplodeInstance = YoutubeExplode(jsSolver: solver);

  return _youtubeExplodeInstance!;
}

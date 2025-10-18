import 'dart:io' show File;

import 'package:ffmpeg_kit_flutter_minimal/ffmpeg_kit.dart' show FFmpegKit;
import 'package:logkeeper/logkeeper.dart' show LogKeeper;

import '/utils/file_utils.dart' show deleteFile;

Future<void> mergeAudioAndVideo({
  required File audioFile,
  required File videoFile,
  required String outputPath,
}) async {
  try {
    await FFmpegKit.executeAsync(
      '-i "${videoFile.path}" -i "${audioFile.path}" -c:v copy -c:a aac -b:a 320k "$outputPath"',
      (session) async {
        final returnCode = await session.getReturnCode();

        if (returnCode!.isValueSuccess()) {
          LogKeeper.info(
            'FFmpeg process completed successfully and the video has been downloaded',
          );

          await deleteFile(fileToDelete: audioFile);
        } else {
          LogKeeper.error(
            'Error! FFmpeg process failed with code: ${returnCode.getValue()}',
          );

          await deleteFile(fileToDelete: audioFile);
          await deleteFile(fileToDelete: videoFile);
        }
      },
      (log) {
        LogKeeper.info('FFmpeg log: ${log.getMessage()}');
      },
    );
  } catch (e) {
    LogKeeper.error('Error merging audio and video streams: ${e.toString()}');

    await deleteFile(fileToDelete: audioFile);
    await deleteFile(fileToDelete: videoFile);

    rethrow;
  }
}

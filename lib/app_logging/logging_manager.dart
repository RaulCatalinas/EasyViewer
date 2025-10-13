import 'dart:convert' show utf8;
import 'dart:io' show Directory, File, FileMode, IOSink;

import 'package:intl/intl.dart' show DateFormat;
import 'package:path/path.dart' show join;

import '/enums/logging.dart' show LogLevels;

class LoggingManager {
  static final _instance = LoggingManager._internal();

  static final _writeLogsTimestampFormatter = DateFormat.Hms();
  static final _filenameTimestampFormatter = DateFormat('yyyy-MM-dd_HH-mm-ss');

  static final _filenameTimestamp = _filenameTimestampFormatter.format(
    DateTime.now(),
  );

  static final _logDir = Directory('logs');
  static final _logFile = File(join(_logDir.path, '$_filenameTimestamp.log'));

  IOSink? _sink;

  factory LoggingManager() {
    return _instance;
  }

  LoggingManager._internal() {
    _initializeLogger();
  }

  void _initializeLogger() {
    _logFile.createSync(recursive: true);

    _sink = _logFile.openWrite(mode: FileMode.append, encoding: utf8);
  }

  static void writeLog(LogLevels level, String message) {
    _instance._sink?.writeln(
      '[${_writeLogsTimestampFormatter.format(DateTime.now())}] ${level.value}: $message',
    );
  }

  static Future<void> saveLogs() async {
    await _instance._sink?.flush();
    await _instance._sink?.close();
  }
}

import 'dart:convert' show utf8;
import 'dart:io' show Directory, File, FileMode, IOSink;

import 'package:intl/intl.dart' show DateFormat;
import 'package:path/path.dart' show join;

import '../enums/logging.dart' show LogLevels;

class LoggingManager {
  static final _instance = LoggingManager._internal();

  static final _logDir = Directory('logs');
  static final _logFile = File(join(_logDir.path, 'app.log'));
  static final _timestampFormatter = DateFormat('dd/MM/yyyy HH:mm');

  IOSink? _sink;

  factory LoggingManager() {
    return _instance;
  }

  LoggingManager._internal() {
    _initializeLogger();
  }

  void _initializeLogger() {
    _ensureLogDirectory();

    _sink = _logFile.openWrite(mode: FileMode.append, encoding: utf8);
  }

  void _ensureLogDirectory() {
    if (!_logDir.existsSync()) {
      _logDir.createSync(recursive: true);
    }
    if (!_logFile.existsSync()) {
      _logFile.createSync();
    }
  }

  static void writeLog(LogLevels level, String message) {
    final timestamp = _timestampFormatter.format(DateTime.now());

    _instance._sink?.writeln('$timestamp - ${level.value}: $message');
  }

  static void saveLogs() {
    _instance._sink?.flush();
    _instance._sink?.close();
  }
}

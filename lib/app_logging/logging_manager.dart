import 'dart:convert' show utf8;
import 'dart:io' show Directory, File, FileMode, IOSink, ProcessSignal, exit;

import 'package:intl/intl.dart' show DateFormat;
import 'package:path/path.dart' show join;

import '../enums/logging.dart' show LogLevels;

class LoggingManager {
  static final LoggingManager _instance = LoggingManager._internal();

  static final Directory _logDir = Directory('logs');
  static final File _logFile = File(join(_logDir.path, 'app.log'));
  static final DateFormat _timestampFormatter = DateFormat('dd/MM/yyyy HH:mm');

  IOSink? _sink;

  final Map<LogLevels, void Function(String)> logLevels = {};

  factory LoggingManager() {
    return _instance;
  }

  LoggingManager._internal() {
    _initializeLogger();
  }

  void _initializeLogger() {
    _ensureLogDirectory();

    _sink = _logFile.openWrite(mode: FileMode.append, encoding: utf8);

    // Register flush on exit
    ProcessSignal.sigint.watch().listen((_) {
      _flushLogs();
      exit(0);
    });
    ProcessSignal.sigterm.watch().listen((_) {
      _flushLogs();
      exit(0);
    });
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

  void _flushLogs() {
    _sink?.flush();
    _sink?.close();
  }
}

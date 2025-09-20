enum LogLevels {
  info('INFO'),
  warning('WARNING'),
  error('ERROR'),
  critical('CRITICAL');

  const LogLevels(this.value);
  final String value;
}

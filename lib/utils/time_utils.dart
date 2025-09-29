bool hasOneMonthPassed(String lastCheckDateString) {
  final parts = lastCheckDateString.split('-');

  if (parts.length != 3) {
    throw FormatException('Invalid date format');
  }

  final lastCheck = DateTime(
    int.parse(parts[0]),
    int.parse(parts[1]),
    int.parse(parts[2]),
  );

  final now = DateTime.now();

  var monthsDifference =
      (now.year - lastCheck.year) * 12 + (now.month - lastCheck.month);

  if (now.day < lastCheck.day) {
    monthsDifference--;
  }

  return monthsDifference >= 1;
}

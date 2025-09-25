List<String> removeEmptyStrings(List<String> inputList) {
  return inputList.where((item) => item.trim().isNotEmpty).toList();
}

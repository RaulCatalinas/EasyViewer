import '/constants/regex.dart' show httpsPattern;
import 'strings_utils.dart' show removeEmptyStrings;

List<String> separateUrls(String urls) {
  final urlsWithSpaces = urls
      .replaceAll(httpsPattern, ' https://')
      .replaceAll(' ', '\n');

  return removeEmptyStrings(urlsWithSpaces.split('\n'));
}

final Map<String, RegExp> invalidChars = {
  'windows': RegExp(r'[<>:"/\\|?*]'),
  'macos': RegExp(r'[:/]'),
  'linux': RegExp(r'[/]'),
};

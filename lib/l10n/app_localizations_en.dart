// ignore: unused_import
import 'package:intl/intl.dart' as intl;
import 'app_localizations.dart';

// ignore_for_file: type=lint

/// The translations for English (`en`).
class AppLocalizationsEn extends AppLocalizations {
  AppLocalizationsEn([String locale = 'en']) : super(locale);

  @override
  String get select_download_directory => 'Select directory';

  @override
  String get download_video => 'Download video';

  @override
  String get download_audio => 'Download audio';

  @override
  String get exit_confirmation_body =>
      'Are you sure you wanna close the application?';

  @override
  String get yes_option => 'Yes';

  @override
  String get contact => 'Contact';

  @override
  String get change_language => 'Change language';

  @override
  String get spanish_language => 'Spanish';

  @override
  String get english_language => 'English';

  @override
  String get error_empty_url => 'No URL entered';

  @override
  String get error_connection =>
      'No internet connection available. Please check your network';

  @override
  String get error_youtube_url => 'The URL is not from YouTube';

  @override
  String get exit_confirmation_title => 'Close Application';

  @override
  String get select_directory => 'Select directory';

  @override
  String get placeholder_url => 'Video URL';

  @override
  String get placeholder_directory => 'Directory for video or audio in video';

  @override
  String get social_media => 'Social Media';

  @override
  String get update_available_title => 'A new version is available';

  @override
  String get update_available_body =>
      'Do you wanna update to the latest version?';

  @override
  String get later_option => 'Later';

  @override
  String get check_updates => 'Check for updates automatically';

  @override
  String get updated_version_title => 'Updated Version';

  @override
  String get updated_version_body =>
      'Congratulations! You are using the latest version of the app. \nNo update is required at this time.';

  @override
  String get error_age_restricted =>
      'This video is age restricted. \nYou can\'t download it.';

  @override
  String get error_live_stream =>
      'The live stream is still live. \nPlease try again when it has finished';

  @override
  String get error_only_members => 'This video is only available to members.';

  @override
  String get error_private_video => 'This video is private.';

  @override
  String get error_blocked_region => 'This video is blocked in your region.';

  @override
  String get error_unavailable_video => 'This video is unavailable.';

  @override
  String get error_default =>
      ' An error occurred while downloading the video. \nPlease try again later.\nIf the error persists, please contact me';

  @override
  String get whats_new_title => 'What\'s new?';

  @override
  String get whats_new_body => '';

  @override
  String get liability_notice_title => 'Liability notice';

  @override
  String get liability_notice_body =>
      'By using this app to download videos from YouTube, you agree that we\'re not responsible for any failure to comply with YouTube\'s terms and conditions. \n\nIt\'s important that you review and comply with YouTube\'s policies before commercially using any content downloaded through the app';

  @override
  String get settings_menu_title => 'Settings Menu';

  @override
  String get settings_menu_icon_tooltip => 'Settings';
}

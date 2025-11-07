import 'dart:async';

import 'package:flutter/foundation.dart';
import 'package:flutter/widgets.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:intl/intl.dart' as intl;

import 'app_localizations_en.dart';
import 'app_localizations_es.dart';

// ignore_for_file: type=lint

/// Callers can lookup localized strings with an instance of AppLocalizations
/// returned by `AppLocalizations.of(context)`.
///
/// Applications need to include `AppLocalizations.delegate()` in their app's
/// `localizationDelegates` list, and the locales they support in the app's
/// `supportedLocales` list. For example:
///
/// ```dart
/// import 'l10n/app_localizations.dart';
///
/// return MaterialApp(
///   localizationsDelegates: AppLocalizations.localizationsDelegates,
///   supportedLocales: AppLocalizations.supportedLocales,
///   home: MyApplicationHome(),
/// );
/// ```
///
/// ## Update pubspec.yaml
///
/// Please make sure to update your pubspec.yaml to include the following
/// packages:
///
/// ```yaml
/// dependencies:
///   # Internationalization support.
///   flutter_localizations:
///     sdk: flutter
///   intl: any # Use the pinned version from flutter_localizations
///
///   # Rest of dependencies
/// ```
///
/// ## iOS Applications
///
/// iOS applications define key application metadata, including supported
/// locales, in an Info.plist file that is built into the application bundle.
/// To configure the locales supported by your app, you’ll need to edit this
/// file.
///
/// First, open your project’s ios/Runner.xcworkspace Xcode workspace file.
/// Then, in the Project Navigator, open the Info.plist file under the Runner
/// project’s Runner folder.
///
/// Next, select the Information Property List item, select Add Item from the
/// Editor menu, then select Localizations from the pop-up menu.
///
/// Select and expand the newly-created Localizations item then, for each
/// locale your application supports, add a new item and select the locale
/// you wish to add from the pop-up menu in the Value field. This list should
/// be consistent with the languages listed in the AppLocalizations.supportedLocales
/// property.
abstract class AppLocalizations {
  AppLocalizations(String locale)
    : localeName = intl.Intl.canonicalizedLocale(locale.toString());

  final String localeName;

  static AppLocalizations? of(BuildContext context) {
    return Localizations.of<AppLocalizations>(context, AppLocalizations);
  }

  static const LocalizationsDelegate<AppLocalizations> delegate =
      _AppLocalizationsDelegate();

  /// A list of this localizations delegate along with the default localizations
  /// delegates.
  ///
  /// Returns a list of localizations delegates containing this delegate along with
  /// GlobalMaterialLocalizations.delegate, GlobalCupertinoLocalizations.delegate,
  /// and GlobalWidgetsLocalizations.delegate.
  ///
  /// Additional delegates can be added by appending to this list in
  /// MaterialApp. This list does not have to be used at all if a custom list
  /// of delegates is preferred or required.
  static const List<LocalizationsDelegate<dynamic>> localizationsDelegates =
      <LocalizationsDelegate<dynamic>>[
        delegate,
        GlobalMaterialLocalizations.delegate,
        GlobalCupertinoLocalizations.delegate,
        GlobalWidgetsLocalizations.delegate,
      ];

  /// A list of this localizations delegate's supported locales.
  static const List<Locale> supportedLocales = <Locale>[
    Locale('en'),
    Locale('es'),
  ];

  /// No description provided for @select_download_directory.
  ///
  /// In en, this message translates to:
  /// **'Select directory'**
  String get select_download_directory;

  /// No description provided for @download_video.
  ///
  /// In en, this message translates to:
  /// **'Download video'**
  String get download_video;

  /// No description provided for @download_audio.
  ///
  /// In en, this message translates to:
  /// **'Download audio'**
  String get download_audio;

  /// No description provided for @exit_confirmation_body.
  ///
  /// In en, this message translates to:
  /// **'Are you sure you wanna close the application?'**
  String get exit_confirmation_body;

  /// No description provided for @yes_option.
  ///
  /// In en, this message translates to:
  /// **'Yes'**
  String get yes_option;

  /// No description provided for @contact.
  ///
  /// In en, this message translates to:
  /// **'Contact'**
  String get contact;

  /// No description provided for @change_language.
  ///
  /// In en, this message translates to:
  /// **'Change language'**
  String get change_language;

  /// No description provided for @spanish_language.
  ///
  /// In en, this message translates to:
  /// **'Spanish'**
  String get spanish_language;

  /// No description provided for @english_language.
  ///
  /// In en, this message translates to:
  /// **'English'**
  String get english_language;

  /// No description provided for @error_empty_url.
  ///
  /// In en, this message translates to:
  /// **'No URL entered'**
  String get error_empty_url;

  /// No description provided for @error_connection.
  ///
  /// In en, this message translates to:
  /// **'No internet connection available. Please check your network'**
  String get error_connection;

  /// No description provided for @error_youtube_url.
  ///
  /// In en, this message translates to:
  /// **'The URL is not from YouTube'**
  String get error_youtube_url;

  /// No description provided for @exit_confirmation_title.
  ///
  /// In en, this message translates to:
  /// **'Close Application'**
  String get exit_confirmation_title;

  /// No description provided for @select_directory.
  ///
  /// In en, this message translates to:
  /// **'Select directory'**
  String get select_directory;

  /// No description provided for @placeholder_url.
  ///
  /// In en, this message translates to:
  /// **'Video URL'**
  String get placeholder_url;

  /// No description provided for @placeholder_directory.
  ///
  /// In en, this message translates to:
  /// **'Directory for video or audio in video'**
  String get placeholder_directory;

  /// No description provided for @social_media.
  ///
  /// In en, this message translates to:
  /// **'Social Media'**
  String get social_media;

  /// No description provided for @update_available_title.
  ///
  /// In en, this message translates to:
  /// **'A new version is available'**
  String get update_available_title;

  /// No description provided for @update_available_body.
  ///
  /// In en, this message translates to:
  /// **'Do you wanna update to the latest version?'**
  String get update_available_body;

  /// No description provided for @later_option.
  ///
  /// In en, this message translates to:
  /// **'Later'**
  String get later_option;

  /// No description provided for @check_updates.
  ///
  /// In en, this message translates to:
  /// **'Check for updates automatically'**
  String get check_updates;

  /// No description provided for @updated_version_title.
  ///
  /// In en, this message translates to:
  /// **'Updated Version'**
  String get updated_version_title;

  /// No description provided for @updated_version_body.
  ///
  /// In en, this message translates to:
  /// **'Congratulations! You are using the latest version of the app. \nNo update is required at this time.'**
  String get updated_version_body;

  /// No description provided for @error_age_restricted.
  ///
  /// In en, this message translates to:
  /// **'This video is age restricted. \nYou can\'t download it.'**
  String get error_age_restricted;

  /// No description provided for @error_live_stream.
  ///
  /// In en, this message translates to:
  /// **'The live stream is still live. \nPlease try again when it has finished'**
  String get error_live_stream;

  /// No description provided for @error_only_members.
  ///
  /// In en, this message translates to:
  /// **'This video is only available to members.'**
  String get error_only_members;

  /// No description provided for @error_private_video.
  ///
  /// In en, this message translates to:
  /// **'This video is private.'**
  String get error_private_video;

  /// No description provided for @error_blocked_region.
  ///
  /// In en, this message translates to:
  /// **'This video is blocked in your region.'**
  String get error_blocked_region;

  /// No description provided for @error_unavailable_video.
  ///
  /// In en, this message translates to:
  /// **'This video is unavailable.'**
  String get error_unavailable_video;

  /// No description provided for @error_default.
  ///
  /// In en, this message translates to:
  /// **' An error occurred while downloading the video. \nPlease try again later.\nIf the error persists, please contact me'**
  String get error_default;

  /// No description provided for @whats_new_title.
  ///
  /// In en, this message translates to:
  /// **'What\'s new?'**
  String get whats_new_title;

  /// No description provided for @whats_new_body.
  ///
  /// In en, this message translates to:
  /// **''**
  String get whats_new_body;

  /// No description provided for @liability_notice_title.
  ///
  /// In en, this message translates to:
  /// **'Liability notice'**
  String get liability_notice_title;

  /// No description provided for @liability_notice_body.
  ///
  /// In en, this message translates to:
  /// **'By using this app to download videos from YouTube, you agree that we\'re not responsible for any failure to comply with YouTube\'s terms and conditions. \n\nIt\'s important that you review and comply with YouTube\'s policies before commercially using any content downloaded through the app'**
  String get liability_notice_body;

  /// No description provided for @settings_menu_title.
  ///
  /// In en, this message translates to:
  /// **'Settings Menu'**
  String get settings_menu_title;
}

class _AppLocalizationsDelegate
    extends LocalizationsDelegate<AppLocalizations> {
  const _AppLocalizationsDelegate();

  @override
  Future<AppLocalizations> load(Locale locale) {
    return SynchronousFuture<AppLocalizations>(lookupAppLocalizations(locale));
  }

  @override
  bool isSupported(Locale locale) =>
      <String>['en', 'es'].contains(locale.languageCode);

  @override
  bool shouldReload(_AppLocalizationsDelegate old) => false;
}

AppLocalizations lookupAppLocalizations(Locale locale) {
  // Lookup logic when only language code is specified.
  switch (locale.languageCode) {
    case 'en':
      return AppLocalizationsEn();
    case 'es':
      return AppLocalizationsEs();
  }

  throw FlutterError(
    'AppLocalizations.delegate failed to load unsupported locale "$locale". This is likely '
    'an issue with the localizations generation tool. Please file an issue '
    'on GitHub with a reproducible sample app and the gen-l10n configuration '
    'that was used.',
  );
}

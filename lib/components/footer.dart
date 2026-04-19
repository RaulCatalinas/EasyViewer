import 'package:fluikit/widgets.dart';
import 'package:flutter/material.dart'
    show
        BuildContext,
        ButtonStyle,
        IconButton,
        Icons,
        Row,
        SizedBox,
        StatelessWidget,
        Widget,
        WidgetState,
        WidgetStateProperty,
        Icon;
import 'package:flutter/rendering.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart'
    show FaIcon, FontAwesomeIcons;

import '/constants/social_media.dart' show socialMedia;
import '/enums/social_media.dart' show SocialMedia;
import '/l10n/app_localizations.dart' show AppLocalizations;
import '/utils/urls.dart' show openUrl, openEmail;

class Footer extends StatelessWidget {
  const Footer({super.key});

  @override
  Widget build(BuildContext context) {
    final commonStyles = ButtonStyle(
      enableFeedback: true,
      mouseCursor: WidgetStateProperty.resolveWith((state) {
        if (state.contains(WidgetState.hovered)) {
          return SystemMouseCursors.click;
        }

        return SystemMouseCursors.basic;
      }),
    );

    return Row(
      mainAxisAlignment: .center,
      children: [
        FluiText(text: AppLocalizations.of(context)!.made_by, fontSize: 13),

        const SizedBox(width: 16),

        IconButton(
          icon: const FaIcon(FontAwesomeIcons.xTwitter, size: 18),
          style: commonStyles,
          onPressed: () async {
            await openUrl(socialMedia[SocialMedia.twitter]!);
          },
        ),

        const SizedBox(width: 8),

        IconButton(
          icon: const FaIcon(FontAwesomeIcons.instagram, size: 18),
          style: commonStyles,
          onPressed: () async {
            await openUrl(socialMedia[SocialMedia.instagram]!);
          },
        ),

        const SizedBox(width: 8),

        IconButton(
          icon: const Icon(Icons.email_outlined, size: 18),
          style: commonStyles,
          onPressed: () async {
            await openEmail(socialMedia[SocialMedia.email]!);
          },
        ),
      ],
    );
  }
}

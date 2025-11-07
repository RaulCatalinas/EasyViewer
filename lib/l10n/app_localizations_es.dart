// ignore: unused_import
import 'package:intl/intl.dart' as intl;
import 'app_localizations.dart';

// ignore_for_file: type=lint

/// The translations for Spanish Castilian (`es`).
class AppLocalizationsEs extends AppLocalizations {
  AppLocalizationsEs([String locale = 'es']) : super(locale);

  @override
  String get select_download_directory => 'Seleccionar directorio';

  @override
  String get download_video => 'Descargar video';

  @override
  String get download_audio => 'Descargar audio';

  @override
  String get exit_confirmation_body =>
      '¿Seguro que quieres cerrar la aplicación?';

  @override
  String get yes_option => 'Si';

  @override
  String get contact => 'Contacto';

  @override
  String get change_language => 'Cambiar idioma';

  @override
  String get spanish_language => 'Español';

  @override
  String get english_language => 'Ingles';

  @override
  String get error_empty_url => 'No se ha introducido ninguna URL';

  @override
  String get error_connection =>
      'No hay conexión a Internet disponible. Por favor Comprueba tu red';

  @override
  String get error_youtube_url => 'La URL no es de YouTube';

  @override
  String get exit_confirmation_title => 'Cerrar aplicación';

  @override
  String get select_directory => 'Selecciona directorio';

  @override
  String get placeholder_url => 'URL del video';

  @override
  String get placeholder_directory =>
      'Directorio para el video o el audio del video';

  @override
  String get social_media => 'Redes sociales';

  @override
  String get update_available_title => 'Hay una nueva versión disponible';

  @override
  String get update_available_body =>
      '¿Quieres actualizar a la ultima versión?';

  @override
  String get later_option => 'Más tarde ';

  @override
  String get check_updates => 'Comprobar actualizaciones automáticamente';

  @override
  String get updated_version_title => 'Versión Actualizada';

  @override
  String get updated_version_body =>
      '¡Felicidades! Estás utilizando la última versión de la aplicación. \nNo es necesario realizar ninguna actualización en este momento.';

  @override
  String get error_age_restricted =>
      'Este video tiene restricción de edad. \nNo puedes descargarlo.';

  @override
  String get error_live_stream =>
      'La transmisión en directo todavía esta vigente. \nVuelve a intentarlo cuando haya finalizado';

  @override
  String get error_only_members =>
      'Este video solo está disponible para miembros.';

  @override
  String get error_private_video => 'Este video es privado.';

  @override
  String get error_blocked_region => 'Este video está bloqueado en tu región.';

  @override
  String get error_unavailable_video => 'Este video no está disponible.';

  @override
  String get error_default =>
      ' Ocurrió un error al descargar el video. \nInténtalo nuevamente más tarde.\nSi el error persiste, ponte en contacto conmigo.';

  @override
  String get whats_new_title => '¿Que hay de nuevo?';

  @override
  String get whats_new_body => '';

  @override
  String get liability_notice_title => 'Aviso de responsabilidad';

  @override
  String get liability_notice_body =>
      'Al utilizar esta aplicación para descargar videos de YouTube, usted acepta que no nos hacemos responsables por cualquier incumplimiento de los términos y condiciones de YouTube. \n\nEs importante que revise y cumpla con las políticas de YouTube antes usar comercialmente cualquier contenido descargado a través de la app.';

  @override
  String get settings_menu_title => 'Menú de configuración';
}

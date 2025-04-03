package config

import (
	"fyne.io/fyne/v2"
	appSettings "github.com/RaulCatalinas/EasyViewer/internal/app_settings"
)

func ConfigureWindow(window fyne.Window) {
	settings := appSettings.GetWindowSettings()

	window.Resize(fyne.NewSize(settings.Width, settings.Height))
	window.SetFixedSize(settings.FixedSize)
	window.CenterOnScreen()
}

func SetIcon(window fyne.Window) {
	icon, _ := fyne.LoadResourceFromPath("internal/assets/icon.png")
	window.SetIcon(icon)
}

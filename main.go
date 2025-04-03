package main

import (
	"fyne.io/fyne/v2/app"
	"fyne.io/fyne/v2/widget"
	"github.com/RaulCatalinas/EasyViewer/internal/config"
)

func main() {
	app := app.New()
	window := app.NewWindow("EasyViewer")

	config.ConfigureWindow(window)
	config.SetIcon(window)

	window.SetContent(widget.NewLabel("Hello World!"))

	window.Show()
	app.Run()
}

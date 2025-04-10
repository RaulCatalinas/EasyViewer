package main

import (
	"embed"

	"github.com/wailsapp/wails/v2"
	"github.com/wailsapp/wails/v2/pkg/options"

	appSettings "github.com/RaulCatalinas/EasyViewer/internal/app_settings"
)

//go:embed all:frontend/dist
var assets embed.FS

//go:embed build/appicon.png
var icon []byte

func main() {
	// Create an instance of the app structure
	app := NewApp()

	// Create application with options
	err := wails.Run(&options.App{
		Title:         appSettings.TITLE,
		Width:         appSettings.WIDTH,
		Height:        appSettings.HEIGHT,
		DisableResize: appSettings.DISABLE_RESIZE,
		Assets:        assets,
		OnStartup:     app.startup,
		Bind: []interface{}{
			app,
		},
	})

	if err != nil {
		println("Error:", err.Error())
	}
}

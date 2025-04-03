package app_settings

type WindowSettings struct {
	Title        string
	Width        float32
	Height       float32
	PreventClose bool
	FixedSize    bool
}

func GetWindowSettings() WindowSettings {
	return WindowSettings{
		Title:        "EasyViewer",
		Width:        830,
		Height:       575,
		PreventClose: true,
		FixedSize:    true,
	}
}

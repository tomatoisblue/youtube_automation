import ctypes

def close_foreground_window():
	handle = ctypes.windll.user32.GetForegroundWindow()
	ctypes.windll.user32.ShowWindow(handle, 0)
# coding:utf-8
import YoutubeAutomation
import OSOperation


if __name__ == "__main__":
	url = input()

	# open video page with YouTubeTools
	yt = YoutubeAutomation.YouTubeAutomation(detach = True)
	yt.open(url)

	yt.basic_background()
	print("COMPLETED")

	# OSOperation.close_foreground_window()
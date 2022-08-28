# coding:utf-8
import YoutubeAutomation
import OSOperation


if __name__ == "__main__":
	url = input()

	# open video page with YouTubeTools
	yt = YoutubeAutomation.YouTubeAutomation(detach = True)
	yt.open(url)

	yt.ad_routine()

	print("COMPLETED")

	# OSOperation.close_foreground_window()
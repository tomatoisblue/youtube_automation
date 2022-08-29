# coding:utf-8
import YoutubeAutomation
import OSOperation


if __name__ == "__main__":
	url = input()

	yt = YoutubeAutomation.YouTube(detach = True)
	yt.open(url)
	yt.basic_background()
	OSOperation.minimize_foreground_window()

	print("COMPLETED")
	yt.ad_routine()


# coding:utf-8
import YoutubeAutomation
import OSOperation


if __name__ == "__main__":

	# LofiGirl youtube channel page
	url = 'https://www.youtube.com/c/LofiGirl'

	yt = YoutubeAutomation.YouTube(headless = True)
	yt.open(url)
	video_url = yt.get_url_of_top_video()
	yt = YoutubeAutomation.YouTube(detach = True, brave = True)
	yt.open(video_url)
	yt.basic_background()
	# OSOperation.close_foreground_window()
	OSOperation.minimize_foreground_window()

	print("COMPLETED")

	yt.ad_routine()

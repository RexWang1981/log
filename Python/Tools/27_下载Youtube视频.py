# this code works well, at least for 1 time.

import yt_dlp


def download_youtube_video(url, save_path):
	ydl_opts = {
		'outtmpl': f'{save_path}/%(title)s.%(ext)s',
	}

	try:
		with yt_dlp.YoutubeDL(ydl_opts) as ydl:
			ydl.download([url])
			print(f"视频已成功下载到 {save_path}")
	except Exception as e:
		print(f"下载视频时出错: {e}")


# 示例用法
url = "https://www.youtube.com/watch?v=yEwdpLSRrP8"
save_path = "./videos"
download_youtube_video(url, save_path)

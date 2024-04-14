from tiktok_uploader.upload import upload_video, upload_videos
from tiktok_uploader.auth import AuthBackend

# single video

if __name__ == "__main__":

	# Tiktok
	# Leave this last, need to manually click Post...
	upload_video('video.mp4', description="test", cookies='tiktok_cookies.txt')	
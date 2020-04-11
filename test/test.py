import os


def main():
	convertToVideo("view_2.png", "w.mp3", "w_out.mp4")

def convertToVideo(view_path, mp3_path, mp4_path):
	shell = "ffmpeg -loop 1 -r 1 -i {}  -i {} -c:a copy -shortest -c:v libx264 {}".format(view_path, mp3_path, mp4_path)
	os.system(shell)

if __name__ == "__main__":
    main()
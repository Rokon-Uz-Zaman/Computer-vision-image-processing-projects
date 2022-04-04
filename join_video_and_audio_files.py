#pip install moviepy
from moviepy.editor import VideoFileClip,AudioFileClip

#path
videopath='/content/videofile1.mp4'
audiopath='/content/audiofile1.mp3'


#read
video=VideoFileClip(videopath)
audio=AudioFileClip(audiopath)

#join
video=video.set_audio(audio)

#write
video.write_videofile("videoAudiojoined.mp4")

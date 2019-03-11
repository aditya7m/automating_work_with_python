# You need to have module moviepy installed. If not then use command
# pip install moviepy to install it


import moviepy.editor as mp
video = mp.VideoFileClip("SampleVideo.mp4")
video.audio.write_audiofile("SampleAudio.mp3")

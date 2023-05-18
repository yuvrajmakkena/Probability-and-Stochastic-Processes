import os
import random
from moviepy.editor import VideoFileClip
from playsound import playsound

# Set the path to the folder containing the videos
video_folder = "videos"

# Set the path to the folder to store the audio files
audio_folder = "audio"

# Create the audio folder if it doesn't exist
os.makedirs(audio_folder, exist_ok=True)

# Get a list of all video files in the folder
video_files = [file for file in os.listdir(video_folder) if file.endswith(".mp4")]

# Convert the video files to audio and save them in the audio folder
audio_files = []
for video_file in video_files:
    # Convert the video to audio
    video_path = os.path.join(video_folder, video_file)
    audio_file = os.path.splitext(video_file)[0] + ".mp3"
    audio_path = os.path.join(audio_folder, audio_file)

    video_clip = VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(audio_path)

    # Close the audio and video clips
    audio_clip.close()
    video_clip.close()

    # Append the audio file path to the list
    audio_files.append(audio_path)

# Shuffle the list of audio files
random.shuffle(audio_files)

# Play the audio files in a uniform distribution
for audio_file in audio_files:
    playsound(audio_file)

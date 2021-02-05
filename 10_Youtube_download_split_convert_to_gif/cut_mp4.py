from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
# ffmpeg_extract_subclip("full.mp4", start_seconds, end_seconds, targetname="cut.mp4")
ffmpeg_extract_subclip("Chasing Toyota Fortuner  Aspire  Highway Chase.mp4", 15, 40, targetname="Highway_sample.mp4")
# ffmpeg_extract_subclip("Kingsman.MKV", 3014, 3164, targetname="Kingsman_clip_2.mp4")

"""
import moviepy.editor as mp
clip = mp.VideoFileClip("Kingsman_clip_1.mp4")
clip_resized = clip.resize(height=360) # make the height 360px ( According to moviePy documenation The width is then computed so that the width/height ratio is conserved.)
clip_resized.write_videofile("Kingsman_resized_1.mp4")

clip = mp.VideoFileClip("Kingsman_clip_2.mp4")
clip_resized = clip.resize(height=360) # make the height 360px ( According to moviePy documenation The width is then computed so that the width/height ratio is conserved.)
clip_resized.write_videofile("Kingsman_resized_2.mp4")
"""


from moviepy.editor import VideoFileClip
import moviepy.video.fx.all as vfx

in_loc = 'Animation Final-1.m4v'
out_loc = 'dummy_out_24.mp4'

# Import video clip
clip = VideoFileClip(in_loc)
print("fps: {}".format(clip.fps))

# Modify the FPS
clip = clip.set_fps(clip.fps * 3)

# Apply speed up
final = clip.fx(vfx.speedx, 24)
print("fps: {}".format(final.fps))

# Save video clip
final.write_videofile(out_loc)
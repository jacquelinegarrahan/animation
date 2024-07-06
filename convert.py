from moviepy.editor import VideoFileClip

def mp4_to_gif(input_path, output_path):
    # Load the video clip
    clip = VideoFileClip(input_path)
    # Write the GIF file
    clip.write_gif(output_path)

# Example usage
input_path = 'random.mp4'
output_path = 'random.gif'
mp4_to_gif(input_path, output_path)

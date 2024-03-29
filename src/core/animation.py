import os
import glob
import time
import posixpath as path
from src.core.gui_maze_solver import update_image
from PIL import Image
import re

_nsre = re.compile('([0-9]+)')

class Animation:
    current_frame = 0

    def natural_sort_key(s):
        return [int(text) if text.isdigit() else text.lower()
                for text in re.split(_nsre, s)]   

    def get_frame_count():
        dirname = path.dirname(__file__)
        image_path = path.join(dirname.split('/src', 1)[0], 'images/*')
        files = glob.glob(image_path)
        return len(files)

    def show_next_frame(maze): 
        Animation.current_frame = (Animation.current_frame + 1) % Animation.get_frame_count()
        update_image(Animation.current_frame)

    def show_prev_frame(maze): 
        Animation.current_frame = (Animation.current_frame - 1) % Animation.get_frame_count()
        update_image(Animation.current_frame)

    def make_gif(maze, frame_folder):
        filesSorted = sorted(glob.glob(frame_folder),key=Animation.natural_sort_key)
        frames = [Image.open(image) for image in filesSorted ]
        frame_one = frames[0]
        frame_one.save("animation/maze_path_animation.gif", format="GIF", 
            append_images=frames,save_all=True, duration=(len(maze)*50), loop=0)

    def export_gif(maze):
        dirname = path.dirname(__file__)
        image_path = path.join(dirname.split('/src', 1)[0], 'images/*')
        Animation.make_gif(maze, image_path)

    def clear_frame_count():
        Animation.current_frame = 0
        update_image(Animation.current_frame)

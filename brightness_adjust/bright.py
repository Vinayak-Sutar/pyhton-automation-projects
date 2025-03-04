import time
import os
from PIL import Image
import pygame
import pygame.camera


def capture_image(filename):
    pygame.camera.init()
    camlist = pygame.camera.list_cameras()
    if not camlist:
        raise ValueError("No camera found")
    cam = pygame.camera.Camera(camlist[0], (640, 480))
    cam.start()
    image = cam.get_image()
    pygame.image.save(image, filename)
    cam.stop()

def calculate_brightness(image_path):
    # image preprocessing
    image = Image.open(image_path)
    greyscale_image = image.convert('L')
    histogram = greyscale_image.histogram()
    pixels = sum(histogram)
    brightness = scale = len(histogram)
    
    # calculate brightness level
    for index in range(scale):
        ratio = histogram[index] / pixels
        brightness += ratio * (-scale + index)
    
    return 1 if brightness == 255 else brightness / scale

def adjust_brightness():
    filename = "filename.jpg"
    brightness_offset = 0.2
    capture_image(filename)
    level = calculate_brightness(filename)
    adjusted_level = min(level + brightness_offset, 1)
    os.system(f"xrandr --output eDP --brightness {adjusted_level}")
    os.remove(filename)

if __name__ == "__main__":
    while True:
        adjust_brightness()
        time.sleep(30)
        # repeats every 30 seconds 

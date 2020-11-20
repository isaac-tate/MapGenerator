#Imports
import noise
import numpy as np
from PIL import Image


#Generation parameters
IMAGE_SHAPE = (1024,1024)
START_POSITION = (12245, 3222)
REPEAT = (10000, 10000)
PERLIN_BASE = 2
SCALE = 1
OCTAVES = 5
PERSISTANCE = 15
LACUNARITY = 0.2


#Colours
ocean = [95, 216, 250]
beach = [244, 220, 181]
lite_grass = [177, 221, 161]
dark_grass = [102, 141, 60]
lite_stone = [195, 183, 172]
snow = [231, 227, 215]
white = [255, 255, 255]


'''
Generates Perlin noise map
'''
def create_world():
    world = np.zeros(IMAGE_SHAPE)
    for i in range(IMAGE_SHAPE[0]):
        for j in range(IMAGE_SHAPE[1]):
            world[i][j] = noise.pnoise2(i+START_POSITION[0]/SCALE,
                                        j+START_POSITION[1]/SCALE,
                                        octaves=OCTAVES,
                                        persistence=PERSISTANCE,
                                        lacunarity=LACUNARITY,
                                        repeatx=REPEAT[0],
                                        repeaty=REPEAT[1],
                                        base=PERLIN_BASE)
    return world


'''
Takes perlin map and adds layer colour
'''
def add_color(world):
    color_world = np.zeros(world.shape+(3,))
    for i in range(IMAGE_SHAPE[0]):
        for j in range(IMAGE_SHAPE[1]):
            if world[i][j] < 0:
                color_world[i][j] = ocean
            elif world[i][j] < 0.10:
                color_world[i][j] = beach
            elif world[i][j] < 0.15:
                color_world[i][j] = lite_grass
            elif world[i][j] < 0.20:
                color_world[i][j] = dark_grass
            elif world[i][j] < 0.30:
                color_world[i][j] = lite_stone
            elif world[i][j] < 0.40:
                color_world[i][j] = snow
            else:
                color_world[i][j] = white

    return color_world


'''
Creates new map and shows it
'''
def save_new_map(save_path):
    world = create_world()
    color_world = add_color(world)
    #Image.save("ex1.png", format="PNG")
    Image.fromarray(np.uint8(color_world), "RGB").save(save_path)



save_new_map("filename.png")

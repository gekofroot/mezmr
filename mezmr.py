#    Copyright (C) 2022 gekofroot
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    any later version.
#
#    This program is distributed WITHOUT ANY WARRANTY; 
#    See the GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <https://www.gnu.org/licenses/>.




#import module
import pygame as pg
from pygame.locals import *
import sys
from colour_palette import *
from utils import *


#initialize
pg.init()

pg.mouse.set_visible(False)

#variables
width = 700
height = 700
width_b = 700
height_b = 700

width_c = 700
height_c = 700
width_d = 700
height_d = 700

width_e = 700
height_e = 700
width_f = 700
height_f = 700

width_g = 700
height_g = 700
width_h = 700
height_h = 700

width_i = 700
height_i = 700
width_j = 700
height_j = 700

width_k = 700
height_k = 700
width_l = 700
height_l = 700

width_m = 700
height_m = 700
width_n = 700
height_n = 700

width_m = 700
height_m = 700
width_n = 700
height_n = 700

screen = pg.display.set_mode((width, height))

col_lis = []

mult_tot = 2
mult_col = 1
mult_blck = 20
black_palette = [BLACK]

def add_color_palette(palette):
    com = []
    for x in black_palette * mult_blck:
        com.append(x)
    for x in palette[ : :-1] * mult_col:
        com.append(x)
    for x in palette * mult_col:
        com.append(x)
    for x in com * mult_tot:
        col_lis.append(x)

palette_list = [red_palette, orange_palette, yellow_palette, green_palette, blue_palette, violet_palette, cyan_palette]

for x in palette_list:
    add_color_palette(x)

def main():

    get_speed_up = False
    get_speed_down = False
    page_speed_up = False
    page_speed_down = False
    line_size_up = False
    line_size_down = False

    running = True
    while running:
        color_list_o = col_lis
        get_speed = 70
        line_size = 10
        bottom_range = 0
        screen.fill(BLACK)

        
        pg.display.set_gamma(1.1)
        
        width_1 = 1
        height_1 = 0
        size_x = 20
        size_y = 20
        
        width_2 = 1323
        height_2 = 20

        width_3 = 41
        height_3 = 40
        
        width_4 = 1283
        height_4 = 60
        
        width_5 = 81
        height_5 = 80
        
        width_6 = 1240
        height_6 = 100
        
        width_7 = 121
        height_7 = 120
        
        width_8 = 1200
        height_8 = 140
        
        width_9 = 161
        height_9 = 160
        
        width_10 = 1160
        height_10 = 180
        
        width_11 = 201
        height_11 = 200
        
        width_12 = 1120
        height_12 = 220
        
        width_13 = 241
        height_13 = 240
        
        width_14 = 1080
        height_14 = 260
        
        width_15 = 281
        height_15 = 280
        
        width_16 = 1040
        height_16 = 300
        
        dirlis = []

        for x in range(16):
            dirlis.append('right')

        direction_17 = 'down'
        
        count_2 = 0 
        for color in color_list_o * 20:
            for event in pg.event.get():
                if event.type == KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                        sys.exit()
                    elif event.key == pg.K_SPACE:
                        screen.fill(BLACK)
                        pg.display.update()
                    elif event.key == pg.K_UP:
                        get_speed_up = True
                    elif event.key == pg.K_DOWN:
                        get_speed_down = True
                    elif event.key == pg.K_LEFT:
                        line_size_down = True
                        line_size_up = False
                    elif event.key == pg.K_RIGHT:
                        line_size_up = True
                        line_size_down = False
                
                if event.type == KEYUP:
                    if event.key == pg.K_UP:
                        get_speed_up = False
                    elif event.key == pg.K_DOWN:
                        get_speed_down = False
                    elif event.key == pg.K_LEFT:
                        line_size_down = False
                    elif event.key == pg.K_RIGHT:
                        line_size_up = False
                
                if get_speed_up:
                    get_speed -= 5
                    if get_speed <= 0:
                        get_speed = 0
                if get_speed_down:
                    get_speed += 5
                    if get_speed >= 20:
                        page_speed = 20
                if line_size_down:
                    line_size -= 1
                    if line_size <= 1:
                        line_size = 1
                if line_size_up:
                    line_size += 1
                    if line_size >= 10:
                        line_size = 10


            for event in pg.event.get():
                if event == QUIT:
                    running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                        sys.exit()
            
            width_lis = [
                    width_1, width_2, width_3, width_4,
                    width_5, width_6, width_7, width_8,
                    width_9, width_10, width_11, width_12,
                    width_13, width_14, width_15, width_16
                    ]
            
            height_lis = [
                    height_1, height_2, height_3, height_4,
                    height_5, height_6, height_7, height_8,
                    height_9, height_10, height_11, height_12,
                    height_13, height_14, height_15, height_16
                    ]
            

            count = 0
            for x in range(0, len(width_lis), 1):
                elidraw(screen, color, width_lis[count], height_lis[count], size_x, size_y, line_size)
                count += 1
            
            if dirlis[0] == 'right':
                width_1 += 20
                if width_1 >= width - 30:
                    dirlis[0] = 'down'
            elif dirlis[0] == 'down':
                height_1 += 20
                if height_1 >= height - 31:
                    dirlis[0] = 'left'
            elif dirlis[0] == 'left':
                width_1 -= 20
                if width_1 <= 12:
                   dirlis[0] = 'up'
            elif dirlis[0] == 'up':
                height_1 -= 20
                if height_1 <= 0:
                    dirlis[0] = 'right'

            if dirlis[1] == 'right':
                width_2 -= 20
                if width_2 <= 32:
                    dirlis[1] = 'down'
            elif dirlis[1] == 'down':
                height_2 += 20
                if height_2 >= height_b - 51:
                    dirlis[1] = 'left'
            elif dirlis[1] == 'left':
                width_2 += 20
                if width_2 >= width_b - 50:
                    dirlis[1] = 'up'
            elif dirlis[1] == 'up':
                height_2 -= 20
                if height_2 <= 20:
                    dirlis[1] = 'right'
            
            if dirlis[2] == 'right':
                width_3 += 20
                if width_3 >= width_c - 70:
                    dirlis[2] = 'down'
            elif dirlis[2] == 'down':
                height_3 += 20
                if height_3 >= height_c - 71:
                    dirlis[2] = 'left'
            elif dirlis[2] == 'left':
                width_3 -= 20
                if width_3 <= 50:
                    dirlis[2] = 'up'
            elif dirlis[2] == 'up':
                height_3 -= 20
                if height_3 <= 40:
                    dirlis[2] = 'right'

            if dirlis[3] == 'right':
                width_4 -= 20
                if width_4 <= 70:
                    dirlis[3] = 'down'
            elif dirlis[3] == 'down':
                height_4 += 20
                if height_4 >= height_d - 91:
                    dirlis[3] = 'left'
            elif dirlis[3] == 'left':
                width_4 += 20
                if width_4 >= width_d - 90:
                    dirlis[3] = 'up'
            elif dirlis[3] == 'up':
                height_4 -= 20
                if height_4 <= 60:
                    dirlis[3] = 'right'

            if dirlis[4] == 'right':
                width_5 += 20
                if width_5 >= width_e - 110:
                    dirlis[4] = 'down'
            elif dirlis[4] == 'down':
                height_5 += 20
                if height_5 >= height_e - 111:
                    dirlis[4] = 'left'
            elif dirlis[4] == 'left':
                width_5 -= 20
                if width_5 <= 90:
                    dirlis[4] = 'up'
            elif dirlis[4] == 'up':
                height_5 -= 20
                if height_5 <= 80:
                    dirlis[4] = 'right'

            if dirlis[5] == 'right':
                width_6 -= 19
                if width_6 <= 112:
                    dirlis[5] = 'down'
            elif dirlis[5] == 'down':
                height_6 += 20
                if height_6 >= height_f - 130:
                    dirlis[5] = 'left'
            elif dirlis[5] == 'left':
                width_6 += 19
                if width_6 >= width_f - 130:
                    dirlis[5] = 'up'
            elif dirlis[5] == 'up':
                height_6 -= 20
                if height_6 <= 100:
                    dirlis[5] = 'right'
            
            if dirlis[6] == 'right':
                width_7 += 20
                if width_7 >= width_g - 152:
                    dirlis[6] = 'down'
            elif dirlis[6] == 'down':
                height_7 += 20
                if height_7 >= height_g - 151:
                    dirlis[6] = 'left'
            elif dirlis[6] == 'left':
                width_7 -= 20
                if width_7 <= 132:
                    dirlis[6] = 'up'
            elif dirlis[6] == 'up':
                height_7 -= 20
                if height_7 <= 120:
                    dirlis[6] = 'right'

            if dirlis[7] == 'right':
                width_8 -= 20
                if width_8 <= 152:
                    dirlis[7] = 'down'
            elif dirlis[7] == 'down':
                height_8 += 20
                if height_8 >= height_h - 171:
                    dirlis[7] = 'left'
            elif dirlis[7] == 'left':
                width_8 += 20
                if width_8 >= width_h - 170:
                    dirlis[7] = 'up'
            elif dirlis[7] == 'up':
                height_8 -= 20
                if height_8 <= 140:
                    dirlis[7] = 'right'
            
            if dirlis[8] == 'right':
                width_9 += 20
                if width_9 >= width_i - 191:
                    dirlis[8] = 'down'
            elif dirlis[8] == 'down':
                height_9 += 20
                if height_9 >= height_i - 191:
                    dirlis[8] = 'left'
            elif dirlis[8] == 'left':
                width_9 -= 20
                if width_9 <= 172:
                    dirlis[8] = 'up'
            elif dirlis[8] == 'up':
                height_9 -= 20
                if height_9 <= 160:
                    dirlis[8] = 'right'
            
            if dirlis[9] == 'right':
                width_10 -= 20
                if width_10 <= 192:
                    dirlis[9] = 'down'
            elif dirlis[9] == 'down':
                height_10 += 20
                if height_10 >= height_j - 211:
                    dirlis[9] = 'left'
            elif dirlis[9] == 'left':
                width_10 += 20
                if width_10 >= width_j - 210:
                    dirlis[9] = 'up'
            elif dirlis[9] == 'up':
                height_10 -= 20
                if height_10 <= 180:
                    dirlis[9] = 'right'

            if dirlis[10] == 'right':
                width_11 += 20
                if width_11 >= width_k - 230:
                    dirlis[10] = 'down'
            elif dirlis[10] == 'down':
                height_11 += 20
                if height_11 >= height_k - 231:
                    dirlis[10] = 'left'
            elif dirlis[10] == 'left':
                width_11 -= 20
                if width_11 <= 212:
                    dirlis[10] = 'up'
            elif dirlis[10] == 'up':
                height_11 -= 20
                if height_11 <= 200:
                    dirlis[10] = 'right'

            if dirlis[11] == 'right':
                width_12 -= 20
                if width_12 <= 222:
                    dirlis[11] = 'down'
            elif dirlis[11] == 'down':
                height_12 += 20
                if height_12 >= height_l - 251:
                    dirlis[11] = 'left'
            elif dirlis[11] == 'left':
                width_12 += 20
                if width_12 >= width_l - 250:
                    dirlis[11] = 'up'
            elif dirlis[11] == 'up':
                height_12 -= 20
                if height_12 <= 220:
                    dirlis[11] = 'right'

            if dirlis[12] == 'right':
                width_13 += 20
                if width_13 >= width_m - 270:
                    dirlis[12] = 'down'
            elif dirlis[12] == 'down':
                height_13 += 20
                if height_13 >= height_m - 271:
                    dirlis[12] = 'left'
            elif dirlis[12] == 'left':
                width_13 -= 20
                if width_13 <= 242:
                    dirlis[12] = 'up'
            elif dirlis[12] == 'up':
                height_13 -= 20
                if height_13 <= 240:
                    dirlis[12] = 'right'

            if dirlis[13] == 'right':
                width_14 -= 20
                if width_14 <= 272:
                    dirlis[13] = 'down'
            elif dirlis[13] == 'down':
                height_14 += 20
                if height_14 >= height_n - 291:
                    dirlis[13] = 'left'
            elif dirlis[13] == 'left':
                width_14 += 20
                if width_14 >= width_n - 290:
                    dirlis[13] = 'up'
            elif dirlis[13] == 'up':
                height_14 -= 20
                if height_14 <= 270:
                    dirlis[13] = 'right'

            if dirlis[14] == 'right':
                width_15 += 20
                if width_15 >= width_m - 310:
                    dirlis[14] = 'down'
            elif dirlis[14] == 'down':
                height_15 += 20
                if height_15 >= height_m - 311:
                    dirlis[14] = 'left'
            elif dirlis[14] == 'left':
                width_15 -= 20
                if width_15 <= 292:
                    dirlis[14] = 'up'
            elif dirlis[14] == 'up':
                height_15 -= 20
                if height_15 <= 280:
                    dirlis[14] = 'right'

            if dirlis[15] == 'right':
                width_16 -= 20
                if width_16 <= 302:
                    dirlis[15] = 'down'
            elif dirlis[15] == 'down':
                height_16 += 20
                if height_16 >= height_n - 331:
                    dirlis[15] = 'left'
            elif dirlis[15] == 'left':
                width_16 += 20
                if width_16 >= width_n - 330:
                    dirlis[15] = 'up'
            elif dirlis[15] == 'up':
                height_16 -= 20
                if height_16 <= 300:
                    dirlis[15] = 'right'
            
            
            pg.display.update()
            pg.time.wait(get_speed)


        pg.display.update()


if __name__ == '__main__':
    main()

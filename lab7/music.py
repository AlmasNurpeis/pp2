import pygame as p
import os
#87783170341 Ұлбике Үсенқызы
p.init()

class SOUND:
    def __init__(self, path_to_sound, path_to_photo):
        self.sound = p.mixer.Sound('lab7\\music\\' + path_to_sound)
        self.photo = p.image.load('lab7\\assets\\imagesformusic\\' + path_to_photo)
        self.is_playing = True
    
    def placePhoto(self,screen):
        self.photo = p.transform.scale(self.photo, (430, 410))
        screen.blit(self.photo, (31, 121))

path_to_sound = os.listdir('lab7\\music\\')
path_to_photo = os.listdir('lab7\\assets\\imagesformusic\\')
path_to_sound.sort()
path_to_photo.sort()

sounds = []

for i in zip(path_to_photo, path_to_sound):
    print(i)
    print(i[0])
    sound = SOUND(path_to_photo = i[0], path_to_sound = i[1])
    sounds.append(sound)

screen = p.display.set_mode((490, 835))

BACKGROUD = p.image.load('lab7\\assets\\bg.png').convert()
screen.blit(BACKGROUD, (0, 0))
sound_index = 0
sounds[0].sound.play()
sounds[0].placePhoto(screen)

while 1:
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
        if p.mouse.get_pressed()[0]:
            if 685.64 <= p.mouse.get_pos()[1] <= 755.81 and 215.3 <= p.mouse.get_pos()[0] <= 289.54:
                if sounds[sound_index].is_playing:
                    p.mixer.pause()
                    sounds[sound_index].is_playing = False
                else:
                    p.mixer.unpause()
                    sounds[sound_index].is_playing = True
            elif 98 <= p.mouse.get_pos()[0] <= 156 and 695 <= p.mouse.get_pos()[1] <= 756:
                p.mixer.stop()
                sound_index -= 1
                sounds[sound_index+1].is_playing = True
                if(sound_index == -1):
                    sound_index = len(sounds) - 1
                sounds[sound_index].sound.play()
                sounds[sound_index].placePhoto(screen)
            elif 355 <= p.mouse.get_pos()[0] <= 413 and 696 <= p.mouse.get_pos()[1] <= 757:
                p.mixer.stop()
                sound_index += 1
                sounds[sound_index - 1].is_playing = True
                if(sound_index == len(sounds)):
                    sound_index = -1
                sounds[sound_index].sound.play()
                sounds[sound_index].placePhoto(screen)

        
    p.display.flip()
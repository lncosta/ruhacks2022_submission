#Project by Luiza Nogueira Costa


import pygame
from pygame.locals import *
from pygame import mixer

import pygame_menu
from pygame_menu import Theme

scripts = [" Your name is Delilah.\n About a fortnight ago your beloved sister, Leah, fell mysteriously ill \n after going out to gather berries in the woods. \n The village from whence you hail is supersticious - there are talks of sorcery."
           "\n Your peers are too afraid to help. \n Your parents, both merchants, are too far North to come to your aid.  \n If you wish to see your sister live, you must take matters into your own hands."
           "\n According to the village crone, only the witch who dwells near the lakeside \n could offer thee any hope of salvation."
           "\n But she is but a legend, unseen for decades at this point."
           "\n And who is to say her heart is pure as to heed to your plight?"
           "\n Then again, Leah grows weaker by the hour."
           "\n Your heart breaks alongside her health."
            "\n\n And so, you make the decision to step into the forest deep."
    , "Spring has just begun to show its colors, \n so you put on your favorite dark woolen cloak \n and leather boots, \n praying it will not rain while you are out. \n To aid you on your journey, you pack some coffee, \n a variety of breads and cheeses, and your mother's hunting knife \n into your trusted satchel, a gift from your late grandmother. \n Wise beyond your years, you also ask the local apothecary for some medicinal herbs \n as well as a sewing needle and alcohol to clean any eventual wounds. \n One cannot be too careful, you think. \n They say the road is too dangerous for a girl to cross alone. \n\n Would you like to ask for help? ", "C", "D", "E"]

class Application:

    def __init__(self):
        self.run = True
        self.display_surf = None
        self.size = self.width, self.height = 1280, 720
        self.mouse_position = None
        self.menu_page = False
        self.clock = None
        self.background_color = (28, 68, 94)
        self.window_color = (250, 250, 250)

        self.dialogue_box_image = None
        self.button_color = (0, 161, 186)

        self.red_color = (183, 0, 31)
        self.green_color = (0, 118, 148)
        self.purple_color = (201, 199, 255)
        self.dark_purple_color = (121, 118, 206)
        self.white_color = (250, 250, 250)
        self.golden_color = (189, 107, 0)

        self.font = None

        self.current_text = "This is a text-based adventure game.\nUse the clues given to you through the dialogue to advance in the story. "
        self.current_text_index = -1

    def print_dialogue(self, text):
        text_list = []

        if type(text) == type([]):
            text_list.append(text)
        elif type(text) == type("string"):
            text_list = text.split("\n")
        else:
            raise ValueError("Wrong data type")

        dialog_font = pygame.font.Font(None, 35)
        width, height = dialog_font.size("l")

        line_height = -1

        for s in text_list:
            text_width, text_height = dialog_font.size(s)

            if text_height > line_height:
                line_height = text_height

        for count, s in enumerate(text_list):
            surface = dialog_font.render(s, True, (0, 0, 0))
            left = 135
            top = (line_height*count) + 50 + 80
            self.display_surf.blit(surface, (left, top), area = None)

    def process_init(self):
        pygame.init()
        self.display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.menu_page = True
        self.run = False
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 35) #Change font here
        mixer.init()
        mixer.music.load("bensound-ofeliasdream (1).mp3")
        mixer.music.play(-1)

        self.dialogue_box_image = pygame.image.load("Dialog Box.png").convert_alpha()


    def process_event(self, event):
        if event.type == pygame.QUIT:
            self.run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pressed = pygame.mouse.get_pressed()
            print("Mouse input:", mouse_pressed)
            if mouse_pressed[0] == 1:
                self.mouse_position = pygame.mouse.get_pos()

    def process_menu(self):

        font = pygame_menu.font.FONT_COMIC_NEUE
        myimage = pygame_menu.baseimage.BaseImage(
            image_path= "forest4.jpg",
            drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL
        )

        red_color = (183, 0, 31)
        green_color = (0, 118, 148)
        purple_color = (201, 199, 255)
        dark_purple_color = (121, 118, 206)
        white_color = (250, 250, 250)
        golden_color = (189, 107, 0)
        mytheme = Theme(background_color=myimage,
                        title_background_color=(0, 0, 0),
                        widget_font=font,
                        widget_font_size = 120,
                        title_font_color=golden_color,
                        title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_ADAPTIVE,
                        title_font_shadow=True,
                        widget_padding=(10, 30),
                        widget_background_color = None,
                       )


        menu = pygame_menu.Menu('Into The Forest Deep', 1280, 720, theme=mytheme)

        def disable():
            menu.disable()
            self.process_run()

        menu.add.button('Play', action = disable,  selection_effect=pygame_menu.widgets.LeftArrowSelection(), selection_color=purple_color, font_color = dark_purple_color, font_shadow = True)
        menu.add.button('Quit', pygame_menu.events.EXIT,  selection_effect=pygame_menu.widgets.LeftArrowSelection(), selection_color=purple_color, font_color =dark_purple_color,font_shadow = True)
        menu.mainloop(self.display_surf)

    def process_run(self):
        self.run = True
        self.menu_page = False

    def process_loop(self):
        pass
    def process_render(self):
        self.display_surf.fill(self.background_color)
        left = 75
        top = 50
        width = self.width - 150
        height = self.height - (50 * 3)
        window_rect = pygame.Rect(left, top, width, height)
        self.dialogue_box_image = pygame.transform.scale(self.dialogue_box_image, (width, height))
        #pygame.draw.rect(self.display_surf, self.window_color, window_rect)
        self.display_surf.blit(self.dialogue_box_image, window_rect)

        #Button creation:

        button_width = 100
        button_height = 36
        left = int(self.width/2) - int(button_width/2)
        top = int(self.height/1.12)

        next_rect = pygame.Rect(left, top, button_width, button_height)
        text_rect = pygame.Rect(left + 25, top + 8, button_width, button_height)
        pygame.draw.rect(self.display_surf, self.dark_purple_color, next_rect)
        surface = self.font.render("Next", True, self.purple_color)
        self.display_surf.blit(surface, text_rect)

        self.print_dialogue(self.current_text)

        #Check for button click:
        if not self.mouse_position == None:
            button_click = next_rect.collidepoint(self.mouse_position[0], self.mouse_position[1])
            self.mouse_position = None
            if button_click == 1:
                self.current_text_index += 1
                if self.current_text_index >= len(scripts):
                    self.current_text_index -= 1
                self.current_text = scripts[self.current_text_index]

        pygame.display.flip()
        pass
    def process_cleanup(self):
        pygame.quit()

    def process_execute(self):

        if self.process_init() == False:
            self.run = False


        while(self.run or self.menu_page):
            self.clock.tick(40)

            if self.menu_page == True:
                self.process_menu()

            for event in pygame.event.get():
                self.process_event(event)
            self.process_loop()
            self.process_render()

        self.process_cleanup()


if __name__ == '__main__':
    thisApplication = Application()
    thisApplication.process_execute()





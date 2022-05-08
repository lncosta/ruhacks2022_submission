#Project by Luiza Nogueira Costa
#For RUHACKS 2022
#March 6th - 8th 2022


import pygame
from pygame.locals import *
from pygame import mixer

import pygame_menu
from pygame_menu import Theme

scripts = [
#0
    " Your name is Delilah.\n About a fortnight ago your beloved sister,  affectionately nicknamed Leah,\n fell mysteriously ill after going out to gather berries in the woods. \n The village from whence you hail is supersticious - there are talks of sorcery."
           "\n Your peers are too afraid to help. \n Your parents, both merchants, are too far North to come to your aid.  \n If you wish to see your sister live, you must take matters into your own hands."
           "\n According to the village crone, only the witch who dwells near the lakeside \n could offer thee any hope of salvation."
           "\n But she is but a legend, unseen for decades at this point."
           "\n And who is to say her heart is pure as to heed to your plight?"
           "\n Then again, Leah grows weaker by the hour."
           "\n Your heart breaks alongside her health."
            "\n\n And so, you make the decision to step into the forest deep."
#1 - Choice A
    , " Spring has just begun to show its colors, \n so you put on your favorite dark woolen cloak \n and leather boots, \n praying it will not rain while you are out. \n To aid you on your journey, you pack some coffee, \n a variety of breads and cheeses, and your mother's hunting knife \n into your trusted satchel, a gift from your late grandmother. \n Wise beyond your years, you also ask the local apothecary for some medicinal herbs \n as well as a sewing needle and alcohol to clean any eventual wounds. \n One cannot be too careful, you think. \n They say the road is too dangerous for a girl of but twenty and fair to cross alone. \n\n Would you like to ask for help? "
#2
    , " With how unwilling to help the rest of your neighbors already proved themselves  \n to be, you decide not to risk involving someone else in this quest. \n You only have yourself to trust, right? \n Right. \n With your preparations done, you bid farewell to your sister, \n wishing her well. She gives you a golden brooch as a token of protection \n - it makes your fingertips tingle. \n You head eastward towards the forest. \n\n Though you have lived here all your life, this is unknown territory to you. \n The trees and soft grass, plus the faint birdsong in the distance, are friendly enough - \n but you cannot help but feel like someone is watching you wherever you go. \n How peculiar."
#3 - Choice B
    , " You stroll past a clearing where a pack of wolves rests idly in the shade. \n You notice that by their side there are quite a few tree branches, which could \n be useful later down the line. \n However, moving any closer might cause the animals to attack, \n and you are not sure if you are fast enough to run from them. \n\n What to do?"
#4 - Branch from 3, got torch
    , " With feather-light steps and an immesurable amount of caution, \n you manage to come close enough to the pack to gather some of the branches. \n You tie them to the side of your bag with a piece of yarn. \n Sometimes the risk pays off. \n\n You keep on moving foward. "
#5 - Branch from 3, did not get torch
    ," \n Too much of a gamble, you decide, especially with those twigs for legs. \n Hopefully the night isn't too cold nor too dark \n - you might not find any more materials for a fire, as it starts to drizzle. \n\n You keep on moving foward."
#6
    , " You swear you hear the sound of fabric rustling against the grass as you walk. \n Alas, when you turn to glance over your shoulder, there is nothing there. \n It was just a bird, you think. \n Or maybe a fox lost on its way home. \n Nothing that would ever harm you, surely. \n Dwelling on the matter makes your palms sweat \n hence, despite your concerns, you lift up your chin and keep on going. \n\n You hope Leah can at least sleep well while you are away."
#7 - Choice C
    , " About an hour into your walk, you come across a great oak tree. \n  Its roots are covered in moss, luscious and fragrant, \n and on the damp ground close by grow a variety of mushrooms familiar to you. \n Your father has been taking you foraging for these ever since your infancy \n - you'd be daft not to gather some. \n Problem is, either due to nevers or something else entirely, \n you do not feel as confident in your memory as you'd like. \n Every good villageperson knows not to eat the wrong kind of these, \n lest they die rather painfully. \n\n Which mushrooms do you pick? "
#8 - Got Red
    , " Red and white makes for a deadly combination. \n\n Who is to say that is not an advantage under the right circumstances? \n Onwards!"
#9 - Got purple
    , " Though the purplish goo that falls from it might seem suspicious, \n you are 99% sure eating this won't make your ears fall off... \n\n ... Maybe 95% sure, actually. Oh well - onwards!"
#10 - Choice D
    , " You make it to the mountainside cliffs. \n From what the crone told you, you must cross to the other side \n in order to reach the witch's cottage in its alleged location. \n There is a narrow tunnel that supposedly leads to the other side, \n left behind by the old miners, \n but the path is too dark as it is. \n The only other way would be to try and climb the rock. \n\n Which would you like to try?"
#11
    , " The tunnel is rightfully terrifying - full of rabid bats and creatures \n whose milky-yellow eyes stare at you from beneath the rocks. \n Luckily, with the branch you acquired before and a bit of fabric \n and oil from your inventory, you managed to make a torch. \n The blinding light seems to have kept you away from harm. \n You reach the other side of the mountains to find the sky of the early afternoon. \n\n Triumphant, you now stride with confidence. "
#12 - Choice E

    , " After walking for at least another three hours without anything eventful to note, \n it comes the time to make your way across the river. \n Like the old fairytales, you find a goblin keeping guard - \n the water is too violent, and the way around would take weeks, \n so your only chance at traversing is to persuade them to let you through. \n 'Thou must pay thy fares to cross, foul human', says the small and wrinkly creature. \n 'Twenty coins of silver at the least'. \n What little money you have is scarcely enough, \n but folklore says they only need a fair trade. \n Mushrooms might suffice, perhaps so will the cheese you packed. \n\n Which will you part with?"
#13
    , " Your love for your sister knows no bounds \n - even sending a somewhat innocent critter to its untimely end. \n 'Oh, yes', drawls the gobling 'These are delicious! Thou may cross safely, child'. \n The good part of your conscience prays they have a strong stomach \n to deal with the poison or bitter taste, whatever may be. \n Are goblins immune to it? You can't tell. \n\n Either way, you at last reach the creek that is the most to the East. \n A cottage made of rocks and glass lies in sight."

#14
    ," With how terrified your peers seemed to be of this Witch of the Forest, \n you are quite surprised once you make her acquaintance. \n She is neither too thin nor too tall, with no green skin or hairy warts to speak of, \n and from her dimpled smile and ashy-brown curls dusted with powder, \n you cannot think her much older than you. \n She sits in a rocking chair by the porch of her home, a golden pup curled on her lap. \n\n You clear your throat to catch her attention."

#15
    , " She smiles upon noticing you. \n 'I have been expecting you', she says with something akin to fondness in her tone, \n 'So great have been the trials you have faced, \n I was fraid the kettle would run cold. Follow me inside.' \n Though you have no real reason to trust her, determination leads you \n to do as she wishes. \n There is a ligthness to her movements - almost ghost-like, or even similiar to a fairy. "

#16
    , " The interior of the cottage is a lot more comfortable than you had imagined. \n She invites you to take a seat by the hearth. \n 'A little bird has told me all about the troubles with your sister. Poor Leah', \n she drawls in a way that paints sincereness. \n 'I am so sorry to hear she has fallen ill.' \n\n You are quick to ask: 'Can you heal her?', \n\n 'Oh, no, darling. I have no notion how to. But I am sure that you do, don't you?' \n You pause, perplexed, until something clicks into place. \n\n 'She never brought back any berries from her trip, did she? \n And only her close friends ever call her Leah.' \n\n She nods solemly. \n 'We were close - she was my apprentice.' "
#17
    , " You can only imagine how terrified she is that the rest of the town will discover this. \n They will condemn her of sorcery, of abandoning the good path; \n even if she survives, no one will ever extend her a kind hand again. \n 'What happened exactly? You must tell me if I am to solve this mess', \n comes your demand, a little angry. \n The Witch sighs deeply, \n 'To draw powers from these woods binds you to them. \n The taslisman you carry is proof of her connection'. \n You take the brooch from your pocket and realize it has grown warm \n beyond the explainable by simple science. \n The Witch pulls from her own robes a copy of the talisman, made in silver.  \n\n 'She must remain here or have her energy pulled from her. \n Even I cannot leave past the edge of the river for longer than an hour'. "

#18 - Choice F
    , " A cold feeling crawls up your spine, like fear injected into your veins. \n 'Can this connection be severed? Even if at the cost of her magic?' \n Surely what was learnt can be undone, you think. \n The Witch gives the suggestion a long and poignant consideration. \n 'If it was not so strong already, it might work. I cannot stomach the alternative.' \n Truth is, you do not feel qualified to choose for her, so you trace \n the metal curves of the brooch with your thumbs and chew the inside of your cheek. \n 'And can it be transferred to another?', you eventually ask. \n Your companion looks at you in sheer wonderment. \n\n 'Would you be willing to do so?' "

#19 - Choice G
    ,  " 'Gladly', repeats the Witch. 'And they call us heartless.' \n The weight of your decision hangs upon the both of you for a moment. \n 'It will be a while before she may attempt to visit. Can you bear the lack of goodbyes?' \n Deep down you know the question is rhetorical - there is no other choice to be made. \n 'For her sake, yes', you reply. \n Rain pours down with a fervor now, prattling agaisnt the windows \n and the ceramic tiles of the roof. \n 'You know, there is no need to be lonely', the Witch then continues, \n 'I would be happy to teach you as I did to her. Besides, I could use the conversations.' \n\n One one hand, she is a stranger. But likely just as lonely as you are. \n Would you like to stay?"

    , "The End!"]


bad_ending_A_1 = "You decide to call for Martha, the butcher's girl. \n Although kind and mild-tempered, her skills with a blade are unmatched \n and her spirits are strong, \n which you assume might be useful when braving the dangers that lie ahead. \n With the encouragement of coin, Martha is only too happy to accompany you. \n You start your adventure with some light chatter and a sense of companionship. \n However, about two hours in, you come face-to-face with a bear. \n In a panic, Martha decides to attack it with the butterknife you brought for the jam. \n Needless to say, you are no match to the power of nature. \n\n Better to go alone than ill-accompanied, so goes the wisdom of the day. "
choice_A = ["Call for aid", "Go alone"]

choice_B = ["Risk it", "Leave it be"]

choice_C = ["Roundish Red", "Sickly Purple"]

choice_D = ["Climb Up", "Walk Through"]

choice_E = ["Cheeses", "Mushroom"]

bad_ending_D_1 = " Curse the gods of rain! \n You manage to make it about halfway up the cliff before your hand slips. \n From so high up, the path downwards is not too kind on the bones. \n\n Foolishness has its price, dear girl."
bad_ending_D_2 = " Though a tunnel such as this might be safe enough to cross, that assumes one thing: \n That you can see where you are going. \n Without any wood for a torch, you are left to wander in the pitch darkness, \n and eventually no amount of caution can save you \n from tripping on the gravel \n and falling down one of the abandoned coal pits. \n Yours will make for a spooky skeleton for other adventurers to find. \n\n Be wary of your surroundings next time."


bad_ending_E_1 = " 'Does thou take me for a fool, girl?!', spits the goblin in a roaring tone. \n 'Never shall thou cross! Begone, or thou will meet thy end by my crossbow!' \n\n There are times when kindness does not take you far."

choice_F = ["Never", "Gladly"]

bad_ending_1 = " Not all of us are, nor should be, selfless in all the matters of our lives. \n Though it breaks your heart to admit it, \n your sister's freedom could not come at the cost of yours. \n Your misery would be too grand. \n The Witch sobs aloud at your decision, but you make your way back to the village\n  with a basket of berries and a clear mind. \n\n Your sister is so very glad to see you return home safe and sound. \n\n What comes to pass in the future is out of your hands - and you're content with it. "

choice_G = ["No", "Yes"]

ending_2 = " Though she seems like a loving soul, you were always a lone wolf. \n\n You continue your journey into the forest deep, learning from the trees and the birds \n your own kind of primeval magic. \n Missing your home is a small price to pay for the freedom you have gained. \n \n Whenever the darkness scares you, you think of Leah, and all is right again. "

ending_3 = " 'Yes', you reply after a moment of consideration, 'I think I would like that'. \n The Witch's face lights up. \n 'Oh, but I am glad! Come, come - let us have some tea. \n Tomorrow we shall commence your lessons!' \n\n A month later and your sister regains her strength steadily. \n She sends you letters and gifts delivered by crows, \n as well as warm regards from your parents. \n\n You once feared you'd be alone in the forest deep - but you aren't. \n \n Not at all.  "

class Application:

    def __init__(self):
        self.run = True
        self.display_surf = None
        self.size = self.width, self.height = 1280, 720
        self.mouse_position = None
        self.menu_page = False
        self.clock = None
        #self.background_color = (28, 68, 94)
        self.background_color = (0, 55, 41)
        self.window_color = (250, 250, 250)

        self.dialogue_box_image = None
        self.game_over_image = None
        self.button_color = (0, 161, 186)

        self.red_color = (183, 0, 31)
        self.green_color = (0, 118, 148)
        self.purple_color = (201, 199, 255)
        self.dark_purple_color = (121, 118, 206)
        self.white_color = (250, 250, 250)
        self.golden_color = (189, 107, 0)

        self.font = None

        self.current_text = " This is a text-based adventure game.\n Use the clues given to you through the dialogue to advance in the story.  \n There is no looking back, so pick carefully. \n\n And remember: it all comes back to you."
        self.current_text_index = -1

        self.game_state = "start"

        #Game booleans:

        self.picked_up_rope = False;
        self.got_torch = False;
        self.got_red_mushroom = False;

    def print_dialogue(self, text):
        text_list = []

        if type(text) == type([]):
            text_list.append(text)
        elif type(text) == type("string"):
            text_list = text.split("\n")
        else:
            raise ValueError("Wrong data type")

        dialog_font = pygame.font.Font(None, 34)
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
        self.font = pygame.font.Font(None, 30) #Change font here
        mixer.init()
        mixer.music.load("bensound-ofeliasdream (1).mp3")
        mixer.music.play(-1)

        self.dialogue_box_image = pygame.image.load("dialogue_box3.png").convert_alpha()


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

        font = pygame_menu.font.FONT_BEBAS
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
                        title_font = pygame_menu.font.FONT_OPEN_SANS_ITALIC,
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

    def set_game_state(self):
        if self.current_text_index >= len(scripts):
            self.current_text_index -= 1
            self.current_text = scripts[self.current_text_index]

        elif self.current_text_index == 1:
            self.game_state = "choice_A"
            self.current_text = scripts[self.current_text_index]
        elif self.current_text_index == 3:
            self.game_state = "choice_B"
            self.current_text = scripts[self.current_text_index]
        elif self.current_text_index == 7:
            self.game_state = "choice_C"
            self.current_text = scripts[self.current_text_index]
        elif self.current_text_index == 10:
            self.game_state = "choice_D"
            self.current_text = scripts[self.current_text_index]
        elif self.current_text_index == 12:
            self.game_state = "choice_E"
            self.current_text = scripts[self.current_text_index]
        elif self.current_text_index == 18:
            self.game_state = "choice_F"
            self.current_text = scripts[self.current_text_index]
        elif self.current_text_index == 19:
            self.game_state = "choice_G"
            self.current_text = scripts[self.current_text_index]
        else:
            self.game_state = "normal"
            self.current_text = scripts[self.current_text_index]

    def process_render(self):
        if self.game_state == "end screen" or self.game_state == "end screen 2":
            self.game_over_screen()
            return
        self.display_surf.fill(self.background_color)
        left = 25
        top = 20
        width = self.width - 60
        height = self.height - (40 * 3)
        window_rect = pygame.Rect(left, top, width, height)
        self.dialogue_box_image = pygame.transform.scale(self.dialogue_box_image, (width, height))
        self.display_surf.blit(self.dialogue_box_image, window_rect)

        #Button creation:

        button_width = 100
        button_height = 36
        left = int(self.width) - int(button_width/2) - 150
        top = int(self.height/1.12)

        next_rect = pygame.Rect(left, top, button_width, button_height)
        text_rect = pygame.Rect(left + 25, top + 8, button_width, button_height)
        surface = self.font.render("Next", True, self.purple_color)

        self.print_dialogue(self.current_text)

        state = "Not"
        #Choices:

        button_width = 200
        left = int(self.width) - int(button_width / 2) - 900
        top = int(self.height / 1.12)

        next_rect_A = pygame.Rect(left, top, button_width, button_height)
        text_rect_A = pygame.Rect(left + 25, top + 8, button_width, button_height)

        next_rect_B = pygame.Rect(left + 500, top, button_width, button_height)
        text_rect_B = pygame.Rect(left + 500 + 25, top + 8, button_width, button_height)

        if self.game_state == "choice_A":

            pygame.draw.rect(self.display_surf, self.dark_purple_color, next_rect_A)
            surface = self.font.render(choice_A[0], True, self.purple_color)
            self.display_surf.blit(surface, text_rect_A)

            pygame.draw.rect(self.display_surf, self.dark_purple_color, next_rect_B)
            surface = self.font.render(choice_A[1], True, self.purple_color)
            self.display_surf.blit(surface, text_rect_B)
            state = "choosing"
        elif self.game_state == "choice_B":

            pygame.draw.rect(self.display_surf, self.dark_purple_color, next_rect_A)
            surface = self.font.render(choice_B[0], True, self.purple_color)
            self.display_surf.blit(surface, text_rect_A)

            pygame.draw.rect(self.display_surf, self.dark_purple_color, next_rect_B)
            surface = self.font.render(choice_B[1], True, self.purple_color)
            self.display_surf.blit(surface, text_rect_B)
            state = "choosing"
        elif self.game_state == "choice_C":

            pygame.draw.rect(self.display_surf, self.dark_purple_color, next_rect_A)
            surface = self.font.render(choice_C[0], True, self.purple_color)
            self.display_surf.blit(surface, text_rect_A)

            pygame.draw.rect(self.display_surf, self.dark_purple_color, next_rect_B)
            surface = self.font.render(choice_C[1], True, self.purple_color)
            self.display_surf.blit(surface, text_rect_B)
            state = "choosing"
        elif self.game_state == "choice_D":

            pygame.draw.rect(self.display_surf, self.dark_purple_color, next_rect_A)
            surface = self.font.render(choice_D[0], True, self.purple_color)
            self.display_surf.blit(surface, text_rect_A)

            pygame.draw.rect(self.display_surf, self.dark_purple_color, next_rect_B)
            surface = self.font.render(choice_D[1], True, self.purple_color)
            self.display_surf.blit(surface, text_rect_B)
            state = "choosing"
        elif self.game_state == "choice_E":

            pygame.draw.rect(self.display_surf, self.dark_purple_color, next_rect_A)
            surface = self.font.render(choice_E[0], True, self.purple_color)
            self.display_surf.blit(surface, text_rect_A)

            pygame.draw.rect(self.display_surf, self.dark_purple_color, next_rect_B)
            surface = self.font.render(choice_E[1], True, self.purple_color)
            self.display_surf.blit(surface, text_rect_B)
            state = "choosing"
        elif self.game_state == "choice_F":

            pygame.draw.rect(self.display_surf, self.dark_purple_color, next_rect_A)
            surface = self.font.render(choice_F[0], True, self.purple_color)
            self.display_surf.blit(surface, text_rect_A)

            pygame.draw.rect(self.display_surf, self.dark_purple_color, next_rect_B)
            surface = self.font.render(choice_F[1], True, self.purple_color)
            self.display_surf.blit(surface, text_rect_B)
            state = "choosing"
        elif self.game_state == "choice_G":

            pygame.draw.rect(self.display_surf, self.dark_purple_color, next_rect_A)
            surface = self.font.render(choice_G[0], True, self.purple_color)
            self.display_surf.blit(surface, text_rect_A)

            pygame.draw.rect(self.display_surf, self.dark_purple_color, next_rect_B)
            surface = self.font.render(choice_G[1], True, self.purple_color)
            self.display_surf.blit(surface, text_rect_B)
            state = "choosing"
        elif self.game_state == "game over":
            state = "game over"
            pygame.draw.rect(self.display_surf, self.dark_purple_color, next_rect)
            self.display_surf.blit(surface, text_rect)
        elif self.game_state == "done":
            state = "end screen 2"
            pygame.draw.rect(self.display_surf, self.dark_purple_color, next_rect)
            self.display_surf.blit(surface, text_rect)

        else:
            pygame.draw.rect(self.display_surf, self.dark_purple_color, next_rect)
            self.display_surf.blit(surface, text_rect)
            self.game_state = "normal"


        #Check for button click:
        if not self.mouse_position == None:
            if state == "choosing" and self.game_state == "choice_A":
                button_click2 = next_rect_A.collidepoint(self.mouse_position[0], self.mouse_position[1])

                if button_click2 == 1:
                    self.current_text = bad_ending_A_1
                    self.game_state = "game over"

                button_click3 = next_rect_B.collidepoint(self.mouse_position[0], self.mouse_position[1])

                self.mouse_position = None
                if button_click3 == 1:
                    self.current_text_index += 1
                    self.set_game_state()
            elif state == "choosing" and self.game_state == "choice_B":
                button_click2 = next_rect_A.collidepoint(self.mouse_position[0], self.mouse_position[1])
                button_click3 = next_rect_B.collidepoint(self.mouse_position[0], self.mouse_position[1])

                self.mouse_position = None
                if button_click2 == 1:
                    self.got_torch = True;
                    print("Torch acquired.")
                    self.current_text_index += 1
                    self.set_game_state()
                elif button_click3 == 1:
                    self.got_torch = False;
                    self.current_text_index += 2
                    self.set_game_state()
            elif state == "choosing" and self.game_state == "choice_C":
                button_click2 = next_rect_A.collidepoint(self.mouse_position[0], self.mouse_position[1])
                button_click3 = next_rect_B.collidepoint(self.mouse_position[0], self.mouse_position[1])

                self.mouse_position = None
                if button_click2 == 1:
                    self.got_red_mushroom = True;
                    print("Red mushroom acquired.")
                    self.current_text_index += 1
                    self.set_game_state()
                elif button_click3 == 1:
                    self.got_red_mushroom = False;
                    print("Purple mushroom acquired.")
                    self.current_text_index += 2
                    self.set_game_state()
            elif state == "choosing" and self.game_state == "choice_D":
                button_click2 = next_rect_A.collidepoint(self.mouse_position[0], self.mouse_position[1])
                button_click3 = next_rect_B.collidepoint(self.mouse_position[0], self.mouse_position[1])

                self.mouse_position = None
                if button_click2 == 1:
                    print("Picked climb.")
                    self.current_text = bad_ending_D_1
                    self.game_state = "game over"
                elif button_click3 == 1:
                    print("Tried to walk.")

                    if self.got_torch == False:
                        self.current_text = bad_ending_D_2
                        self.game_state = "game over"
                    else:
                        self.current_text_index += 1
                        self.set_game_state()
            elif state == "choosing" and self.game_state == "choice_E":
                button_click2 = next_rect_A.collidepoint(self.mouse_position[0], self.mouse_position[1])
                button_click3 = next_rect_B.collidepoint(self.mouse_position[0], self.mouse_position[1])

                self.mouse_position = None
                if button_click2 == 1:
                    print("Picked cheese.")
                    self.current_text = bad_ending_E_1
                    self.game_state = "game over"
                elif button_click3 == 1:
                    print("Picked mushroom.")

                    if self.got_red_mushroom== False:
                        self.current_text = bad_ending_E_1
                        self.game_state = "game over"
                    else:
                        self.current_text_index += 1
                        self.set_game_state()
            elif state == "choosing" and self.game_state == "choice_F":
                button_click2 = next_rect_A.collidepoint(self.mouse_position[0], self.mouse_position[1])
                button_click3 = next_rect_B.collidepoint(self.mouse_position[0], self.mouse_position[1])

                self.mouse_position = None
                if button_click2 == 1:
                    print("Refused to stay.")
                    self.current_text = bad_ending_1
                    self.game_state = "done"
                    state = "done"
                elif button_click3 == 1:
                    print("Stayed.")
                    self.current_text_index += 1
                    self.set_game_state()
            elif state == "choosing" and self.game_state == "choice_G":
                button_click2 = next_rect_A.collidepoint(self.mouse_position[0], self.mouse_position[1])
                button_click3 = next_rect_B.collidepoint(self.mouse_position[0], self.mouse_position[1])

                self.mouse_position = None
                if button_click2 == 1:
                    print("On your own.")
                    self.current_text = ending_2
                    self.game_state = "done"
                    state = "done"
                elif button_click3 == 1:
                    print("With a friend.")
                    self.current_text = ending_3
                    self.game_state = "done"
                    state = "done"
            else:
                button_click = next_rect.collidepoint(self.mouse_position[0], self.mouse_position[1])
                self.mouse_position = None
                if button_click == 1:
                    if self.game_state == "game over":
                        self.current_text = "Game Over"
                        self.game_state = "end screen"
                        self.game_over_screen()
                    elif self.game_state == "done":
                        self.current_text = "The End!"
                        self.game_state = "end screen 2"
                        self.game_over_screen()
                    else:
                        if self.current_text_index == 4:
                            self.current_text_index += 1
                        elif self.current_text_index == 8:
                            self.current_text_index += 1
                        self.current_text_index += 1
                        self.set_game_state()

        pygame.display.flip()
        pass

    def game_over_screen(self):
        self.display_surf.fill(self.background_color)
        if self.game_state == "end screen":
            self.game_over_image = pygame.image.load("game_over_screen.png").convert_alpha()
        elif self.game_state == "end screen 2" :
            self.game_over_image = pygame.image.load("end_screen.png").convert_alpha()

        window_rect = pygame.Rect(0, 0, self.width, self.height)
        self.game_over_image = pygame.transform.scale(self.game_over_image, (self.width, self.height))
        self.display_surf.blit(self.game_over_image, window_rect)

        if not self.mouse_position == None:
            button_click = window_rect.collidepoint(self.mouse_position[0], self.mouse_position[1])
            self.mouse_position = None
            if button_click == 1:
                self.run = False
                self.process_cleanup()



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

            self.process_render()
            self.process_loop()

        self.process_cleanup()


if __name__ == '__main__':
    thisApplication = Application()
    thisApplication.process_execute()





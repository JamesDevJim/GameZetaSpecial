import serial
import pygame
pygame.mixer.init()

#SOUNDS
soundPregame = pygame.mixer.Sound("/home/pi/Puzzilist/Sounds/music_zapsplat_among_the_stars_no_piano.wav")
soundPrecheck = pygame.mixer.Sound("/home/pi/Puzzilist/Sounds/zapsplat_science_fiction_computer_voice_says_pre_checks_completed_30835.wav") 
soundDoorOpen = pygame.mixer.Sound("/home/pi/Puzzilist/Sounds/zapsplat_science_fiction_door_open_hiss_air_release_then_auto_motor_drome_44436.wav")
soundWelcome = pygame.mixer.Sound("/home/pi/Puzzilist/Sounds/zapsplat_science_fiction_computer_voice_says_welcome_30843.wav")
soundGamePlay = pygame.mixer.Sound("/home/pi/Puzzilist/Sounds/zapsplat_science_fiction_drone_large_cavernous_metallic_43232.wav")
soundSuccess = pygame.mixer.Sound("/home/pi/Puzzilist/Sounds/zapsplat_science_fiction_computer_voice_male_says_success_15858.wav")
soundIncomingMissile = pygame.mixer.Sound("/home/pi/Puzzilist/Sounds/zapsplat_science_fiction_computer_voice_male_says_warning_incoming_missle_15860.wav")
soundExplosion = pygame.mixer.Sound("/home/pi/Puzzilist/Sounds/zapsplat_warfare_missile_incoming_whizz_by_then_explosion_001_31162.wav")
soundData = pygame.mixer.Sound("/home/pi/Puzzilist/Sounds/zapsplat_science_fiction_data_stream_computer_41940.wav")
#Add other success sound. Add button sounds.-

#DISPLAY
    #Play a gray, slow-moving symbol for pregame screen
    #Play a green, slow-moving symbol for gameplay screen
    #Play a green, static symbol for success screen
    #play a red, slow-moving symbol for fail screen
#screen = pygame.display.set_mode((200,200))
#pygame.display.update()

while True:      #Main Loop
    soundPregame.play()

    ser = serial.Serial('/dev/ttyACM0',9600)
    y = int(ser.readline())
    
    print("Push any button to begin.")

    x = input("Start Game? (y/n): ")     
    

    if x == 1 or 2:
        pygame.mixer.stop()
        pygame.mixer.Channel(0).play(soundPrecheck)#How to write a loop that will play three consecutive sounds. Queue only holds one wave file.
        #pygame.mixer.Channel(0).queue(soundDoorOpen)
        #pygame.mixer.Channel(0).queue(soundWelcome)
        pygame.mixer.Channel(0).queue(soundGamePlay)        
        #x = input("Select Wrong or Right anwser(w/r): ")          
        print("Select Blue or Yellow to determine your fate.")
        ser = serial.Serial('/dev/ttyACM0',9600)
        x = int(ser.readline())
#        return
    if x == 1:
        #stop_wait_sound
        pygame.mixer.stop()
        soundSuccess.play()
        print ("\n"*20)
        print("You Win!!!!")
        break
#    else:
#        print("Incorrect Entry")

    if x == 2:
        pygame.mixer.stop()
        pygame.mixer.Channel(0).play(soundIncomingMissile)
        pygame.mixer.Channel(0).queue(soundExplosion)
        print ("\n"*20)
        print("You Lose.")
        break
#    else:
#        pygame.mixer.music.load(pregame_Sound)
#        pygame.mixer.music.play()
#        return
    

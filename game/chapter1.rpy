label chapter1: #label this .rpy file to it can be easy to call it in the script.rpa
stop music fadeout 2.0 #stop the music when loading to the game
play music t2 #play sayori theme
scene bg residential_day #set the scene to house
with dissolve_scene_full #black the screen slowlly

$ s_name = "sayori" #change the s_name to sayori
$ y_name = "yuri" # change y_name to yuri name
$ m_name = "Monika"# change m_name to monika
$ n_name = "Natsuki"#changeN_name to Natsuki
$ restore_all_characters()
#show sayori sprite at 2b in zoom order 2 at pose 11 
show sayori 1b zorder 2 at t11 
s "Hey [player] there's a new kid in the club." #sayori saying hey to the player name
mc "There's Sayori." #mc talking
"I didn't know we had a new student." #mc talking inside his head
s "Yes really" #sayori say yes really
mc "Cool what's her name?" # mc talking
s "Just wait and you will see" #sayori talking
"Then lets go to the club" #mc talking in his head
show bg club_day  # show the club room day
with wipeleft_scene # wipe the scene to the left
stop music fadeout 2.0  # stop the music and fade out
play music t3 #Play music
show sayori 2b zorder 2 at t11 # show sayori sprite

s "Hey Monika, hey Yuri, and hey Natsuki" # sayori speak
hide sayori  # hideing sayori sprite
#show sayori sprite to 2b becuse i don't know what pose to give to her model t11 mean tranlation then where you see the charctor appear
show monika 3b zorder 2 at t11 
m "Hey Sayori" # monika say hi to sayori
#show monika at 3b and zoom 2times at translation 11
hide monika # hide monika sprite
show yuri 1b zorder 2 at t11 
y "Hi Sayori" #yuri say hi to sayori
#show yuri at 1b zoom 2 rtimes at translaton 11
hide yuri  # hide yuri sprite
show natsuki 1b zorder 2 at t11
n "Hello Sayori" #natsuki say hi
#show natsuki at 1b zom 2 at translation 11
hide natsuki  #hide Natsuki sprite
mc "Hi everyone, I heard we have a new student in the club?" # Main Charactor say hi to every girl in the club
show monika 1b zorder 2 at t11 # show monika sprite
m "Hey [player] how's your day going?" #mc being nice to monika
mc "I'm having a good day today Monika, Thanks for asking" #monkia being a simp to the player
mc ":)" #MC do a smile face becuse MC have a crush on Monika lol
m "That's good to hear" # Monika Talking
m "And today we have a new student in the club" # Monika Talking
hide monika # hide monika cute sprite lol
show natsuki 1b zorder 2 at t11 #show mad natsuki
n "I should make some cupcakes for the new student then" #Natsuki being nice for some reson
hide natsuki # hide natsuki cute sprite
show yuri 1b zorder 2 at t11  #show curse yuri
y "I'll go get the tea" # yuri not being wired
hide yuri # hide yuri 
scene bg club_day #set the scene club day 
with wipeleft_scene #wipe the scene to the left

menu: #let the player control the story
    mc "Who should I help?" # mc talking to him self asking who he will help
    "Make Tea": #menu name
        $ options = True # bool statement
    "Make Cupcakes": # menu name 2
        $ options = False #bool statement

if  options: #if statement
        "I will help Yuri with the tea" #TODO for TigerClips1 add yuri sprite where match with the story so yay for me AAAAAAAAAAAAAAAAAA                  #Todo comeplate natsuki sprite for all the lines for the cupcake/ add yuri sprite fix spelling error and add yuri tea lines tomorrow
        play music t6 #play music
        scene bg club_day # set the scene to club day
        mc "Hey Yuri can I help you with the tea?" #MC being nice to yuri
        show yuri 1e zorder 2 at t11 # show yuri sprite
        y "Sure [player] this tea will get done faster if more people help out" #Yuri's text will change in the future to be like the Original Yuri for ddlc
        hide yuri # hide yuri
        "Great can't wait to help" #spelling error fix thanks to Kwhitehead07/Blackdeath
        show yuri 1b zorder 2 at t11 #show yuri
        y "I will need you to use the school's auto tea maker 3,000"
        hide yuri # hide yuri
        show yuri 1b zorder 2 at f32 #show yuri
        y "..." #stright face
        hide yuri #hide yuri sprite
        show yuri 1b zorder 2 at t11 # show yuri
        y "Hehe" #yuri acting weird
        hide yuri #hide yuri sprite
        mc "Tea maker what now?" #MC being a boomer
        show yuri 1b zorder 2 at t11 #show yuri
        y "It's just a joke [player]" #yuri being a boomer too
        hide yuri #hide yuri sprite
        mc "Oh " #MC being stupid
        mc "..." #MC doing a stright face
        "And now we wait  until the tea get's done." #Mc talking
        "Then we put the tea in the glass cup." #MC being born lol jk
        show yuri 1b zorder 2 at t11 #show yuri
        y "Tea smells good ahaha" #yuri acting wired like she was in DDLC OG game
        hide yuri #hide yuri sprite
        mc "What's so funny?" #MC being confuse
        show yuri 2b zorder 4 at t11 #shwing yuri sprite
        y "Nothing [player]" #yuri being sus
        stop music # stop the music to scare the player hehe
        hide yuri #hide yuri
        "Yuri acting odd reminds you when something happened a long time ago when Yuri did something that was gross and terrifying but you can't remember what it was." #MC being reminded of something that happen in act 2 of ddlc
        play music t6 #Play the music
        show yuri 1b zorder 2 at t11 #show yuri
        y "Hehehehe" #yuri being weird
        hide yuri #hide yuri sprite
        show yuri glitch2 zorder 2 at t11 #show yuri glitch from to spook the player
        play music t6g #play glitch music
        play sound g5 #play glitch sound breaking the 4th wall
        y '¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéê'#Monika hack yuri lol (this is reminding of og ddlc but there will only be one encounter like this till later)
        stop sound #stop the scary sound

        stop music  #stop the glitch music
        play music t6 #play normal music

        hide yuri #hide yuri sprite
        mc "Okay Yuri" #mc not being weird
        show yuri 1b zorder 2 at t11 #show yuri
        y "That's all thank's for helping [player]" #yuri being nice
        hide yuri #hide yuri sprite
        mc "No problem"  #mc being smart
        scene bg club_day #change the scene to club room day
        with wipeleft_scene #wipe the scene to the left
        stop music fadeout 2.0 #stop the music
        play music t5 #play okay everyone music
        
        #yuri lines are done just need add few fixes then it will look good
else:  #else this will happening when you click the 2 options 
        "I will help Natsuki with the cupcakes"
        show natsuki 1l zorder 2 at t11 #show natsuki sprite
        play music t5 #play music 
        scene bg club_day # change the scene to bg day
        mc "Can I help you with the cupcakes Natsuki?" #MC being random
        n "Sure but you have to follow my instructions" #change this later to make natsuki bit mad
        show natsuki 1l zorder 2 at t11 #show natsuki sprite
        hide natsuki #hide natsuki sprite
        "Time to Have some fun" # MC talking to the player 4th wall breaking
        show natsuki 1b zorder 2 at t11 #show natsuki sprite
        n "Alright we need to make some cake, flour, eggs, sugar, salt, milk or water works, and some oil too"#i google this
        hide natsuki#hide natsuki sprite
        mc "Alright I'll go get that." #Mc talking
        show natsuki 1a zorder 2 at t11 #show natsuki sprite
        n "Okay thank you" #natsuki talking
        hide natsuki#hide natsuki sprite
        show natsuki 1b zorder 2 at t11 #show natsuki sprite
        n "And I need a pan that's square"#natsuki talking
        hide natsuki #hide natsuki sprite
        show natsuki 1b zorder 2 at t11 #show natsuki sprite
        n "And the temperature need's to be up to 350 degrees"#google this
        hide natsuki  #hide natsuki spirte
        show natsuki 1b zorder 2 at t11 #show natsuki spirte
        n "So we can bake this cupcake for the new student" #natsuki being nice
        hide natsuki #hide natsuki sprite
        mc "Okay it's done" #mc talking
        mc "Cake look so good and Natsuki added cat ears as the icing" #mc talking
        show natsuki 1b zorder 2 at t11 #show natsuki sprite
        n "Alright we're done with the cake thanks to [player] for helping"  #natsuki being nice
        hide natsuki  #hide natsuki sprite
        scene bg club_day #set the scene to club room day
        with wipeleft_scene #wipe the scene to the left
        
        
if options == True: #if the player click to help yuri with the tea
    show yuri 1b zorder 2 at t11 #show yuri sprite
    y "Tea's done thanks to [player]" #it will say this if the player chose help yuri with tea
    hide yuri #hide yuri sprite
    mc "I'm happy to help" #mc talking
else: #else if the player chose cupcakes then sayori will help yuri with the tea
    show yuri 1b zorder 2 at t11 #show yuri sprite
    y "Tea is done thanks to Sayori" #if the player did not help yuri with the tea then she will say this
    hide yuri #hide yuri sprite
    show sayori 1b zorder 2 at t11 #show sayori sprite
    s "It was fun" #sayori talking
    hide sayori #hide sayori sprite
if options == False: #if the player click cupcakes then natsuki will thank the player
    show natsuki 1b zorder 2 at t11 #show natsuki sprite
    n "Cupcakes are done thanks to [player]" #natsuki being nice
    hide natsuki #hide natsuki sprite
    mc "I'm happy to help" #player talking
else: #else if the player click tea then sayori will help natsuki with the cupcakes
    show natsuki 1b  zorder 2 at t11  #show natsuki sprite
    n "Cupcakes are done thanks to Sayori" #natsuki being nice may change
    hide natsuki   #hide natsuki sprite
    show sayori 1b zorder 2 at t11 #show sayori sprite
    s "I've learned so much about baking thanks for letting me help out!" #sayori being sayori
    hide sayori #hide sayori sprite

stop music fadeout 2.0 #fadeout the music
play music t3 #play music
show monika 3a zorder 3 at t11 #show monika sprite
m "Good job everyone!" #monika being monika
hide monika #hide monika sprite 
"The new club member is here " #mc see the new  club member
 
with wipeleft_scene #wipe the scene to the left
return # exit

label chapter1_page2: #enable chapter1_page2
scene bg club_day #set the scene to club room day
play music  t3 #play music
#TODO wait until the artist complete ironmouse art then add her art to the definitions.rpy 
m "The new student is here guys"
m "Get ready guys"
mc "Okay"
s "Let's go"
y "Ok"
n "Alright"
"Its cool how all the girls in the club did this just for the new student"
i "Ummm he-hello?"
s "Hey there new kid!"
s "Welcome to the literature club! My name is Sayori!"
n "I hope this girl isn't a manga hater."
y "Uhm, hi there"
m "I hope you enjoy it here, my name is monika, let me introduce everyone"
m "so that right there is [player]"
mc "Hello there"
m "And that there is yuri"
y "H-hello"
m "And here is natsuki, try not to anger her though."
n "You like manga?"
i "Yeah I do actually, I like this one called Dragon Ball Volume 1"
m "But manga isn't even literature"
n "But manga is liturature!"
i "Yeah I agree"
m "Fine, if you say so"
m "Anyways, what's your name?"
i "My name is Ironmouse"
$ i_name = "Ironmouse"
m "Strange name, but hello there Ironmouse!"
s "Hey Ironmouse! Nice to know you name finally!"
y "Hi Ironmouse"
n "Hello there Ironmouse, don't get into trouble around here!"
mc "Nice to meet you Ironmouse"
i "Hello everyone, nice to know you guys!"
m "Alright so, let me explain what we do daily"
m "All you need to do is write a unique poem, read books for ideas and such"
"Very lovely day we are having right [player]?" #random 4th wall break
m "We bake cupcakes, make tea, mostly basic stuff"
m "Speaking of which, its about time we write a poem, so if you don't know what to do today we'll run you through it"
i "Okay"
$ renpy.movie_cutscene("mod_assets/video/1.ogx") #set a movie scene from spongebob a few moments later
return #exit

#Todo for  blackdeath5h  add story line for ironmouse Please Keep it PG 13 make it connect the story lines Kwhitehead07 put and TigerClips1 Put
label chapter1_page3:















#end of Blackdeath5h story lines
return

#To Do for TigerClips1 add the menu and add the story line for the all 6 charactor
label chapter1_page4:





































#END of lines for TigerClips1
return

#TODO for lylly not found
label chapter1_page4_part_2:







































return

#End Of Chaptor 1

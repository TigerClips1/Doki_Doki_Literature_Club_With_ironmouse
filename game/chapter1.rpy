label chapter1: #label this .rpy file to it can be easy to call it in the script.rpa
# let say i'm done with this code  have to hit ctral s to save it
stop music fadeout 2.0 #stop the music when loading to the game
play music t2 #ply sayori thame
scene bg residential_day #set the scene to house
with dissolve_scene_full #vlack the screen slowlly

$ s_name = "sayori" #change the s_name to sayori
$ y_name = "yuri" # change y_name to yuri name
$ m_name = "Monika"# change m_name to monika
$ n_name = "Natsuki"#changeN_name to Natsuki
$ restore_all_characters()
#show sayori sprite at 2b in zoom order 2 at pose 11 
show sayori 1b zorder 2 at t11 
s "Hey [player] there's a new kid in the club." #sayori saying hey to the player name
mc "There's Sayori." #mc talking
"I didn't know we had a new student." #mc talking in his head
s "Yes really" #sayori say yes really
mc "Cool what's her name?" # mc talking
s "Just wait and you will see" #sayori talking
"Then lets go to the club" #mc talking in his head
show bg club_day  # show the club room day
with wipeleft_scene
stop music fadeout 2.0 
play music t3
show sayori 2b zorder 2 at t11 

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
show monika 1b zorder 2 at t11
m "Hey [player] how's your day going?"
mc "I'm having a good day today Monika, Thanks for asking"
mc ":)"
m "That's good to hear"
m "And today we have a new student in the club"
hide monika
show natsuki 1b zorder 2 at t11
n "I should make some cupcakes for the new student then"
hide natsuki
show yuri 1b zorder 2 at t11 
y "I'll go get the tea"
hide yuri
scene bg club_day
with wipeleft_scene

menu: #let the player control the story
    mc "Who should I help?" # mc talking to him self asking who he will help
    "Make Tea":
        $ options = True
    "Make Cupcakes":
        $ options = False

if  options: #if statement
        "I will help Yuri with the tea" #TODO for TigerClips1 add yuri sprite where match with the story so yay for me AAAAAAAAAAAAAAAAAA                  #Todo comeplate natsuki sprite for all the lines for the cupcake/ add yuri sprite fix spelling error and add yuri tea lines tomorrow
        play music t6
        scene bg club_day
        mc "Hey Yuri can I help you with the tea?"
        show yuri 1e zorder 2 at t11
        y "Sure [player] this tea will get done faster if more people help out" #Yuri's text will change in the future to be like the Original Yuri for ddlc
        hide yuri
        "great can't wait to help" #i will fix these spelling error and gramor error and change the sprite need to do research about that of all sprite poss and tranlation
        show yuri 1b zorder 2 at t11
        y "I will need you to use the school's auto tea maker 3,000"
        hide yuri
        show yuri 1b zorder 2 at f32
        y "..."
        hide yuri
        show yuri 1b zorder 2 at t11
        
        y "Hehe"
        hide yuri
        mc "Tea maker what now?"
        show yuri 1b zorder 2 at t11
        y "It's just a joke [player]"
        hide yuri
        mc "Oh "
        mc "..."
        "And now we wait to until the tea is done"
        "Then we put the tea in the glass cup"
        show yuri 1b zorder 2 at t11
        y "Tea smells good ahaha"
        hide yuri
        mc "What's so funny?"
        show yuri 2b zorder 4 at t11
        y "Nothing [player]"
        stop music 
        hide yuri
        "Yuri acting odd reminds you when something happened a long time ago when Yuri did something that was gross and terrifying but you can't remember what it was."
        play music t6
        show yuri 1b zorder 2 at t11
        y "Hehehehe"
        hide yuri
        show yuri glitch2 zorder 2 at t11
        play music t6g
        play sound g5
        y '¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéê'
        stop sound

        stop music 
        play music t6

        hide yuri
        mc "Okay Yuri"
        show yuri 1b zorder 2 at t11
        y "That's all thank's for helping [player]"
        hide yuri
        mc "No problem" 
        scene bg club_day
        with wipeleft_scene
        stop music fadeout 2.0
        play music t5



        
        #yuri lines are done just need add few fixes then it will look good
else:  #else this will happening when you click the 2 options 
        "I will help Natsuki with the cupcakes"
        show natsuki 1l zorder 2 at t11
        play music t5
        scene bg club_day
        mc "Can I help you with the cupcakes Natsuki?"
        n "Sure but you have to follow my instructions"
        "Time to Have some fun"
        n "Alright we need to make some cake, flour, eggs, sugar, salt, milk or water works, and some oil too"
        mc "Alright I'll go get that "
        n "Okay thank you"
        n "And I need a pan that's square"
        n "And the temperature need's to be up to 350 degrees"
        n "So we can bake this cake for the new student"
        mc "Okay it's done"
        "And we wait and Natsuki add some extra stuff to make it look good"
        mc "Cake look so good and Natsuki added cat ears as the icing"
        n "Alright we're done with the cake thanks to [player] for helping" # i will add sprite for these line later
        scene bg club_day
        with wipeleft_scene
        
        
if options == True: #if the player click to help yuri with the tea
    y "Tea's done thanks to [player]" #it will say this at the end
    mc "I'm happy to help"
else:
    y "Tea is done thanks to Sayori" #if the player did not help yuri with the tea then she will say this
    s "It was fun"
if options == False:
    show natsuki 1b zorder 3 at t11
    n "Cupcakes are done thanks to [player]"
    mc "I'm happy to help"
    hide natsuki
else:
    show natsuki 1b  zorder 2 at t11
    n "Cupcakes are done thanks to Sayori"
    hide natsuki 
    show sayori 1b zorder 2 at t11
    s "I've learned so much about baking thanks for letting me help out!"
    hide sayori

stop music fadeout 2.0
play music t3
show monika 3a zorder 3 at t11
m "Good job everyone!"
hide monika
"The new club member is here "

with wipeleft_scene
return # exit

#Todo for Kwhitehead07 add  40 line for the story
label chapter1_page2:
scene bg club_day
play music  t3

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
"Very lovely day we are having right [player]?"
m "We bake cupcakes, make tea, mostly basic stuff"
m "Speaking of which, its about time we write a poem, so if you don't know what to do today we'll run you through it"
i "Okay"
$ renpy.movie_cutscene("mod_assets/video/1.ogx")


















#end here for Kwhitehead07 part of the story
return

#Todo for  blackdeath5h  add story line for ironmouse Please Keep it PG 13 make it connect the story lines LyllyNotFound put and TigerClips1 Put
label chapter1_page3:















#end of Blackdeath5h story lines
return

#To Do for TIgerClips1 add the menu and add the story line for the all 6 charactor
label chapter1_page4:





































#END of lines for TigerClips1
return

#TODO for lylly not found
label chapter1_page4_part_2:







































return

#End Of Chaptor 1

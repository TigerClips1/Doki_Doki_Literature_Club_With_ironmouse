label chapter1: #label this .rpy file to it can be easy to call it in the script.rpa
# let say i'm done with this code  have to hit ctral s to save it
stop music fadeout 2.0 #stop the music when loading to the game
play music t2 #ply sayori thame
scene bg residential_day #set the scene to house
with dissolve_scene_full #vlack the screen slowlly

$ s_nmae = "sayori" #change the s_name to sayori
$ y_name = "yuri" # change y_name to yuri name
$ m_name = "Monika"# change m_name to monika
$ n_name = "Natsuki"#changeN_name to Natsuki
$ restore_all_characters()
#show sayori sprite at 2b in zoom order 2 at pose 11 
show sayori 1b zorder 2 at t11 
s "Hey [player] there's a new kid in the club." #sayori saying hey to the player name
mc "There is sayori." #mc talking
"I didn't not know we had a new student." #mc talking in his head
s "yes really." #sayori say yes really
mc "cool what's her name?" # mc talking
s "just wait and you will see" #sayori talking
"Then we go to the club" #mc talking in his head
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
y "Hey Sayori" #yuri say hi to sayori
#show yuri at 1b zoom 2 rtimes at translaton 11
hide yuri  # hide yuri sprite
show natsuki 1b zorder 2 at t11
n "Hello Sayori" #natsuki say hi
#show natsuki at 1b zom 2 at translation 11
hide natsuki  #hide Natsuki sprite
mc "Hi everyone I heard we have a new student in the club" # Main Charctor say hi to every girl in the club
show monika 1b zorder 2 at t11
m "Hello [player] how is your day"
mc "I'm having a good day today Monika, Thanks for asking"
mc ":)"
m "That's good to hear"
m "Yes there's a new student in the club"
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
    "I choose to help yuri with the Tea":
        $ options =  True # bool varable 
    "Cupcakes": #name of the menu options
        $ options = False
        "I'm happy to help"

if  options: #if statement
        "I will help yuri with the tea" #TODO for TigerClips1 add yuri sprite where match with the story so yay for me AAAAAAAAAAAAAAAAAA                  #Todo comeplate natsuki sprite for all the lines for the cupcake/ add yuri sprite fix spelling error and add yuri tea lines tomorrow
        play music t6
        scene bg club_day
        mc "Hey yuri can I help you with the tea?"
        show yuri 1e zorder 2 at t11
        y "Sure [player] this tea will get done faster when more people help out" #Yuri's text will change in the future to be like the Original Yuri for ddlc
        hide yuri
        "That great can't wait to help" #i will fix these spelling error and gramor error and change the sprite need to do research about that of all sprite poss and tranlation
        show yuri 1b zorder 2 at t11
        y "I will need you to use the school's auto tea maker 3,000"
        hide yuri
        show yuri 1b zorder 2 at f32
        y "..."
        hide yuri
        show yuri 1b zorder 2 at t11
        
        y "haha"
        hide yuri
        mc "tea maker what now?"
        show yuri 1b zorder 2 at t11
        y "it's just a joke [player]"
        hide yuri
        mc "Oh "
        mc "..."
        "And now we wait to until the tea is done"
        "Then we put the tea in the glass cup"
        show yuri 1b zorder 2 at t11
        y "Tea smells good ahaha"
        hide yuri
        mc "What's so funny "
        show yuri 2b zorder 4 at t11
        y "Nothing [player]"
        hide yuri
        "yuri acting weird reminds you when something happened a long time ago when yuri did something that was gross but you can't remember what it was."
        mc "Okay yuri"
        show yuri 1b zorder 2 at t11
        y "that's it thank you for helping [player]"
        hide yuri
        mc "No problem" 
        scene bg club_day
        with wipeleft_scene
        
        #yuri lines are done just need add few fixes then it will look good
else:  #else this will happening when you click the 2 options 
        "I will help Natsuki with the cupcakes"
        show natsuki 1l zorder 2 at t11
        play music t5
        scene bg club_day
        mc "Can I help you with the cupcakes Natsuki?"
        n "Sure but you have to follow my instructions"
        "Time to Have some fun"
        n "alright we need to make some cake, flour, eggs, sugar, salt, milk or water works, and some oil too"
        mc "Alright I'll go get that "
        n "Okay thank you"
        n "And I need a pan that's square"
        n "And the temperature need's to be up to 350 degrees"
        n "So we can bake this cake for the new student"
        mc "Okay it's done"
        "And we wait and Natsuki add some extra stuff to make it look good"
        mc "cake look so good and Natsuki added cat ears as the icing"
        n "Alright we're done with the cake thanks to [player] for helping" # i will add sprite for these line later
        scene bg club_day
        with wipeleft_scene
        
        
if options == True: #if the player click to help yuri with the tea
    y "tea's done thanks to [player]" #it will say this at the end
else:
    y "tea is done thanks to Sayori" #if the player did not help yuri with the tea then she will say this
    s "It was fun"
if options == False:
    show natsuki 1b zorder 3 at t11
    n "cupcakes are done thanks to [player]"
    hide natsuki
else:
    show natsuki 1b  zorder 2 at t11
    n "cupcakes are done thanks to Sayori"
    hide natsuki 
    show sayori 1b zorder 2 at t11
    s "I've learned so much about baking thanks for letting me help out"
    hide sayori

stop music fadeout 2.0
play music t3
show monika 3a zorder 3 at t11
m "Good job everyone"
hide monika
"The new club member is here"
return # exit

#Todo for Kwhitehead07 add  40 line for the story
label chapter1_page2:






























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
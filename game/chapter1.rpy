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
s "Hey [player] there a new kid in the club." #sayori saying hey to the player name
mc "There is sayori." #mc talking
"I Did not know we have a new student." #mc talking in his head
s "yes really." #sayori say yes really
mc "cool what's her name" # mc talking
s "just wait and you will see" #sayori talking
"So we go to the club" #mc talking in his head
show bg club_day  # show the club room day
with wipeleft_scene
stop music fadeout 2.0 
play music t3
show sayori 2b zorder 2 at t11 

s "Hey monika and hey yuri and hey natsuki" # sayori speak
hide sayori  # hideing sayori sprite
#show sayori sprite to 2b becuse i don't know what pose to give to her model t11 mean tranlation then where you see the charctor appear
show monika 3b zorder 2 at t11 
m "Hey sayori" # monika say hi to sayori
#show monika at 3b and zoom 2times at translation 11
hide monika # hide monika sprite
show yuri 1b zorder 2 at t11 
y "hey sayori" #yuri say hi to sayori
#show yuri at 1b zoom 2 rtimes at translaton 11
hide yuri  # hide yuri sprite
show natsuki 1b zorder 2 at t11
n "hey sayori" #natsuki say hi
#show natsuki at 1b zom 2 at translation 11
hide natsuki  #hide Natsuki sprite
mc "hello everyone i hear we have a new student in the club" # Main Charctor say hi to every girl in the club
show monika 1b zorder 2 at t11
m "Hello [player] how is your day"
mc "monika i'm haveing a good day Thanks for asking"
mc ":)"
m "that good to hear"
m "yes there is a new student in the club"
hide monika
show natsuki 1b zorder 2 at t11
n "there is a new student i should make some cupcakes"
hide natsuki
show yuri 1b zorder 2 at t11 
y "i will get the tea"
hide yuri
scene bg club_day
with wipeleft_scene
menu: #let the player controll the story
    mc "who should i help" # mc talking to him self asking who he will help
    "i chose to help yuri with the Tea":
        $ options =  True # bool varable 
    "Cupcakes": #name of the menu options
        $ options = False
        "I'm so happy to help"

if  options: #if satement
        "i will help yuri with the tea" #TODO for TigerClips1 add yuri sprite where match with the story so yay for me AAAAAAAAAAAAAAAAAA                  #Todo comeplate natsuki sprite for all the lines for the cupcake/ add yuri sprite fix spelling error and add yuri tea lines tomorrow
        play music t6
        scene bg club_day
        mc "Hey yuri can i help you with the tea"
        show yuri 1e zorder 2 at t11
        y "yes sure [player] this tea will get done faster when more people help out" #yuri text will change in the feture to be like the Og yuri for ddlc
        hide yuri
        "That great can't wait to help" #i will fix these spelling error and gramor error and change the sprite need to do research about that of all sprite poss and tranlation
        show yuri 1b zorder 2 at t11
        y "i need you to use the school auto tea maker 3.000"
        hide yuri
        show yuri 1b zorder 2 at f32
        y "..."
        hide yuri
        show yuri 1b zorder 2 at t11
        
        y "haha"
        hide yuri
        mc "tea maker what"
        show yuri 1b zorder 2 at t11
        y "it's just a joke [player]"
        hide yuri
        mc "oh "
        mc "..."
        "and we wait to until the tea is done"
        "now we put the tea in the glass cup"
        show yuri 1b zorder 2 at t11
        y "tea smell good ahaha"
        hide yuri
        mc "what so funny "
        show yuri 2b zorder 4 at t11
        y "nothing [player]"
        hide yuri
        "yuri act wired remind of something happen long time ago when yuri did something that was gross cant remaber what that is."
        mc "okay yuri"
        show yuri 1b zorder 2 at t11
        y "that it thanks for helping [player]"
        hide yuri
        mc "no problom" 
        scene bg club_day
        with wipeleft_scene
        
        #yuri lines are done just need add few fixes then it will look good
else:  #else this will happening when you click the 2 options 
        "I will help Natsuki with the cupcakes"
        show natsuki 1l zorder 2 at t11
        play music t5
        scene bg club_day
        mc "natsuki can i help you with the cupcaks"
        n "sure but you have to fellow everything "
        "Time to Have fun"
        n "allright we need to make  cake flour, eggs, sugar, salt, milk or water will work, oil "
        mc "i will get that "
        n "ok thank you"
        n "and i need a pan that square"
        n "tempurture need to be 350 degress"
        n "To bake this cake for  the new student"
        mc "ok done"
        "and we wait and natsuki add some extra stuff to make it look good"
        mc "cake look so good and Natsuki added cat ears as the icing"
        n "allright we done with the cake thanks to [player] for helping" # i will add sprite for these line later
        scene bg club_day
        with wipeleft_scene
        
        
if options == True: #if the player click to help yuri with the tea
    y "tea is done thanks to [player]" #it will say this at the end
else:
    y "tea is done thanks to sayori" #if the player did not help yuri with the tea then she will say this
    s "it was fun"
if options == False:
    show natsuki 1b zorder 3 at t11
    n "cupcakes are done thanks to [player]"
    hide natsuki
else:
    show natsuki 1b  zorder 2 at t11
    n "cupocakes are done thanks to sayori"
    hide natsuki 
    show sayori 1b zorder 2 at t11
    s "i learn so much about bakeing thanks for letting me help you"
    hide sayoori

stop music fadeout 2.0
play music t3
show monika 3a zorder 3 at t11
m "good job to all"
hide monika
"new club member is here"
return # exit

#Todo for LyllyBotFound add  40 line for the stroy
label chapter1_page2:






























#end here for LyllyNotFound part of the story
return

#Todo for  blackdeath5h  add story line for ironmouse Please Keep it PG 13 make it connect the story lines LyllyNotFound put and TigerClips1 Put
label chapter1_page3:















#end of Blackdeath5h story lines
return

#To Do for TIgerClips1 add the menu and add the story line for the all 6 charactor
label chapter1_page4:






























































#todo Kwhitehead07




































return

#End Of Chaptor 1
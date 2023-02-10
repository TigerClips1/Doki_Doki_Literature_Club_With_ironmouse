label chapter1: #label this .rpy file to it can be easy to call it in the script.rpa

stop music fadeout 2.0 #stop the music when loading to the game
play music t2 #ply sayori thame
scene bg residential_day #set the scene to house
with dissolve_scene_full #vlack the screen slowlly

$ s_nmae = "sayori" #change the s_name to sayori
$ y_name = "yuri" # change y_name to yuri name
$ m_name = "Monika"# change m_name to monika
$ n_name = "Natsuki"#changeN_name to Natsuki
#show sayori sprite at 2b in zoom order 2 at pose 11 
show sayori 2b zorder 2 at t11 
s "Hey [player] there a new kid in the club." #sayori saying hey to the player name
mc "There is sayori." #mc talking
"I Did not know we have a new student." #mc talking in his head
s "yes really." #sayori say yes really
mc "cool what her name" # mc talking
s "just wait and you will see" #sayori talking
"So we go to the club" #mc talking in his head
with wipeleft_scene #wipe the screen to the left to let the player know there done with that line of text
hide bg residential_day # hide the scen background
hide sayori  # hide sayori sprite
show bg club_day # show the club room day
s "Hey" # sayori speak
#show sayori sprite to 2b becuse i don't know what pose to give to her model t11 mean tranlation then where you see the charctor appear
show sayori 2b zorder 2 at t11 
m "Hey sayori" # monika say hi to sayori
hide sayori  # hideing sayori sprite
#show monika at 3b and zoom 2times at translation 11
show monika 3b zorder 2 at t11 
y "hey sayori" #yuri say hi to sayori
hide monika # hide monika sprite
#show yuri at 1b zoom 2 rtimes at translaton 11
show yuri 1b zorder 2 at t11 
n "hey sayori" #natsuki say hi
hide yuri  # hide yuri sprite
#show natsuki at 1b zom 2 at translation 11
show natsuki 1b zorder 2 at t11
hide natsuki  #hide Natsuki sprite
mc "hello everyone i here we have a new kid in the club" # Main Charctor say hi to every girl in the club
return # exit
#todo add menu and all the 4chr say hi to mc  and add music for TigerClips1

#Todo for LyllyBotFound add  40 line for the stroy






























#end here for LyllyNotFound part of the story
return

#Todo for  blackdeath5h  add story line for ironmouse Please Keep it PG 13 make it connect the story lines LyllyNotFound put and TigerClips1 Put















#end of Blackdeath5h story lines
return

#To Do for TIgerClips1 add the menu and add the story line for the all 6 charactor



































































































return

#End Of Chaptor 1
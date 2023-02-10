label chapter1:

stop music fadeout 2.0
play music t2
scene bg residential_day
with dissolve_scene_full

$ s_nmae = "sayori"
$ y_name = "yuri"
$ m_name = "Monika"
$ n_name = "Nutsuki"
$ i_name = "ironmouse"
show sayori 2b zorder 2 at t11
s "Hey [player] there a new kid in the club."
mc "There is sayori."
"I Did not know we have a new student."
s "yes really."
mc "cool what her name"
s "just wait and you will see"
"So we go to the club"
with wipeleft_scene
hide bg residential_day
hide sayori 
show bg club_day
s "Hey"
show sayori 2b zorder 2 at t11
m "Hey sayori"
hide sayori 
show monika 3b zorder 2 at t11
y "hey sayori"
hide monika
show yuri 1b zorder 2 at t11
n "hey sayori"
hide yuri 
show natsuki 1b zorder 2 at t11
hide natsuki 
mc "hello everyone i here we have a new kid in the club"
return
#todo add menu and all the 4chr say hi to mc  and add music
#Todo for LyllyBotFound add her line for the stroy

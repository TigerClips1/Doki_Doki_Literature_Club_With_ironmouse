## script.rpy

# This is the main script that Ren'Py calls upon to start
# your mod's story! 

label start:

    # This label configures the anticheat number for the game after Act 1.
    # It is recommended to leave this as-is and use the following in your script:
    #   $ persistent.anticheat = renpy.random.randint(X, Y) 
    #   X - The minimum number | Y - The maximum number
    $ anticheat = persistent.anticheat

    # This variable sets the chapter number to 0 to use in the mod.
    $ chapter = 0

    # This variable controls whether the player can dismiss a pause in-game.
    $ _dismiss_pause = config.developer

    ## Names of the Characters
    # These variables set up the names of the characters in the game.
    # To add a character, use the following example below: 
    #   $ mi_name = "Mike". 
    # Don't forget to add the character to 'definitions.rpy'!
    $ s_name = "Sayori"
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"
    $ i_name = "?????????"

    # This variable controls whether the quick menu in the textbox is enabled.
    $ quick_menu = True

    # This variable c ontrols whether we want normal or glitched dialogue
    # For glitched dialogue, use 'style.edited'.
    $ style.say_dialogue = style.normal

    # This variable controls whether Sayori is dead. It is recommended to leave
    # this as-is.
    $ in_sayori_kill = None
    
    # These variables controls whether the player can skip dialogue or transitions.
    $ allow_skipping = True
    $ config.allow_skipping = True

    ## The Main Part of the Script
    # This is where your script code is called!
    # 'persistent.playthrough' controls the playthrough number the player is on i.e (Act 1, 2, 3, 4)
    #TODO add an elif satement here
    if persistent.playthrough == 0:
        #TODO all these will be comment out until the credits are done  for testing
        #Day 1 ##
        $ chapter = 1
        call chapter1 from _call_chapter1 
        call chapter1_page2 from _call_chapter1_page2
        call chapter1_page3 from _call_chapter1_page3
        call chapter1_page4 from _call_chapter1_page4
        call chapter1_page4_part_2 from _call_chapter1_page4_part_2
        call poem from _call_poem
        jump credits
        return

        #Day 2 ##
        #$ chapter = 2
        #call chapter2 from _call_chapter2
        #call poem from _call_poem_1
        
        ## Day 3 ##
        #$ chapter = 3
        #call chapter3 from _call_chapter3 
        #call poem from _call_poem_2
        #jump credits
        #return
# This label is where the game 'ends' during Act 1.
label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return

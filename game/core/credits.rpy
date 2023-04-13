## credits.rpy

# END

#TODO  make the credits nice  

# This image shows the DDLC logo with certain transforms.
image credits_logo:
    "mod_assets/gui/logo.png"
    truecenter
    zoom 0.6 alpha 0 subpixel True
    linear 2.0 alpha 1
    4.5
    linear 2.0 alpha 0

# This image shows the DDLCWITHIRONmouse team logo with certain transforms.
image credits_ts:
    "mod_assets/images/bg/splash.png"
    xalign 0.5 yalign 0.6
    zoom 0.65 alpha 0 subpixel True
    linear 2.0 alpha 1
    4.5
    linear 2.0 alpha 0

# This style declares the text appearance of the work type credits text in the
# credits.
style credits_header:
    font "gui/font/RifficFree-Bold.ttf"
    color "#ffaae6"
    size 36
    text_align 0.5
    outlines []

# This style declares the text appearance of the person type credits text in the
# credits.
style credits_text:
    font "gui/font/Halogen.ttf"
    color "#fff"
    size 36
    text_align 0.5
    outlines []

# This image shows the work-type credits text to the credits (Game Concept).
image credits_header = ParameterizedText(style="credits_header", ypos=-40)

# This image shows the person-type credits text to the credits (Dan Salvato).
image credits_text = ParameterizedText(style="credits_text", ypos=40)


# This transform handles the credits scrolling animation in the credits.
transform credits_scroll:
    subpixel True
    yoffset 740
    linear 15 yoffset -380

# This transform handles the credits text scrolling animation in the credits.
transform credits_text_scroll:
    anchor (0.5, 0.5) subpixel True
    yoffset 920
    linear 15 yoffset -200


# This transform handles the credits right scrolling animation in the credits.
transform credits_scroll_right:
    xalign 0.9
    credits_scroll

# This transform handles the credits left scrolling animation in the credits.
transform credits_scroll_left:
    xalign 0.1
    credits_scroll

# This transform handles the credits text right scrolling animation in the credits.
transform credits_text_scroll_right:
    xpos 960
    credits_text_scroll

# This transform handles the credits text left scrolling animation in the credits.
transform credits_text_scroll_left:
    xpos 320
    credits_text_scroll

# This label starts the second part of the credits with development information.
label credits:
    scene black
    play music t1
    $ starttime = datetime.datetime.now()
    pause 0.88
    show credits_logo
    pause 9.12
    
    # These show statements shows the work-type and person-type credits in the 
    # credits.
    show credits_header "OG Programmer" as credits_header_1 at credits_text_scroll_left
    show credits_text "Dan Salvato" as credits_text_1 at credits_text_scroll_left
    
    $ pause(35.15)
    
    show credits_header "OG Character Art" as credits_header_2 at credits_text_scroll_right
    show credits_text "Satchely" as credits_text_2 at credits_text_scroll_right
    
    $ pause(45.25)
    
    show credits_header "OG Background Art" as credits_header_1 at credits_text_scroll_left
    show credits_text "Velinquent" as credits_text_1 at credits_text_scroll_left
    
    $ pause(46.35)
    
    show credits_header "OG Writing" as credits_header_2 at credits_text_scroll_right
    show credits_text "Dan Salvato" as credits_text_2 at credits_text_scroll_right
    
    $ pause(47.45)
    
    show credits_header "OG Music" as credits_header_1 at credits_text_scroll_left
    show credits_text "Dan Salvato" as credits_text_1 at credits_text_scroll_left
    
    $ pause(48.55)
    
    show credits_header "OG Vocals" as credits_header_2 at credits_text_scroll_right
    show credits_text "Jillian Ashcraft" as credits_text_2 at credits_text_scroll_right
    
    $ pause(49.65 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header "Programming/Story" as credits_header_1 at credits_text_scroll_left
    show credits_text "TigerClips1" as credits_text_1 at credits_text_scroll_left
    $ pause(50.75)
    show credits_header "Programming/Story" as credits_header_2 at credits_text_scroll_right
    show credits_text "Kwhitehead07" as credits_text_2 at credits_text_scroll_right
    $ pause(51.85 - (datetime.datetime.now() - starttime).total_seconds())
    show credits_header "Programming/Story" as credits_header_1 at credits_text_scroll_left
    show credits_text "LyllyNotFound" as credits_text_1 at credits_text_scroll_left
    $ pause(51.95)
    show credits_header "Programming/Story" as credits_header_2 at credits_text_scroll_right
    show credits_text "Blackwolf5h" as credits_text_2 at credits_text_scroll_right
    $ pause(53.95 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header "Character Art" as credits_header_1 at credits_text_scroll_left
    show credits_text "Nexus" as credits_text_1 at credits_text_scroll_left
    $ pause(54.95)
    show credits_header "Stickr art" as credits_header_2 at credits_text_scroll_right
    show credits_text "Just Jam" as credits_header_2 at credits_text_scroll_right
    
    $ pause(55.95 - (datetime.datetime.now() - starttime).total_seconds())

    show credits_header "Background art" as credits_header_1 at credits_text_scroll_left
    show credits_text "Justjam\nNexus" as  credits_text_1 at credits_text_scroll_left
    $ pause(56.95)
    show credits_header "Main Menu music" as credits_header_2 at credits_text_scroll_right
    show credits_text " Video Game Remixes" as credits_text_2 at credits_text_scroll_right
    
    $ pause(57.95 - (datetime.datetime.now() - starttime).total_seconds())

    show credits_header "Special Thanks" as credits_header_1 at credits_text_scroll_left
    show credits_text "IronMouse" as credits_header_1 at credits_text_scroll_left
    $ pause(58.96)
    show credits_header "Special Thanks" as credits_header_2 at credits_text_scroll_right
    show credits_text "BejuuMike" as credits_text_2 at credits_text_scroll_right
    $ pause(59.97 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header "Special Thanks" as credits_header_1 at credits_text_scroll_right
    show credits_text "GhostNight SA" as credits_text_1 at credits_text_scroll_right
 
    show credits_header "Special Thanks" as credits_header_2 at credits_text_scroll_left
    show credits_text "[player]" as credits_text_2 at credits_text_scroll_left
    
    $ pause(101.10 - (datetime.datetime.now() - starttime).total_seconds())
     
    show credits_ts
    show credits_text "made with love by":
        zoom 0.75 xalign 0.5 yalign 0.25 alpha 0 subpixel True
        linear 2.0 alpha 1
        4.5
        linear 2.0 alpha 0
    pause 9.3

    # This label starts the end of the game loop with the ending poem or Dan's 
    label postcredits_loop:
        $ persistent.autoload = "postcredits_loop"
        $ renpy.save_persistent()
        $ config.keymap['game_menu'] = []
        $ config.keymap['hide_windows'] = []
        $ renpy.display.behavior.clear_keymap_cache()
        $ quick_menu = False
        $ config.skipping = False
        $ config.allow_skipping = False

        scene black
        stop music fadeout 2.0
        python:
            delete_all_saves()
            renpy.loadsave.location.unlink_persistent()
            renpy.persistent.should_save_persistent = False
            renpy.quit()
    return

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

# This transform handles the credits center scrolling animation in the credits.
transform credits_scroll_center:
    xalign 0.6
    credits_scroll

# This transform handles the credits text center scrolling animation in the credits.
transform credits_text_scroll_center:
    xpos 620
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
    show credits_header "\nOG Programmer" as credits_header_1 at credits_text_scroll_center
    show credits_text "\nDan Salvato" as credits_text_1 at credits_text_scroll_center
    
    $ pause(35.15 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header "\nOG Character Art" as credits_header_2 at credits_text_scroll_center
    show credits_text "\nSatchely" as credits_text_2 at credits_text_scroll_center
    
    $ pause(36.15 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header "\nOG Background Art" as credits_header_1 at credits_text_scroll_center
    show credits_text "\nVelinquent" as credits_text_1 at credits_text_scroll_center
    
    $ pause(37.15 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header "\nOG Writing" as credits_header_2 at credits_text_scroll_center
    show credits_text "\nDan Salvato" as credits_text_2 at credits_text_scroll_center
    
    $ pause(38.15 - (datetime.datetime.now() - starttime).total_seconds())

    show credits_header "\nOG Music" as credits_header_1 at credits_text_scroll_center
    show credits_text "\nDan Salvato" as credits_text_1 at credits_text_scroll_center
    
    $ pause(39.15 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header "\nOG Vocals" as credits_header_2 at credits_text_scroll_center
    show credits_text "\nJillian Ashcraft" as credits_text_2 at credits_text_scroll_center
    
    $ pause(40.15 - (datetime.datetime.now() - starttime).total_seconds())
       
    show credits_header "\nProgramming/Story" as credits_header_1 at credits_text_scroll_center
    show credits_text "\nBlackwolf5h" as credits_text_1 at credits_text_scroll_center
    show credits_text "\nKwhitehead07" as credits_text_1 at credits_text_scroll_center
    show credits_text "\nLyllyNotFound" as credits_text_1 at credits_text_scroll_center
    show credits_text "\nTigerClips1" as credits_text_1 at credits_text_scroll_center

    $ pause(44.15 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header "\nBackgrund Art/Sticker art/Character Art" as credits_header_1 at credits_text_scroll_center
    show credits_text "\nJustjam" as  credits_text_1 at credits_text_scroll_center
    show credits_text "\nNexus" as  credits_text_1 at credits_text_scroll_center
    $ pause(47.15 - (datetime.datetime.now() - starttime).total_seconds())
    #TDO fix the Credits
    show credits_header "\nMain Menu music" as credits_header_2 at credits_text_scroll_center
    show credits_text "\nVideoGameRemixes" as credits_text_2 at credits_text_scroll_center
    
    $ pause(48.15 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header "\nSpecial Thanks" as credits_header_1 at credits_text_scroll_center
    show credits_text "\nGhostNight SA\n[player]\nBijuuMike\nIronMouse" as credits_text_1 at credits_text_scroll_center

    $ pause(90.10 - (datetime.datetime.now() - starttime).total_seconds())
    
    stop music fadeout 2.0
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
        python:
            delete_all_saves()
            renpy.loadsave.location.unlink_persistent()
            renpy.persistent.should_save_persistent = False
            renpy.quit()
    return

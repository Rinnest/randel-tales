screen say(who, what):
    style_prefix "say"

    frame:
     xpos 0 ypos 0
     minimum (1280, 35)
     ymaximum 35
     text "[calendar.Output]" xalign 0.5


    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

screen hud():
    add "images/border.png"

    vbox:

        if time == 0:
            text "morning"
        if time == 1:
            text "afternoon"
        if time == 2:
            text "evening"
        if time == 3:
            text "night"

    vbox xalign 0.0 yalign 0.06:

        text "Money-[money]"

    vbox xalign 0.5 yalign 0.0:


        text "Day [day]"
    imagebutton:
        xalign 0.9
        yalign 0.0
        idle "journal"
        hover "journalh"
        action Show("screenjournal")

    imagebutton:
        xalign 1.0
        yalign 0.0
        idle "map"
        hover "maph"
        action Show("screenmap")
        activate_sound "map.mp3"

screen traits():
    hbox xalign 0.01 yalign 0.9:



        imagebutton:
            xalign 0.2
            yalign 0.2
            idle "bwct"
            hover "bwct1"
            action Jump("bookworm")

        imagebutton:
            xalign 0.2
            yalign 0.2
            idle "hhct"
            hover "hhct1"
            action Jump("hothead")

        imagebutton:
            xalign 0.99
            yalign 0.8
            idle "pct"
            hover "pct1"
            action Jump("playful")  

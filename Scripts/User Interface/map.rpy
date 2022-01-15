label map:
    play sound ("map.mp3")
    show mapscrn with dissolve

    menu:
        "home":
            jump home

        "academy":
            if time > 1:
                mc "the academys closed,i cant go there now"
                jump map
            jump academy

        "adventures guild":
            if time > 2:
                mc "Ive got nothing to do there at night"
                jump map
            jump guild

        "library":
            if time > 2:
                "the librarys closed"
                jump map
            jump library

        "trading shop":
            if time > 2:
                "hes probably gone at this time"
                jump map
            jump store

        "Forrest":
            if time > 2:
                "its dangerous to go out there in the night"
                jump map
            jump forest

        "Pete's fishing hut":
            if time > 2:
                "i should'nt bother him at this time"
                jump map
            jump fishhut

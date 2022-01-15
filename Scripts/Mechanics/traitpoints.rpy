label hothead:
    $ chartrait += 2
    play sound ("chime.mp3")
    $ renpy.notify("Character trait: Hot head")
    jump out1

label playful:
    $ chartrait += 3
    play sound ("chime.mp3")
    $ renpy.notify("Character trait: Playful")
    jump out1

label bookworm:
    $ chartrait += 1
    play sound ("chime.mp3")
    $ renpy.notify("Character trait: Bookworm")
    jump out1

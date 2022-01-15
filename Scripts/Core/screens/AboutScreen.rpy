screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")


            text _("A game by Bunis")
            text _("Music by Vimuwima. {a=https://vimuwima.onuniverse.com/}Check him out{/a}")
            text _("Version X by Rin. {a=https://f95zone.to/members/trapgodrin.3632583/}Check him out{/a}")
            text _("I would like to thank all my wonderfull Patrons for supporting the game, also thanks to all the beta testers for giving me feedback and helping me make the game better.")
            text _("And thank you all for playing")


            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")

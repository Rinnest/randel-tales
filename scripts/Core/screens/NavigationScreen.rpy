screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        if not main_menu:

            textbutton _("Main Menu") action MainMenu()

        if renpy.variant("pc"):

            textbutton _("Quit") action Quit(confirm=not main_menu)

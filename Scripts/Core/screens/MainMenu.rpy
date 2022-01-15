screen main_menu():


    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        pass

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"

    ##patreon link

    imagebutton:
        idle "patreonbutton"
        hover "patreonbutton1"
        action OpenURL("https://www.patreon.com/randeltales")
        xalign 0.7
        yalign 0.95

    imagebutton:
        idle "discord"
        hover "discord1"
        action OpenURL("https://discord.gg/5SutjWP")
        xalign 0.5
        yalign 0.99

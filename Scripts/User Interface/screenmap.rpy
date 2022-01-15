screen screenmap():
    image ("mapscrn")
    
    imagebutton:
        
        
        
        
        
        xalign 0.3
        yalign 0.0
        idle "journalbackscrn"
        hover "journalbackscrn1"
        action Hide("screenmap")
    imagebutton:
        xalign 0.55
        yalign 0.2
        idle "mplibrary"
        hover "mplibrary1"
        action Jump("library")  
        
    imagebutton:
        xalign 0.75
        yalign 0.55
        idle "mpguild"
        hover "mpguild1"
        action Jump("guild")  
        
    imagebutton:
        xalign 0.9
        yalign 0.75
        idle "mpmerch"
        hover "mpmerch1"
        action Jump("store")  
        
    imagebutton:
        xalign 0.25
        yalign 0.7
        idle "mpmark"
        hover "mpmark1"
        action Jump("market")  
        
    imagebutton:
        xalign 0.55
        yalign 0.55
        idle "mpgabe"
        hover "mpgabe1"
        action Jump("gabehouse")  
        
    imagebutton:
        xalign 0.25
        yalign 0.37
        idle "mpsacademy"
        hover "mpsacademy1"
        action Jump("academy")  
        
    imagebutton:
        xalign 0.57
        yalign 0.85
        idle "mphouse"
        hover "mphouse1"
        action Jump("home")  
    
    imagebutton:
        xalign 0.93
        yalign 0.1
        idle "mphut"
        hover "mphut1"
        action Jump("fishhut")  
    
    imagebutton:
        xalign 0.165
        yalign 0.9999
        idle "mpforrest"
        hover "mpforrest1"
        action Jump("forest")  
        
    
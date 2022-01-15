screen screenjournal():
    add "images/journalscrn.png"
    vbox xalign 0.6 yalign 0.1:
        text "[mc]'s Journal"
        
    vbox xalign 0.82 yalign 0.565:
        if level >= 10:
            text "{color=#800000} Bronze {/color}"

    vbox xalign 0.67 yalign 0.6:
        text "[level]"
        text "[exp]"
    vbox xalign 0.78 yalign 0.29:
        
        text "[swordlvl]"
        text "[bowlvl]"
        text "[magiclvl]"
    
    imagebutton:
        
        
        
        
        
        xalign 0.9
        yalign 0.0
        idle "journalbackscrn"
        hover "journalbackscrn1"
        action Hide("screenjournal")
        
    imagebutton:
        
        
        xalign 0.44
        yalign 0.15
        idle "notesbtn"
        hover "notesbtn1"
        action Hide ("screenjournal") and Show ("notes")
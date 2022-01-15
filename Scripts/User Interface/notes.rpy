screen notes():
    image ("notesjournal")
    
    imagebutton:
        
        
        
        
        xalign 0.9
        yalign 0.0
        idle "journalbackscrn"
        hover "journalbackscrn1"
        action Hide("notes")
        
    vbox ymaximum 0.8 xalign 0.85 yalign 0.2 xsize 0.32 xanchor 0.8 yanchor 0:
        ## quest 1
        if q1 == 0:
            text ("> I should visit the guild again.")
        if q1 == 1 :
            
            text ("{b}The Way of the Voyeur{/b}")
            text ("> So I need to learn about the invisibilty spell.")
            text (" I could ask Scarlett.")
            
        if q1 == 2 and ieyeorb == 0:
            text ("{b}The Way of the Voyeur{/b}")
            text ("> I need to buy an Eye Orb from the merchant.")
            
        if q1 == 2 and ieyeorb == 1:
            text ("{b}The Way of the Voyeur{/b}")
            text ("> Ok... It's peaking time...")
        
        if q1 == 3:
            text ("{b}The Way of the Voyeur.{/b}")
            text ("> I should give this Eye Orb to Sander.")
        
        ## quest 2
        if q2 == 0 and q1 == 4:
            text ("> I should talk to Eve?")
            
        if q2 == 1 and readalphafalcon == 0:
            
            text ("{b}Show Who's Alpha{/b}")
            text ("> I need to learn about the \"Alpha Falcon\".")
            
        if q2 == 1 and readalphafalcon == 1:
            text ("{b}Show Who's Alpha{/b}")
            text ("> I need paint for a green arrow. I think Uncle Pete might have some.")
            
            
        if q2 == 2 and alphafalcon < 3:
            
            text ("{b}Show Who's Alpha{/b}")
            text ("> Its time to hunt.")
        
        if q2 == 2 and alphafalcon >= 3:
            text ("{b}Show Who's Alpha{/b}")
            text ("> I've hunted the three Alpha Falcons. Now I gotta go speak to Eve.")
        
        if diamond == 1:
            text ("{b}Miscellaneous{/b}")
            text ("> I better sell this diamond. The only place I think I can sell it at is..")
            text ("Mervin's Trading Center")
            
        if theanight == 1 and stealthlvl == 0:
            text ("{b}Thea's quest{/b}")
            text "> Thea keeps waking up. I need to find a way to do more with her.."
            text "Who could I ask for advice on something like this?"
        
        if sawcynth == 3:
            text ("{b}Miscellaneous{/b}")
            text "> I should talk to cynthia at the academy"
            
        if level >= 5 and icamping == 0:
            text ("{b}Miscellaneous{/b}")
            text ("> since now I'm able to go on quests, I should probably buy some camping gear")
            
        if level < 10:
            text ("{b}Miscellaneous{/b}")
            text ("> I should level up more in the guild")
        if party == 1:
            text ("{b}Miscellaneous{/b}")
            text ("> I should probably talk to eve if I want to go on a quest with them")
        
        if findtheaclothes == 1:
            text ("{b}Thea's quest{/b}")
            text ("> I need some clothes for Thea. Who can i ask?")
            text ("someone from the academy I guess.")
        
        if thearuntimer > 0 and thearun ==1:
            text ("{b}Thea's quest{/b}")
            text ("> I didn't see Thea around today.I should check on her")
            
        if theajob == 1:
            text ("{b}Thea's quest{/b}")
            text ("> I should wait for a few days")
            
        if level >= 10 and party == 1 and sawtriss == 0:
            text ("{b}Miscellaneous{/b}")
            text ("> I should visit the guild")
        
        if level >= 10 and party == 1 and sawjuly == 1:
            text ("{b}Miscellaneous{/b}")
            text ("> July is Hiding something. I should sneak into the guild at night and see whats going on")
        if level >= 10 and party == 1 and sawjuly == 2 and sawjuly < 4:
            text ("{b}Miscellaneous{/b}")
            text ("> I should check on July and see whats really going on.")
        if sawtriss == 1:
            text ("{b}Triss's Quest{/b}")
            text ("> I feel like going into the forest today")
            
        if sawmegan == 1:
            text ("{b}Megan's Quest{/b}")
            text ("> I should go hunting today")
        if sawmegan == 2:
            text ("{b}Megan's Quest{/b}")
            text ("> I should go tell July about the bandits I saw in the forest")
        
        if sawmegan == 3 and metmegangq == 0:
            text ("{b}Megan's Quest{/b}")
            text ("> I should meet Megan at the guild quarters in the evening.")
            
        if trissq1 == 1 and ibugnet == 0:
            text ("{b}Triss's Quest{/b}")
            text ("> I should buy a bug net to catch butterflies.")
        
        if trissq1 == 1 and ibugnet == 1:
            text ("{b}Triss's Quest{/b}")
            text ("> Ok I got the net. Now I just have to go meet her in the afternoon.")
        
        if trissq1 == 2 and mettrissgq == 0:
            text ("{b}Triss's Quest{/b}")
            text ("> I should meet Triss at the guild quarters in the afternoon.")
            
        if aerindead == 1 or savedaerin == 1 and evemillyquest == 0:
            text ("{b}Eve's Quest{/b}")
            text ("> I should meet Eve at the guild quarters.")
            
        if party == 1 and showpetebadge == 0:
            text ("{b}Miscellaneous{/b}")
            text ("> I'm a bronze level adventurer now! I should go and tell uncle Pete the good news")

        if day >= 5 and gabee1 == 0 and sanderquest> 0:
            
            text ("{b}Gabe's Quest{/b}")
            text ("> Go to the academy in the evening.")
        
        if gabee1 == 1:
            
            text ("{b}Gabe's Quest{/b}")
            text ("> I need to find a history book. I should go to the library.")
        
        if gabee1 == 2:
            
            text ("{b}Gabe's Quest{/b}")
            text ("> I couldn't find a book in the library. Lori told me to ask Boris.")
        
        if gabee1 == 3 and studygabe2 == 0:
            
            text ("{b}Gabe's Quest{/b}")
            text ("> I should study the books and go to Gabe's house in the evening.")
            
        if studygabe2 == 1 and didtest == 0:
            text ("{b}Gabe's Quest{/b}")
            text ("> I should wait until the test.")
        
        if didtest == 1 and faila == 0 and level < 10:
            text ("{b}Gabe's Quest{/b}")
            text ("> I should focus on leveling up in the guild.")
        
        if gabe2 == 1 and level >= 10 and gabequest2 == 0:
            text ("{b}Gabe's Quest{/b}")
            text ("> I think I saw a new quest on the quest board.")
        
        if gabequest2 == 1 and gabequest3 == 0:
            text ("{b}Gabe's Quest{/b}")
            text ("Train Gabe :>")
            
        if gabefinger > 4 and gabefingerclass == 0:
            text ("{b}Gabe's Quest{/b}")
            text ("I should go to class. I have a special training for Gabe in mind.")
        
        if gabefingerclass == 1 and dildoi == 0:
            text ("{b}Gabe's Quest{/b}")
            text ("I should buy Gabe a present. Something that will help her with her training.")
        
        if gabedildo >= 5 and gabetrip == 0:
            text ("{b}Gabe's Quest{/b}")
            text ("I should go to Gabes house in the evening.")
        
        if gabetrip == 1 and gabequest3 == 0:
            text ("{b}Gabe's Quest{/b}")
            text ("Go to the academy.")
        
        if  sanderquest == 0:
            text ("{b}Gabe's Quest{/b}")
            text ("I should complete Sanders quest first.")
            
             
        if theagotjob == 1 and theadogfood == 0:
            text ("{b}Thea's Quest{/b}")
            text ("I should check on Thea.")
        
        if petedinner == 1 and sanderevedinner < 1:
            text ("{b}Thea's Quest{/b}")
            text ("I should tell Thea that I'm inviting Sander and Eve for dinner tonight.")
        if sanderpetedinner == 0  and sanderevedinner == 2:
            text ("{b}Thea's Quest{/b}")
            text ("Invite someone for dinner.")
        
        if sanderpetedinner == 2 and theadinner < 2:
            text ("{b}Thea's Quest{/b}")
            text ("I wonder what Thea would think about having dinner with me. Come on man up and ask her [mc]!")
            
        if theadinner == 3 and theasex == 0:
            text ("{b}Thea's Quest{/b}")
            text ("I should go see Thea at work. The tavern should be at the market. Go in the evenings.")
        
        if theaguildjob < 2 and theasex == 1:
            text ("{b}Thea's Quest{/b}")
            text ("Go to the guild and ask July if Thea could get a job there.")
        if theaguildjob == 2:
            text ("{b}Thea's Quest{/b}")
            text ("Tell Thea she got the job!")
        
        if theaguildjob == 3 and theaguild == 0:
            text ("{b}Thea's Quest{/b}")
            text ("Lets see how Thea's doing at her new job. Go in the evenings.")
             
        
        if sawcynth >= 6  and party == 1 and cynthquest2 == 0 and savecynth == 1:
            text ("{b}Cynthia's Quest{/b}")
            text ("Go to the guild in the afternoon.")
        
        if cynthquest2 == 1 and cynthquest3 == 0:
            text ("{b}Cynthia's Quest{/b}")
            text ("I should talk to cynthia in the afternoon.")
        
        if cynthquest3 == 1 and cynthtrain < 7:
            text ("{b}Cynthia's Quest{/b}")
            text ("I should train with Cynthia in the evenings.")
        
        if cynthtrain >= 7 and cynthquest4 == 0:
            text ("{b}Cynthia's Quest{/b}")
            text ("Cynthia asked me to come with her on a monster hunt. I should talk to her in the guild when I'm ready.")
        
        if cynthquest4 == 1 and  cynthquest5 == 0:
            text ("{b}Cynthia's Quest{/b}")
            text ("Todays a good day to go hunting. I should go to the forest.")
        
        if cynthquest5 >= 1 and cynthboots == 0 and  sawjuly >=5:
            text ("{b}Cynthia's Quest{/b}")
            text ("I should check on Cynthia and see if she's doing fine. Better go to the guild in the afternoon.")
        
        if cynthquest5 >= 1 and cynthboots == 1 and cynthquest6 == 0:
            text ("{b}Cynthia's Quest{/b}")
            text ("Wait a few days.")
        
        if cynthquest6 == 1 and cynthkiss == 0 and savecynthia == 1:
            text ("{b}Cynthia's Quest{/b}")
            text ("Go to the academy.")
        
        if cynthquest6 == 1 and cynthkiss == 0 and savecynthia == 0 and cynthmemloss == 0:
            text ("{b}Cynthia's Quest{/b}")
            text ("Go to the academy.")
            
        if cynthkiss >= 1 and cynthdate == 0:
            text ("{b}Cynthia's Quest{/b}")
            text ("I've got a date with Cynthia! I should talk to her at the guild when I'm ready.")
            
            
        if sawjuly <5 and cynthquest5 >= 1:
            text ("{b}Cynthia's Quest{/b}")
            text ("Progress in July's quest.")
            
            
            
        
           
            
            
        
            
                
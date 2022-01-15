define flash  =  Fade(0.1, 0.0, 0.5, color="#fff")
define u = Character("Uncle Pete", color = "#e6ccb3")
define g = Character("Gabrial", color = "#DB93FF")
define s = Character("Scarlet", color = "#EFC667")
define b = Character("Boris", color = "#e6ccb3")
define t = Character("Taliya", color = "E08B8B")
define e = Character("Evelyn", color = "#D2E5B3")
define sa = Character("Sander", color = "#e6ccb3")
define j = Character("July", color = "#FFB575")
define l = Character("Lori", color = "#ACA5CB")
define me = Character("Mervin", color = "#e6ccb3")
define c = Character("Cynthia", color = "#FF7F7F")
define m = Character("Megan", color = "#e6ccb3")
define tr = Character("Triss", color = "#e6ccb3")
define th = Character("Thea", color = "#FF893A")
define n = Character("Nessa", color = "#e6ccb3")
define mi = Character("Milly", color = "#e6ccb3")
define a = Character("Aerin", color = "#81EA82")
define z = Character("Zenelith", color = "#e6ccb3")
define le = Character("Leshek", color = "#e6ccb3")
define he = Character("You", color = "#B3C6FF")
image RinPatch = im.Scale("RinPatch.png", 1280, 720)

label splashscreen:
    scene splashlogo with fade
    pause
    scene splashwarning with fade
    pause
    scene 18over with fade
    pause
    scene warning with fade
    pause
    scene RinPatch with fade
    pause
    return

label start:


    scene black
    play music "windhowl.mp3"
    pause
    show text " {color=#fff}All the choices you make will affect the final outcome of the game. {/color}"
    with dissolve
    pause
    hide text with dissolve
    pause
    show text " {color=#fff}Certain choices you make can lead to character deaths which will completely terminate their quest line.{/color}"
    with dissolve
    pause
    hide text with dissolve
    show text " {color=#fff}Choose wisely.{/color}"
    with dissolve
    pause
    hide text with dissolve
    pause
    show text "{color=#fff}{i}Mom! Dad!{/color}"
    window hide
    pause
    hide text with dissolve

    scene mcsml with dissolve
    pause
    scene jumpscare1
    pause
    he "We need to go!"

    he "They're coming!"
    pause
    scene talkdream

    he "We need to go! NOW!!!"
    stop music
    pause 0.3
    show animation1
    pause
    play music ("home.mp3")
    hide animation1
    scene wakeup3
    "{i}Ugh... That dream again."
    "{i}What were they saying?"
    "{i}......"
    "{i}It sounded like-"
    scene wakeup4
    "{i}Wait... the sun is already up!"
    scene wakeup5
    "{i}Shit! That means I'm late! Oh man, I overslept!"
    "{i}Damn it, looks like I'm gonna be late on the first day of Academy!"
    show text "{color=#fff}You quickly get up and get changed.{/color}" at truecenter
    with dissolve
    pause
    hide text with dissolve
    scene mcroomblur
    show animation2

    he "Time to go."
    hide animation2
    show thinkmc

label trait:
    scene traitsbg with fade
    "Bunis" "This feature is still a work in progress. More content will be added in the future."
    window hide
    show text "{color=#fff}Choose your character trait.{/color}"
    with dissolve
    pause
    hide text with dissolve
    call screen traits


    pause


label out1:
    scene villageback with fade
    show thinkmc with easeinright
    "Mmh... If I remember correctly, the Academy building should be next to the village library."
    show sadtalkuncle with easeinleft
    if chartrait == 1:
        $ magiclvl += 1

    if chartrait == 2:
        $ swordlvl += 1

    if chartrait == 3:
        $ bowlvl += 1
    hide thinkmc
    show suprised
    u "*pant* *pant*"
    hide suprised
    show lookdownsupmc
    u "Oof!"
    show suprised
    hide lookdownsupmc
    show sadtalkuncle
    u "Thank god your still here."

    show unclenormal
    hide suprised
    hide lookdownsupmc
    show talkwamc
    he "Uncle Pete... what's up? "
    hide talkwamc
    show smilemc
    show uncletalk
    u "huff... huff... Hey kid."
    u "It's your first day of the Academy, right?"
    hide uncletalk
    show unclenormal
    show talkmc
    he "Yeah, I'm heading there right now."
    hide talkmc
    show smilemc
    hide unclenormal
    show uncletalk
    u "Then I want you to have this."
    scene sword with fade
    he "What?! Really?"
    u "Of course. It's my old sword."
    he "Wow... Uncle, I don't know what to say... are you sure?"
    u "Yeah. An old fisherman like me has no use for it now."
    menu:
        "Thank you so much, Uncle.":
            scene villageback
            show unclesmilet
            show talksadhappymc
            he "Thank you so much, Uncle."
            show screen notice
            pause
            hide screen notice
            $ good += 5
            $ unclerel += 10
            show uncletalk
            show normalmc
            u "No problem, kiddo!"
            hide uncletalk
            show unclenormal
            hide talksadhappymc
            show talkwamc
            he "This sword looks really well made. How did you even get it?"
            hide talkwamc
            hide unclenormal
            show normalmc
            show unclesmilet
            u "You know, I used to be a traveling merchant back in the day, right?"
            u "I come by things like this all the time."
            hide unclesmilet
        "Well, whatever give it here. I'm late.":
            scene villageback
            show unclesmilet
            show talkmc
            "Well, whatever give it here. I'm late."
            $ bad += 10
            $ unclerel -= 10
            show saduncle
            show screen notice2
            pause
            hide screen notice2
            pause
            hide saduncle

    hide normalmc
    show normalmc
    show uncletalk
    u "Oh, and another thing."
    u "Gabrial's back in town."
    u "She'll be at the Academy too."
    hide normalmc
    hide uncletalk
    show unclenormal
    show talksadhappymc
    he "Really? It's been almost six years since she left."
    hide unclemormal
    hide talksadhappymc
    show normalmc
    show uncletalk
    u "I guess she finished her studies at Westian."
    show talkhappymc
    he "Yeah."
    hide talkhappymc

    u "She was the only friend you've made when I first brought you to Randel. Do you remember that?"
    he "Yeah."
    u "You two would do everything together... Heh, those were the days."
    u "I used to imagine the two of you getting married and settling down here."
    show angry
    he "Uncle Pete!"
    show unclesmilet
    u "Hahaha, just messing with you, kid... Hahaha, look how red your face is."
    "{i}Uncle Pete really likes to make fun of me..."
    u "Don't take anything this old geezer says seriously. You just go out there and do your best, you hear me?"
    show talksadhappymc
    hide angry
    "I will..."
    show talksadhappymc
    he "{i}Shit, I forgot I'm late!"
    he "Nice talking to you, Uncle. But I gotta go now, I'm already late."
    he "Bye!"
    he "And thanks for the sword!"
    show normalmc
    pause
    hide talkmc
    hide talksadhappymc
    hide normalmc with easeoutleft
    hide uncletalk
    hide unclesmilet
    hide unclenormal
    hide saduncle
    hide unclemormal
    show ucletalkturn
    hide sadtalkuncle
    u "No problem!"
    u "Ah... They grow up so fast."
    stop music
    scene academy with fade
    show normalmc with easeinright
    he "{i}I finally made it. It looks like I'm not too late."
    he "{i}It looks bigger from the outside..."
    hide normalmc
    show thinkmc
    he "{i}......"
    he "{i}Is that girl in the hoodie staring at me?"
    he "{i}Why is she staring at me?"
    hide thinkmc
    show blushsmilemc
    menu:
        "I think she likes me...":

            he "{i}I guess she likes me...?"
            he "......"
            he "{i}How is that the first thing that comes to my head?"
            he "{i}Man, I suck."

        "I guess it's nothing.":
            he "{i}I guess it's nothing."
    hide blushsmilemc
    show suprisedblushmc
    he "{i}Shit! She's coming this way!"
    he "{i}Just relax, act cool."
    hide suprisedblushmc
    scene academytalkblr
    show suprisedblushmc
    show talkgabe
    "{color=#DB93FF}Hoodie girl" "Hi."
    show normalgabe
    he "{i}She just talked to me."
    he "......"
    pause
    he "{i}I should probably say something..."
    menu:
        "Hey.":
            show blushtalkhappymc
            he "Hey."
            hide normalgabe
            hide blushtalkhappymc
            hide normalgabe
            show normalmc
            show talkgabe
            "{color=#DB93FF}Hoodie girl" "It's so good to see you again. It's been so long."

        "Hey, babe.":
            "{i}Ok, be confident. Girls like that."
            "{i}...I think."
            pause
            hide suprisedblushmc
            show talkwamc
            he "Hey, babe."
            pause
            show wagabe
            "{i}Shit! I guess she didn't like that."
            pause
            hide wagabe
            hide normalgabe
            hide talkwamc
            show normalmc
            show talkgabe
            "{color=#DB93FF}Hoodie girl" "...It's good seeing you too. It's been so long."

    show suprised
    pause
    show talkwamc
    he "Do I know y-"
    he "Wait, Gabe, is that you!?"
    hide talkgabe
    hide talkwamc
    show normalmc
    show talkwagabe
    g "Of course it's me, dummy!"
    he "Sorry, I coundn't recognize you."
    g "You couldn't recognize me? Really? I'm your best friend!"
    hide talkwagabe
    show normalgabe
    show talksadhappymc
    he "How could I? You look totally different!"
    show talkwagabe
    show smilemc
    g "Really?"
    he "Yeah."
    menu:
        "You look kinda shifty.":
            hide smilemc
            show talksadhappymc
            he "I don't know... you look kinda shifty with the hoodie."
            show wagabe
            pause
            hide wagabe
        "You look cute.":
            $ gaberel += 5
            show blushtalkhappymc
            he "You look kinda cute with the hoodie."
            show cutegabe
            g "......"
            g "It's not supposed to look cute."
            show screen notice
            pause
            hide screen notice
            show worriedblushdgabe
            show talkwamc
            he "Oooh, I see."
            g "Wh-what?"
            he "You're going for that {b}mysterious{/b} look, aren't you?"
            hide worriedblushdgabe
            show smilemc
            show cutegabeu
            g "N-no."
            he "You're trying to look cool, but it's not working at all. Hahaha."
            hide cutegabe
            show angrygabeblush
            show smileecmc

            show yellblushgabe
            g "Come on, man! I put a lot of effort into this outfit!"
            g "And I'm not trying to act cool, ok!?"
            he "Ok, ok, I was just messing with you."
            g "Jeez, I forgot how much of a jerk you can be."
            hide yellblushgabe
            show angrygabeblush
            hide worriedblushdgabe
            hide angrygabeblush
            hide cutegabeu
            hide smileecmc
            hide blushtalkhappymc
    hide talkwagabe
    show talkwamc
    show normalgabe
    he "Heheh... So, how was Westian?"

    show smilemc
    show talkgabe
    g "It was... ok."
    hide talkgabe

    show talkwamc
    he "I guess you're a very powerful mage now, aren't you?"
    hide talkwamc
    show normalmc
    show talkgabe
    g "No, idiot. They only teach how to be fluent in Mardenese at Westian. I only read and studied the spells. Using them is a whole different story."
    hide talkgabe
    show talkmc

    he "What? So that means you know all the spells but can't use them?"
    hide talkmc
    show smilemc
    show talkgabe
    g "Yeah, that's why I came here. They say that the new magic arts teacher is really good."

    hide smilemc
    hide talkgabe
    show talkwamc
    he "So... you spent six years reading spell books?"
    hide suprised
    hide talkwamc
    hide talksadhappymc
    show normalmc
    show talkgabe
    g "Yeah, pretty much."
    show normalgabe
    show talksadhappymc
    he "That... sounds kinda boring."
    hide suprised
    hide talksadhappymc
    show normalmc
    show talkwagabe
    g "...Kinda."
    g "So... enough about me, How's your life?"
    if chartrait == 1 :
        g "Still a shut-in reading books all day?"
        show angry
        he "Shut-in? You're one to talk. You were the same."
        g "I definitely went out more than you did. You wouldn't even go to the library, I had to bring all the books to your lazy ass."
        hide angry
        show talkwanmc
        he "Fine, you have a point. I just liked staying home ok."
        g "So, who brought you the books after I left? ...Oh wait, let me guess, Uncle Pete?"
        hide talkwanmc
        show talksadhappymc
        he "Yeah."
        g "What a lazy head."
        he "Ok, ok, I'm better now, see? I'm going out more now."
        g "Oh yeah, of course."
        hide talksadhappymc
        "{i}Gabe's right. She was the only friend I had when I was little. She would always come to my house with books and the both of us would read all day."
    if chartrait == 2:
        g "Still getting beaten up all the time?"
        show angry
        "Beaten up? I never got beaten up!"
        g "Hahahah... I wonder who that boy was? The one I bandaged up all the time every time he'd come to my house all bruised up."
        he "That happened like one time."
        g "Hmm... Ok, whatever you say, tough guy."
        "{i}Gabe's right. I really did go to her every time after I got into a fight. She always comforted me."
        show talkmc
        hide angry
        he "I'm not that much of a hothead now"
        g "Yeah. Your limbs are intact, so I guess you're right."
        show angry
        hide talkmc
        he "What's that supposed to mean?"
        g "Hehehe..."
        hide angry
    if chartrait == 3:
        g "How's the gang?"
        show talkwanmc
        he "The gang?"
        g "Yeah, the gang, your buddies. The guys you spent most of your time playing with."
        he "Oh, yeah... We haven't hung out in a while."
        g "What, really?"
        he "Yeah."
        g "Why?"
        he "Eh..."
        he "I guess we grew up and started having better things to do."
        g "That's sad. Man, you guys were running around all day."
        hide talkwanmc
        show talksadhappymc
        he "Well, it's not like we hate each other."
        he "{i}Thinking back, why exactly did we stop hanging out? We were so close."
        hide talksadhappymc

    g "Ok, that's enough chatting. Let's go to the class, shall we?"
    show talkwamc
    he "Sure. After you, ma'am."
    g "Hehehe..."
    scene academytalkblr
    show normalgabe
    show talkhappymc
    pause
    show normalmc
    hide normalgabe with easeoutright
    "{i}Gabe's really changed a lot. It was really nice talking to her after all this time."
    pause
    show suprised
    "Groundskeeper" "Hey, lad, wait up!"
    show normalgk with easeinleft
    hide suprised
    pause
    show talkgk
    "Groundskeeper" "Hey, I got a little job for you... Can you go and get them boxes to the store room."
    hide talkgk
    show talkmc
    he "Why me? Aren't you the groundskeeper here?"
    he "It's your job."
    show talkgk
    hide talkmc
    "Groundskeeper" "You kids these days! I got enough work as it is. Just go and move the boxes, will ya?"
    "Groundskeeper" "I already sent another one of you brats to clean the place up."
    hide talkgk
    show talksadhappymc
    he "...But my class is about to start."
    hide talksadhappymc
    show talkgk
    "Groundskeeper" "So what, who needs em? Now take the boxes and go!"
    scene black
    show text "{color=fff}You take the boxes to the store room." at truecenter
    with dissolve
    pause
    hide text with dissolve
    scene storeroomblr
    show normalmc with easeinright
    pause
    show thinkmc
    he "{i}Phew, I finaly made it. Damn those boxes were heavy..."
    he "{i}......"
    he "{i}Wait, didn't the groundskeeper send another student to clean this place? It looks really dusty."
    he "{i}I bet the guy he sent here to clean the place bailed out. I should've done the same."
    he "{i}Anyway, my job here is done. I gotta ru-"
    "Unknown voice" "Zzz..."
    hide thinkmc
    show suprised
    he "What the hell was that?"
    "{color=#EFC667}Unknown voice" "Zzz......"
    he "{i}There it is again."
    hide suprised
    show thinkmc
    "{i}It sounds like someone's sleeping."
    "{i}It's coming from one of those lockers."
    scene sleepmclose with fade
    "{color=#EFC667}Unknown voice" "ZZZZ........"
    he "There's someone inside."

    menu:
        "Open":
            scene sleepm with vpunch
            pause
            he "{i}Shit!"
            he "{i}Who is this? Wait, is this the person the groundskeeper sent?"
            scene sleepm
            pause
            he "{i}Judging by her outfit, she looks like a mage."
            he "{i}Damn mages and their sexy outfits."
            menu:
                "Peek":
                    $ peek += 1
                    he "{i}Man, her outfit is so revealing. It's making me super horny right now."
                    he "{i}Might as well take a little peek..."
                    scene sleepm2 with dissolve
                    pause

                    he "{i}She's not wearing any panties!"
                    he "{i}Ok... slowly... just a little more..."
                    scene sleepm2
                    pause
                    scene sleepm2 with hpunch
                    he "{i}Shit! She's waking up, damn it!"
                    scene storeroomblr
                    show normalmc
                    show yawnm
                    "{color=#EFC667}Mage ""Yaaawn..."
                    hide yawnm
                    show talkm
                    "{color=#EFC667}Mage" "Hi."
                    show talkmc
                    he "Hi..."
                    hide talkmc
                    "{i}Why... Why, Lord, I was so close."
                    jump mage2
                "Wake her up":
                    he "{i}I'm not a damn pervert. I gotta wake her up."
                    he "Hey, wake up!"
                    "{color=#EFC667}Mage" "Huh, wa-wait what?"
                    jump mage
        "Knock":
            he "{i}I should knock, that's the decent thing to do, right?"
            he "Hey, wake up!"
            "You knock on the locker a few times"
            "{color=#EFC667}Mage" "Whoa, ow, wh... What the fuck?"
            he "{i}Sounds like she's waking up."
            jump mage

label mage:
    scene storeroomblr
    show normalmc
    show yawnm
    "{color=#EFC667}Mage" "Yaaawn..."
    hide yawnm
    show talkm
    "{color=#EFC667}Mage" "Hello there."
    hide talkm
    show normalm
    show talkmc
    he "Hi."
    hide talkmc

label mage2:
    show normalm
    show talkm
    "{color=#EFC667}Mage" "Man, how long was I out? That was one good nap."
    hide talkm
    show talksadhappymc
    he "I don't know."
    he "...Did the groundskeeper send you here to clean the place?"
    hide talksadhappymc
    show sadtalkm
    "{color=#EFC667}Mage" "Oh shit, I totally forgot! Yeah, yeah, he did send me here, but then I saw this small locker. It looked so cozy. So I went in, and before I knew it, I fell asleep!"
    hide sadtalkm
    show sadsmilem
    show talkwamc
    he "Just like that."
    hide talkwamc
    hide normalmc
    show smilemc
    hide sadsmilem
    show talksleepm
    "{color=#EFC667}Mage" "Just like that."
    hide talksleepm
    show talkhappymc
    he "So, it's your first day too, huh?"
    hide talkwamc
    hide happytalkmc
    show talkm
    "{color=#EFC667}Mage" "Hmm... Oh, yeah."
    "{color=#EFC667}Mage" "The name's Scarlet by the way!"
    hide talkm
    show talkhappymc
    he "Nice to meet you."
    hide talkhappymc
    show smilemc
    pause
    show wasmilem
    pause
    hide smilemc
    show talkwamc
    he "What?"
    hide talkwamc
    show smilemc
    show talkwam
    s "And you are?"
    hide talkwam
    show talksadhappymc

    $ mc = renpy.input("Oh, sorry, I'm...")
    if mc == "":
        s "What? You didn't say anything."
        $ mc = renpy.input("I said my name is...")
        if mc == "":
            "Bunis" "Hello, I'm the developer! Please enter a name. If not, a default name will be given."
            $ mc = renpy.input("My name is...")
            if mc == "":
                "Bunis" "Ok, so you're going with the default name then?"
                "Bunis" "You will now be called Jack."
                $ mc = "Jack"

    show talkwam
    hide talksadhappymc
    s "Ok, [mc], now are you going to help me clean this place?"
    hide talkwam
    show angry
    mc "What? That's supposed to be your job!"
    hide angry
    show angrynmc
    show sadtalkm
    s "Oh, come on, [mc], help me out! I can't do all this by myself!"
    hide sadtalkm
    show plsm
    s "Pweeease??"

    menu:
        "I'm late for class, sorry.":
            hide angrynmc
            hide plsm
            show talksadhappymc
            show sadm
            mc "I'm late for class, sorry, I gotta go."
            hide talksadhappymc
            show talkwanmc
            mc "Aren't you coming? Our class must've started by now."
            show normalmc
            show sadtalkm
            s "I've still got cleaning to do. You go ahead, I'll come after I finish this up."
            show talkwanmc
            mc "Ok, don't be late."
            jump class1
        "Ok, fine!":
            $ scarel += 10
            hide angrynmc
            hide plsm
            show angry
            mc "Ok, fine!"
            show screen notice
            pause
            hide screen notice
            hide angry
            show angrynmc
            show teethecm
            s "Yaaay!"
            show talkmc
            mc "Uhmm... But I don't have a broom."
            hide teethecm
            show talkm
            hide talkmc
            s "You can have mine!"
            show normalm
            hide talkm
            show talkwanmc
            mc "Then what are you going to use?"
            hide talkwanmc
            show talkm
            s "Oh, I have my staff here. I can turn it into just about anything."
            hide talkm
            show talkwamc
            hide angrynmc
            mc "Really? Wow, that's cool."
            show normalmc
            hide talkwamc
            show talkwam
            s "Yeah, I know, I use it for {b}all{/b} kinds of things..."
            show thinkmc
            show anythingm
            hide talkwam
            pause
            show talkwanmc
            mc "{i}Wait, what's with that look? Does she mean what I think she means?"
            show talksadhappymc
            mc "Uhm... yeah... haha... that's really convenient..."
            hide talksadhappymc
            hide anythingm
            show yawnm
            s "...You didn't get it?"
            s "{i}sigh...{/i} I thought kids these days were more open about these stuff."
            hide yawnm
            show thinkmc
            mc "What?"
            s "Urg... just forget it."
            mc "{i}She did mean it! ...Or it just could be my pervy brain."
            "The two of you start cleaning."
            show sweep with fade
            "After about a minute, Scarlet dozes off."
            show sweep with vpunch
            mc "You're asleep AGAIN?!"
            s "Yeah I'm so tired... but see, I'm still cleaning."
            mc "That's cheating."
            s "Zzz... Zzz..."
            mc "{i}What's with that girl? Always falling asleep... And how is she so good at magic? She's supposed to be a recruit."
            mc "{i}Wait, Is this the minimum standard? This girl's casting spells and has a shape-shifting staff while I can barely swing a sword..."
            scene black
            show text "{color=fff}You finally finish cleaning up the place." at truecenter
            with fade
            pause
            hide text with fade
            scene storeroomblr
            show normalmc
            pause
            show yawnm
            pause
            hide yawnm
            show talkm
            s "Yay! We did it!"
            hide talkm
            show normalm
            show talkwanmc
            mc "Technically, it was me and your staff."
            hide talkwanmc
            show teethecm
            s "Hehe..."
            show talkmc
            mc "Ok, now we seriously need to go."
            hide talkmc
            show uhm
            s "We?"
            show talkwanmc
            mc "Yeah {b}we{/b}! Aren't you coming? Our class must've started already!"
            hide talkwanmc
            show sadtalkm
            s "Oh yeah, I'm coming. You go ahead. I have to get some stuff."
            show sadsmilem
            show talkwanmc
            mc "What- Ok. Whatever, I'm going. Don't be late."
            hide sadsmilem
            hide talkwanmc
            hide normalmc
            show sadtalkm
            s "O-Ok... see you soon!"
            show sadsmilem
            mc "Bye!"

label class1:
    scene black
    show text "{color=fff}You go to the class door. You slowly poke your head in and scout out the surroundings." at truecenter
    with fade
    pause
    hide text with fade
    scene lecture with fade
    "The class has already started, but the teacher hasn't noticed you yet. You look around for a space to slowly creep in."
    "Then you see someone waving from the corner of the class."
    scene class with fade
    "It's Gabrial. Looks like she saved you a seat."
    "You slowly duck, stealthily move to Gabrial and get seated."
    scene lecturetalk with fade
    g "What took you so long?"
    mc "Uhh... I'll explain later. What did I miss?"
    scene lecture
    g "Umm... you didn't miss anything, actually."
    g "He's just been rambling on and on about rules and discipline all this time."
    mc "Ok, that's good to know. Thank you for saving me a seat, by the way."
    scene lecturetalk
    g "Ohh, it's nothing."
    scene black
    show text "{color=fff}The class goes on for a while and you quickly get bored." at truecenter
    with fade
    pause
    hide text with fade
    scene lecturetalk
    mc "{i}Scarlet still hasn't shown up... she must have fallen asleep again."
    mc "Man, this is so boring..."

    menu:
        "Look around the class":
            $ sawcynth += 1
            mc"{i}Might as well look around the class. Maybe I'll spot some hot chicks."
            "You look around the class slowly so that no one notices you... especially Gabe..."
            "Then your eyes fix on a girl."
            scene stare with fade
            mc "{i}Wow, she's pretty."
            mc "I haven't seen her before..."
            g "Cynthia Gardner."
            scene lecture
            mc "Wh-What, who?"
            g "I know you were staring at her, [mc]."
            menu:
                "No, I was not.":
                    mc "No, I was not..."
                    g "Pfft. Yeah, right."
                "Ok, fine, you caught me.":
                    mc "Ok, fine, you caught me... So what? Can't a guy look at a hot girl once in a while?"
                    g "Jeez, [mc], I didn't know you were such a perv."
                    mc "Perv?! I was just looking at her!"
                    g "Yeah, right."
            mc "Whatever... is she new in town? I've never seen her before."
            g "Yeah, she's from Thane."
            mc "In the east?"
            g "Yeah. Thane is under high alert, didn't you know? "
            g "Since it's right below Fort Hern. If the fort goes down, they'll be the first to get attacked."
            mc "But, why now? Hern's still holding right?"
            g "Yeah, but for how long? They say the Demon King's army is getting stronger."
            menu:
                "It will be up to us to protect it then.":
                    mc "It will be up to us to protect it then."
                    g "......"
                    g "Pfftthahahahaha! \"It will be up to us to protect it.\" ...Hahaha, you should hear yourself!"
                    mc "What? I'm serious."
                    g "Haha! Yeah, yeah. Ok, almighty [mc], you'll be there to save us!"
                    mc "...Meanie."
                "Say nothing":
                    mc "Hmm."
            g "Anyway, coming back to Cynthia."
            g "From what I've heard she's a very nice person. Friendly, caring... and beautiful of course."
            mc "Hmm..."
            g "Don't even think about it, [mc], you don't stand a chance. All the boys in the Academy are going after her."
            mc "That's harsh."
            g "What? I'm just being honest."
            "The class goes on for a while."
            mc "{i}Urrgh, this is so boring... I'm starting to fall asleep..."
            menu:
                "Look at Cynthia":
                    mc "{i}Might as well look at Cynthia again."
                    "You slowly look at Cynthia from the corner of your eye so that Gabe doesn't notice."
                    scene stare
                    mc "She looks so pretty..."
                    scene stare
                    pause
                    mc "Like... an... angel..."
                    scene stare1 with dissolve
                    mc "...an...gel..."
                    scene black with dissolve
                    pause
                    g "[mc], wake up! Goddammit, [mc]! Wake up!"
                    "You hear Gabe whisper harshly as she nudges you with her elbow."
                    scene lecturetalk with vpunch
                    "You automatically stand up."
                    b "Glad to see you're up... Mister...?"
                    mc "[mc], sir."
                    b "Ok, Mr. [mc], I see you found the lesson to be boring... Then I assume you already knew what I was teaching?"
                    mc "No, sir, I... Wha-"
                    $ caughtboris += 1
                    b "Ok then. Let's see, Mr. [mc], would you kindly tell me what I was teaching just now?"
                    menu:
                        "History of Merdian":
                            mc "History of Merdian?"
                            b "It seems like you haven't paid the slightest attention... GET OUT OF MY CLASS, NOW!"
                            jump out
                        "Forts of Merdian":
                            mc "Forts of Merdian."
                            b "Ok, it seems you paid more attention than I initially thought."
                            b "Ok then, Mr. [mc], what is the name of the fort located at the east border of Merdian?"
                            if chartrait == 1:
                                play sound ("chime.mp3")
                                $ renpy.notify("Bookworm check: Success!")
                                mc "{i}Wait I've read about this. It's Fort Hern."
                            menu:

                                "Fort Hern":
                                    mc "Fort Hern."
                                    b "Oh... uhm... It seems like you actually did know... O-Ok then, sit down and don't let me catch you dozing off again."
                                    "You sit down and Gabe gives you a thumbs up."
                                    g "Nice work, [mc]."
                                    "The class goes on for what feels like an eternity."
                                    jump out
                                "Westian":
                                    mc "Westian."
                                    b "I'm sorry, Mr. [mc], but that is incorrect... I'll forgive you this time. Don't let me catch you dozing off again... you may sit down. "
                                    "The class goes on for what feels like an eternity."
                                    jump out
                                "Mordor":
                                    mc "Mordor."
                                    b "Mordor? ...What? Was that some place you saw in your dreams while you were sleeping, Mr. [mc]?"
                                    b "I'm sorry, Mr. [mc], but that is incorrect... I'll forgive you this time. Don't let me catch you dozing off again... you may sit down. "
                                    "The class goes on for what feels like an eternity."
                                    jump out
                        "Angels":
                            mc "Umm... Angels?"
                            b "WHAT?! ...GET OUT OF MY CLASS, NOW!"
                            jump out
                "No, I have to focus. This might be important.":
                    he "{i}No, I have to focus. This might be important."
                    b "Merdian has four main forts located at its borders."
                    scene lecture
                    pause
                    scene lecturedraw
                    b "In the south we have Dermis, in the north we have Winden, in the west Dorm and in the east Hern..."
                    b "...As you know, the Dark Lands are beyond Hern to the east. That is where the Demon King's army is stationed."
                    b "Which means Hern is the last defense we have against the Demon King's army."
                    b "It's a well-known fact that the Demon King is dead... but his generals and his army still remain. Though weakened, they are far greater in number. So remember, the threat still remains."
                    b "Luckily, Fort Hern is one of the strongest and oldest forts in Merdian, and for years it has held off countless attacks."
                    jump DemonKing

        "No, I have to focus. This might be important.":
            mc "{i}No, I have to focus. This might be important."
            b "Merdian has four main forts located at its borders."
            scene lecture
            pause
            scene lecturedraw
            b "In the south we have Dermis, in the north we have Winden, in the west Dorm and in the east Hern..."
            b "...As you know, the Dark Lands are beyond Hern to the east. That is where the Demon King's army is stationed."
            b "Which means Hern is the last defense we have against the Demon King's army."
            b "It's a well-known fact that the Demon King is dead... but his generals and his army still remain. Though weakened, they are far greater in number. So remember, the threat still remains."
            b "Luckily, Fort Hern is one of the strongest and oldest forts in Merdian, and for years it has held off countless attacks."
            jump DemonKing

label DemonKing:
    g "Did you know that the Demon King died in the Hern siege?"
    mc "Really?"
    g "Yeah, though no one is really sure about it. They say the one who slayed the Demon King suddenly vanished."
    mc "What do you mean?"
    g "I heard that he just disappeared."
    mc "What, you mean that he ran away?"
    g "Yeah, something like that."
    mc "Why?"
    g "Who knows? Some say that when he killed the Demon King, a part of its soul was transfused with his slayer."
    g "So he sealed himself off somewhere so that he could contain the Demon King."
    mc "Why not just kill himself?"
    g "What?"
    mc "I mean, if he killed himself, wouldn't the Demon King die with him?"
    g "Who knows. There may be a reason for it."
    g "Maybe if he killed himself, the Demon King would be released."
    g "And it would possess someone else again."
    mc "Hm... yeah. That would make sense."
    "You listen to the rest of the lesson until class ends."
    jump out

label out:
    scene academytalkblr with fade
    show normalmc
    show normalgabe
    pause
    show talkhappymc
    mc "Well, that was boring as hell. What's our next class?"
    hide talkhappymc
    show talkgabe
    g "It's Magical Arts. Come on, let's go quick."

label mageclass:
    scene lecturemage1 with fade
    g "The teacher is late!"
    mc "Yeah."
    "The door opens and the teacher quickly runs to the board."
    scene lecturemage3
    s "Good morning class, sorry I'm late."
    mc "{i}WHAT!"
    mc "{i}Th-That's Scarlet. She's our magical arts teacher?! What the hell?"
    scene lecturemage2

    g "Wow, she's younger than I thought. She almost looks our age."
    mc "......"
    g "[mc]?"
    mc "Y-Yeah, she does..."
    scene lecturemage3
    "The class goes on for a while and after some time, it ends."
    "You go and meet up with Scarlet before she leaves."
    scene lecturemage1
    show normalm
    show normalmc
    show talkmc
    mc "Excuse me, Miss Scar-"
    hide talkmc
    show talkwam
    s "Oh, hello there, [mc]. And please just call me Scarlet."
    hide talkwam
    show talkmc
    mc "B-But, y-you were..."
    hide talkmc
    show talkwam
    s "Yeah, I know, I know you're surprised."
    s "I'm sorry I didn't tell you earlier."
    hide talkwam
    show talkwanmc
    mc "But, why?"
    hide talkwanmc
    show talkm
    s "I don't know, it was kinda fun!"
    hide talkm
    show talkwamc
    mc "So the groundskeeper also mistook you for a student?"
    hide talkwamc
    show teethm
    s "Yeah, it's my first day here anyway. I guess he didn't know."
    hide teethm
    show talkwanmc
    mc "And you didn't say anything?"
    hide talkwanmc
    show talkwam
    s "Nope!"
    hide talkwam
    show talkwanmc
    mc "Why?"
    hide talwanmc
    show talkm
    s "It just feels great to be young again you know?"
    hide talkm
    show talkwanmc
    mc "What?"
    hide talkwamc
    show talkwam
    s "I'm older than you think, [mc]."
    hide talkwam
    show talkwamc
    mc "But you look very young..."
    show talkm
    hide talwamc
    s "I know! It's because of a de-aging spell."
    show talkwamc
    hide talkm
    mc "De-aging spell?"
    mc "Never heard of it before."
    hide talkwamc
    show talkm
    s "Makes sense. I don't mean to brag, but the de-aging spell is an S-class spell. Many mages don't use it."
    hide talkm
    show talkmc
    mc "Wow... So, does that mean you're like... hundreds of years old?"
    hide talkmc
    show sadtalkm
    s "I'm not that old, you dolt."
    hide sadtalkm
    show talkwanmc
    mc "Ok, how old are you then?"
    show talkm
    hide talkwanmc
    s "Fifty-three."
    hide talkm
    show talkmc
    mc "Still a bit old."
    hide talkmc
    show smileecmc
    show talkwam
    s "Oh, shut up, [mc]."
    mc "Hehe..."
    show talkwam
    s "Ok kid, you better go now. I've got another class."
    hide talwam
    show talkwamc
    mc "Ok, now you're really starting to sound old."
    hide talwamc
    show smilemc
    show teethecm
    s "Ahah, see you, [mc]."
    hide teethecm
    show talkwam
    s "And also, [mc], I hope this doesn't change anything."
    s "we're still friends, right?"
    hide talkwam
    show talkhappymc
    mc "......"
    mc "Yeah."
    s "Glad to hear it."
    hide normalm with easeoutleft
    if peek > 0:
        s "Oh, and another thing. The next time I catch you peeking..."
        s "I'll kill you."
        show suprised

label arena:
    scene black with fade
    show text "{color=#fff}You then go to the arena for your combat training class." at truecenter
    with fade
    pause
    hide text
    scene arena with fade
    "You see all the students gathered at the arena. You quickly join them."
    "You hear random students talking."
    "Student 1" "Did you hear General Taliya is here? She came to train us."

    "Student 2" "What! No way, are you serious?"
    "Student 1" "Yeah, man."
    show normalt with easeinright
    "Taliya marches in front of the students."
    show aten
    t "Attention students!"
    hide aten
    show talkt
    t "My name is Taliya Bridges. As you may know, I am here to train all of you new recruits."
    t "Because Randel is one of the closest towns to Hern, we need as many soldiers from this town as possible."
    t "That is why I personally came to Randel to make sure each one of you will be trained well enough to defend Merdian."
    t "Ok everyone, get ready for training. I'll get into something comfortable as well."
    "Taliya starts to strip down her armor."
    scene tt1
    mc "{i}Man, she has a fit body..."
    "You notice all the other students ogling her as well, but she doesn't seem to notice or care."
    scene tt2
    t "Ok recruits, line up... first I'm going to teach you how to properly use a sword."
    t "Everybody, draw your swords."
    "You reach to grab your sword."
    scene black with flash
    scene tt1
    "A sudden chill runs down your spine as soon as you touch the hilt of your sword."
    mc "{i}What the hell was that?!"
    mc "{i}Argh... my chest is burning..."
    "You almost lose consciousness, but you manage to hold on."
    "After a while, the pain settles."
    mc "{i}Urrrg... That was weird... What was that?"
    scene tt2
    t "Ok recruits, we'll be practicing basic strikes today."
    t "Ok now, let's begin."
    show animationsword
    "You train for a while."
    if chartrait == 2:
        "The training lasted longer than you thought. You were pretty good compared to the other recruits."
    else:

        "The training lasted longer than you thought. At the end your hands feel like they're about to fall off."
    hide animaion
    scene tt2
    t "That's enough for today, recruits. You did a good job. I hope to see you all a lot in the training field."

label schoolend:
    scene academytalkblr with fade
    show normalmc with easeinright
    mc "Man, what a day."
    show normalgabe with easeinleft
    pause
    show talkgabe
    g "Hi, [mc]! How was your combat arts class?"
    hide talkgabe
    show angry
    mc "It was hell, that's what it was."
    hide angry
    g "Heheh."
    show talkgabe
    g "I'm glad I didn't sign up for that!"
    hide talkgabe
    show angry
    mc "Lucky you."
    hide angry
    show talkgabe
    g "Heheh... Well, see you tomorrow, [mc]."
    hide talkgabe
    show talkhappymc
    mc "Wait, Gabe, if you don't mind me asking... Where do you live now?"
    hide talkhappymc
    show talkwagabe
    g "In my old house, silly. Next to the Adventurer's Guild."
    hide talwagabe
    show talksadhappymc
    mc "Oh! Then it won't be hard to find you."
    hide talksadhappymc
    show talkwagabe
    g "Now that I think about it... You always wanted to join the Adventurer's Guild, right? Aren't you going to join?"
    hide talkwagabe
    show talkhappymc
    mc "Yeah. I think I'll be checking it out today before going home."
    hide talkhappymc
    show talkgabe
    g "Really? Good luck then!"
    hide talkgabe
    show talkhappymc
    mc "Thanks, See you later!"
    scene villageback with fade
    show normalmc with easeinleft
    pause
    hide normalmc
    show smilemc
    mc "{i}Time to go to the Adventurer's Guild."
    mc "{i}I've been wanting for this moment for so long..."
    mc "{i}I wanted to wait until I joined the academy so I could train my abilities, guess I don't have anything to wait now."
    mc "{i}And finally they won't kick me out for being too young!"
    hide smilemc with easeoutright

label pguild:
    play music ("aguild.mp3")
    scene adventurersguild with fade
    show normalmc with easeinright
    pause
    show smilemc
    mc "{i}Wow, it's just like I imagined it would be. The warm fire, the stone wall, the bear rug and the finely carved wooden benches. Now this is an Adventurer's Guild!"
    mc "{i}I can't wait to get started. I wonder where I'll join?"
    scene agblr with dissolve
    show talkow with easeinleft
    show suprised
    e "Quick, move aside."
    hide suprised
    show talksadhappymc
    mc "Y-Yes, but, uhm... could you tell me who I should speak to...? I'm here to join the Adventurer's Guild."
    hide talkow
    show talkhse
    hide talksadhappymc
    show smilemc
    e "......"
    e "Oh really? It's nice to see young faces around here for a change."
    e "How old are you, little one?"
    show talkhappymc
    show smilese
    mc "19."
    hide talkhappymc
    show talkhse
    e "Is that so? Well, you gotta go talk to July. She's right over there behind the counter."
    show talkhappymc
    hide talkhse
    mc "Thanks."
    hide talkhappymc
    show lookdownsupmc
    sa "Urghh... Uhmm... Just give one more drink Eve, I can take... it..."
    hide lookdownsupmc
    show talkwase
    e "Shut up, Sander. You had too much and I'm cutting you off!"
    e "Eh... This is my friend, Sander. He just had a little too much today... I'm taking him outside before he throws up all over the place... again."
    sa "It was just 19 beers, Eve... I've had way more beforeee."
    e "Anyway, I gotta go, little one... Welcome to the Guild... Oh, I'm sorry. I didn't get your name."
    show talkhappymc
    mc "[mc]."
    e "Alright, welcome to the Guild, [mc]!"
    hide talkwase
    hide smilese with easeoutright
    hide talkhappymc
    mc "{i}She was nice... So, I've got to go to July."
    scene adgc1 with fade
    mc "{i}What, she's asleep? What the hell is wrong with the women in this town?!"
    mc "Uhm..."

    scene adgc2 with vpunch
    j "Yes...? What brings you to the Adventurer's Guild?"
    mc "{i}Oh shit, she scared me."
    mc "Oh, uhm, I thought tha-"
    j "I was asleep? ...Yeah, I get that a lot... My eyes are just really tiny. Hehehehe."
    mc "......"
    j "So, are you here to join?"
    mc "Yeah."
    j "Ohh, that's nice. How old are you?"
    mc "19."
    j "So you're legally allowed to join... What's your name?"
    mc "[mc]."
    j "[mc], can you sign this paper, please?"
    scene adgc2
    pause
    scene adgc3 with dissolve
    pause
    "You sign the paper."
    scene adgc4
    j "Ok... so now listen closely."
    j "There are five ranks in the guild: Recruit, Bronze, Silver, Gold, and Diamond."
    j "You will start at the Recruit rank. You can progress to the other classes by gaining experience. "
    j "You gain experience by completing quests and slaying monsters. Quests will be assigned according to your respective rank."
    j "When you reach Bronze, you will get your first badge and that makes you an approved adventurer... Only adventurers of Bronze rank and above have the ability to join or form a party."
    j "Here's a sheet which shows the class progression."
    show gn with dissolve
    j "Until you reach level 5, you can't go on any quests. Until then, you can go to the forest and slay beasts to gain experience... But remember, the deeper into the forest you go, the more dangerous the monsters become. Here's a map which shows the areas of the forest."
    show mf with dissolve
    j "If you slay wild boars, please bring them to the Guild."
    mc "Will I get paid?"
    j "Yes... 5 silver per boar."
    mc "Nice."
    j "And here's your exp charm."
    mc "Uhh... What does it do?"
    j "Didn't I tell you?"
    mc "...No."
    j "Oh my goodness, sorry. I'm getting too old for this teehee."
    j "Let me explain. This exp charm will collect a certain amount of exp points every time you slay a monster or complete a quest."
    j "Think of it a some sort progression tracker."
    mc "Oh, cool."
    j "Remeber to wear it at all times. It wont collect exp unless you wear it."
    mc "Ok."
    scene adgc4
    j "That's all for my briefing."
    j "You do have weapons right?"
    mc "Yeah."
    j "Ok, have this... It's just a little help to get you started... Spend it wisely."
    "You received 30 silver."
    $ money += 30
    mc "Thank you, July."
    j "Any more questions?"
    scene adgc3

label qg:

    menu:
        "When can I go on quests?":
            j "When you reach level five. Until then, hunt wild boars or slay monster to gain experience. "
            jump qg
        "Can I slay other monsters?":
            j "You can. Just be careful, most of them are very dangerous. Be sure you are trained enough with your sword and bow before you do."
            j "Also, you should study about these monsters before slaying them. Go to the Library and find The Book of Monsters and study the monsters to find their weaknesses."
            jump qg
        "Where can I get new equipment?":
            j "There's a trading caravan just outside the Guild. You can buy equiment from there."
            jump qg
        "No more questions.":
            mc "No more questions. Thank you!"

    j "See you soon, young adventurer."
    j "Make sure you go check out the Library!"
    mc "Ok, bye, July."
    mc "I can't go home yet then, gotta go check out the library."
    stop music

    scene library with fade
    pause
    show normalmc
    mc "Man, this place looks deserted. I guess the people in Randel aren't big readers..."
    if chartrait == 1:
        mc "It's my first time here as well, even though I was such a bookworm back then."
    show talkl
    show suprised
    scene libraryblr
    show grumpl
    show suprised with vpunch
    "{color=#8C79C6}Stranger" "Hey, who are you?"

    mc "{i}Ah shit, got startled again."
    hide suprised
    hide talkl
    show grumpl
    show talkhappymc
    mc "Uh, I'm [mc]. Can you tell me where I can find the librarian?"
    show talkl
    hide talkhappymc
    show smilemc
    "{color=8C79C6}Stranger" "You're looking at her. I'm Lori, I'm the librarian here."
    show talksadhappymc
    mc "Oh sorry, I-"
    hide talksadhappymc
    show talkl
    l "Enough with the act! Why are you here?"
    l "Hiding from the guards? Hiding from your parents? Or are you waiting for some girl so you can fool around in here?!"
    hide talkl
    show talksadhappymc
    mc "Uhm... No, I'm here to find a book actually."
    hide talksadhappymc
    show normall
    pause
    show talkwal
    l "Wait... Are you actually here to read?"
    hide talkwal
    show talksadhappymc
    mc "...Yeah."
    show talkhl
    l "Really?! Oh my god, we rarely get any actual readers here!"
    hide talkhl
    show talkhsl
    l "I'm sorry if I was a bit harsh before... most people come here just to fool around."
    hide talkhsl
    show talkhnl
    l "So! What's the name of the book you are looking for?"
    hide talhnl
    show smilel
    show talkhappymc
    mc "The Book of Monsters."
    hide talkhappymc
    show talkhnl
    l "Oh! So, that means you are an adventurer?"
    hide talkhnl
    show talkhappymc
    mc "Yeah."
    show talkhl
    l "That's awesome."
    hide talkhl
    show talkhsl
    l "I've always wanted to become one myself but... I am too weak and I'm rather scared of monsters."
    hide talkhsl
    show talkhappymc
    mc "Haha, everyone's scared of monsters."
    mc "And after all, adventures aren't fun without danger, right?"
    hide talkhappymc
    show talkhsl
    l "Hehehe, you're right, [mc]. I bet you'll be a great adventurer.!"
    l "But sorry, [mc], I won't be able to give you the book today. I haven't taken it out in years, so I'll have to look for it... Come back tomorrow, I'll be sure to give it to you then."
    hide talkhsl
    show talkhappymc
    mc "It's ok. I'll come back tomorrow then."
    hide talkhappymc
    show talkhsl
    l "By the way... [mc], are you a student at the Academy?"
    hide talkhsl
    mc "Yeah."
    show talkhsl
    l "If you have any trouble with your studies, feel free to ask... I'll be glad to help."
    hide talkhsl
    show talksadhappymc
    mc "Really? Thanks, Lori, I really appreciate that."
    hide talksadhappymc
    show talkhsl
    l "No problem! I like helping others, y'know... and it gets really boring sitting in here all day."
    hide talkhsl
    show talkhappymc
    mc "Heh, don't worry, I'll be back."
    hide talkhappymc
    hide smilmc
    show talkhnl
    l "Bye!"
    scene black with fade
    scene mcroomn
    pause
    show normalmc
    mc "{i}Finally, I'm home. That was one hell of a day."
    mc "{i}Now I can jump into my bed!"
    "{i}knock knock knock"
    show thinkmc
    mc "{i}Ugh, who is it this late?"
    scene ut1 with fade
    mc "Hello? Who's there?"
    u "Open up, [mc], it's me."
    mc "Oh, Uncle Pete, wait a sec..."
    scene ut2 with dissolve
    u "Hey, kid... I was just passing by, so I came for a quick chat."
    scene ut3 with dissolve
    u "And I brought fish."
    scene ut2 with dissolve
    $ petefish += 1
    mc "Thanks, Uncle Pete, Why don't you come in?"
    u "No, no. I just came for a quick visit and it's already late. How was your first day?"
    mc "It was cool. A bit hectic, but alright... and I saw Gabrial."
    mc "She's changed a lot since I last saw her."
    scene utsmirk with dissolve
    pause
    mc "What?"
    u "She's grown a lot, hasn't she?"
    mc "Yeah?"
    u "...Hmm."
    mc "Wait... again!? Don't you ever get tired of the same joke, uncle?"
    scene ut2 with dissolve
    u "Hahahahaha... I sure don't get tired seeing your face blush every time."
    mc "There's nothing like that, we're just friends, ok!?"
    u "I get it, I get it, I won't bring it up again... Haha."
    u "Anything else?"
    mc "Huh... Oh, I joined the Adventurer's Guild too!"
    u "Really?"
    u "You always wanted join, didn't ya? Ever since you were a little boy. I'm so proud of you, [mc]."
    mc "Thanks, Uncle Pete."
    u "So, what's it like having the house to yourself?"
    mc "It's ok, but you didn't have to leave, Uncle Pete."
    u "Nah, you're a big kid now. You don't want old farts like me staying with ya. And besides, I've always liked the fishing hut more than this dusty old place."
    mc "Hey!"
    u "Heh."
    mc "Oh, and another thing. I had that dream again."
    u "The one with your parents? Was it the same thing?"
    mc "Yeah, but this time I think they said something."
    u "What did they say?"
    mc "It didn't make any sense... it kinda sounded like..."
    scene ut4
    mc "...You are not our son."
    mc "I don't know what it means."
    scene ut2
    u "It's probably nothing. Dreams usually don't make much sense... I've had a lot of weird dreams myself."
    u "Don't worry about it too much, kid."
    mc "Yeah, but I keep seeing it again, and again..."
    u "You just need to get some good rest... Go to sleep earlier."
    mc "Yeah, I really haven't slept much recently."
    u "Ok then, [mc], eat the fish and..."
    mc "Sleep early."
    u "Sleep early. See you, kid."
    mc "Bye, Uncle Pete! Same goes for you... It's too late to go fishing at this hour, you know!"
    u "Hah, smartass!"
    scene ut1 with dissolve
    mc "{i}Anyway, he's right. I better go to bed."
    scene sleep with fade
    mc "Ahh... I've missed you, bed."
    scene black with fade
    pause
    show text "{color=#fff}Would you like to enable cheats?"
    pause
    hide text
    menu:
        "No (Recommended for first time players.)":
            "No cheats for me."
        "Yes (Recommended for players who are coming back.)":
            "No grinding for me."
            $ Cheats += 1
    jump home

image animation1:
    "jumpscare1"
    0.4
    "jumpscare2" with flash
    1.5
    "jumpscare3" with Dissolve(0.5)
    0.3
    "jumpscare4" with Dissolve(0.5)
    0.2
    "jumpscare5"
    0.3
    "wakeup1" with flash
    0.3
    "wakeup2"

image animation2:
    "yawnmc"
    0.5
    "normalmc"

image animationsword:
    "sword1"
    0.5
    "sword2"
    0.5
    repeat
image animationbow:
    "archery1"
    0.5
    "archery2"
    0.5
    "archery3"
    0.5
    repeat

image animationbowgood:
    "archery1"
    0.5
    "archery2"
    0.5
    "archery4"
    0.5
    repeat

image animationread:
    "read1"
    0.6
    "read2"
    0.6
    "read3"
    0.6
    repeat

image animationreadl:
    "readl1"
    0.4
    "readl2"
    0.4
    "readl3"
    0.4
    repeat

image animationoblinidle:
    "goblin1"
    0.3
    "goblin2"
    0.3
    "goblin3"
    0.3
    "goblin2"
    repeat

image animationoblindie:
    "goblin4"
    0.05
    "goblin5"

image animationambush:
    "ambush2"
    0.1
    "ambush3"

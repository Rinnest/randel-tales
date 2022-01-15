label Scarlet:

    if findtheaclothes == 1:
        hide screen hud
        mc "Scarlet seems like a safe bet. She taught me that invisibility spell without a second thought."
        mc "Ok... Let's do this."
        scene lecturemage2 with fade
        "You find Scarlet in her classroom reading a book, and making notes for a study plan. She notices you walk in and looks up at you with a smile."
        show smilemc
        scene lecturemage3
        s "[mc]! I was just thinking about you. Are you wanting to learn any extracurricular spells for your \"stealth missions\"?"
        "She giggles and looks back down to her notes."
        s "I actually found this interesting spell that will make you-"
        mc "Uhm... no, I actually had a favor to ask of you Ms... I mean Scarlet."
        "Scarlet looks up again and closes her book. She leans forward on her desk."
        s "What can I do for you, sweetie?"
        mc  "\"Ahh... I can almost see right down her shirt... is she doing this on purpose?\""
        mc "Uhm... well... I... "
        "Scarlet's smile widens as she watches you."
        mc "I need some of your clothes..."
        "Scarlet's smile doesn't move an inch. She looks at you coyly."
        scene lecturemage1
        show smilemc
        show normalm
        show talkwam
        s "Hrm... I have to admit, I wasn't expecting that one. Why do you need them?"
        mc "\"She took that... well? I'm not sure what I was expecting... Now, how should I handle this?\""
        menu:
            "Be honest":
                mc "To be honest Scar, I went on an adventure to Yokel and saved a girl. The town was destroyed and she has nothing left. She needs a few change of clothes."
                show sadtalkm
                s "...Wow... That poor girl..."
                s "\"Why am I both disappointed and delighted? He's so sweet.\""
                s "Of course [mc], I'll leave some clothes in your desk tomorrow. Give that poor girl my regards, ok?"
                mc "\"That was remarkably painless...\""
                mc "Thank you, Scar. I'll be leaving now, I gu-"
                show anythingm
                s "Oh, but you'll owe me a favor someday."
                hide smilemc
                show talkwanmc
                mc "What?"
                s "You'll owe me one. My clothes are really nice, and I'm not going to force a girl down on her luck to owe me anything."
                mc "What do you want?"
                s "Oh... I haven't decided yet. I'll get back to you on that."
                "Scarlet winks."
                s "Go on now! I think class is starting soon!"
                mc "Ok then... Bye, Scarlet..."
                s "Bye, [mc]..."
                s "I love making that boy squirm..."
                "You leave the room with a sense of dread. Wondering what \"favor\" lies ahead in your future."
                $ theaclothestimer += 1
                $ findtheaclothes +=1
                jump academy

            "Lie about it":
                mc "Well... you see... I..."
                show normalm
                "Scarlet stares through you."
                show wasmilem
                show talksadhappymc
                mc "I mean... I'm learning how to be a tailor, just in case adventuring doesn't work out, so..."
                "Scarlet continues to stare. Somehow smiling even wider than before."
                mc "So I need some clothes...to hem... for practice... just in case..."
                "Scarlet stares at you. The silence is deafening. You think you are about to crack under the pressure, when she suddenly bursts into laughter."
                show lolm
                s "Hahaha!!! [mc], you are a monumentally bad liar, you dolt!"
                "She continues to laugh as you feel your pride slowly disintegrate."
                s "Oh wow... haha... I needed that. Ok [mc]. Just for the good laugh, I'll give you some clothes to \"hem\". But if you are considering an alternate career path. May suggest becoming a jester. You are hilarious!"
                mc "Thanks, Scarlet..."
                "Scarlet laughs again while you consider leaving."
                hide lolm
                show talkwam
                show thinkmc
                s "I'll drop them off in your desk tomorrow, sweetie. They won't be anything fancy, so don't get too... excited... about them."
                mc "No, it isn't for anything like that..."
                s "Sure, sure [mc], I -totally- believe you."
                "Scarlet winks at you."
                s "You should get going, class is going to start soon, I believe."
                mc "Thanks, Scar."
                s"Don't do anything I wouldn't do with them!"
                "Scarlet begins to laugh again as you exit the classroom. "
                mc "Wow... that could have gone better... at least I have the clothes for Thea..."
                $ theaclothestimer += 1
                $ findtheaclothes +=1
                jump academy


    hide screen hud
    scene lecturemage1
    show talkhappymc
    show normalm
    mc "Hello."
    hide talkhappymc
    show smilemc
    show talkwam
    s "Hey there ki-... I mean [mc], what's up?"
    menu:
        "Ask for help with the priestess" if bothpath >= 4 and protectionspell < 2 :
            if protectionspell == 0:
                show normalm
                show smilemc
                show talkmc
                mc "Scarlet, I-"
                s "Hold it right there. Are you asking for some favor again?"
                show talksadhappymc
                mc "Urr, yeah."
                s "I knew it! man, I should start charging you for these types of stuff. I feel like I'm spoiling you."
                mc "Please Scarlet, I really need your help this time."
                s "..........."
                s "Geez, fine. I can't say no to that face."
                mc "Heheh, thanks."
                s "So, what do you want this time, sir?"
                mc "Do you know protection magic I could use?"
                s "Yeah."
                mc "Could you teach me?"
                s "Hmm, what kind of protection spell do you need?"
                mc "What do you mean?"
                s "I mean, what kind of magic do you need protection from? Low class magic, medium class magic, high class magic?"
                mc "Umm, something like... elf magic."
                s "Elf magic! You've been dealing with quite a lot of elves recently."
                mc "\"I should tell her. She' helped me a lot, she deserves to know.\""
                mc "If I tell you something, can you keep it a secret?"
                s "Oh yes! I love secrets."
                mc "Ok."
                "You tell Scarlet the whole story."
                show uhm
                s "I can't believe a priestess would do that. [mc], this sounds serious. Let me go there, I can stop her."
                mc "No! I promised Eve that I wouldn't tell anyone about their village."
                s "Hmm. I see, you have to do it alone then?"
                mc "Yeah."
                s "I understand."
                s "So [mc], there's some good news and some bad news."
                mc "Ok."
                s "The bad news is, elf magic is really powerful. And I think at your level, it would take at least years until you learn a protection spell to counter elf magic."
                mc "Oh."
                hide uhm
                s "Hold on, I haven't said the good news yet. The good news is, you got yourself a master mage who can put a powerful protection spell on you."
                mc "Really! That's great! Let's get started then, I have no time to lose'"
                s "Hold on, mister. I need at least two days to put the spell on you."
                mc "What?! Really?"
                s "Come here."
                "Scarlet touches your forehead with her palm."
                s "Your mana level is too low."
                s "I can't put the spell on you at once."
                mc "Huh, why? I thought my mana had nothing to do with the spell."
                s "It does. Think of it as this way; A scrawny soldier needs to go through an army of orcs. So he's given a very strong armor, but it's heavy. Now, what happens when he wears it?"
                s "He gets crushed, because the armor is too heavy for him?"
                s "It's the same here. You're the scrawny soldier and the heavy armor is the protection spell."
                mc "Oh, I get it. But why take two days then?"
                s "I need to make the armor as light as possible so you can wear it. That takes time."
                mc "Ah, ok."
                s "I'll start the first phase now, but you'll have to come again if you want the spell to work properly."
                mc "Got it."
                show black with fade
                "Scarlet takes out her staff and chants a spell. She waves her staff and zaps you with a red beam of light. Your body starts to get heavy to the point where you feel like it would sink into the ground."
                hide black
                show worriedmc  with flash
                s "Ok, we're done for today."
                mc "\"Urgh, my head.\""
                s "[mc]?"
                mc "I'm fine, just a bit dizzy."
                s "Hahaha. Imagine if I did the whole thing right now."
                mc "Yeah... now I kind get what you said earlier."
                s "Now go home and get some rest."
                mc "Right, I'll be back for the second phase of the spell."
                s "Ok."
                scene academytalkblr
                show worriedmc
                show lookdownsupmc
                mc "\"Urk... I don't feel so good.\""
                show normalg with easeinleft
                pause 0.5
                hide normalg
                show talkwagabe
                hide lookdownsupmc
                show sadg
                g "Whoa, [mc]? What's up? You don't look so good."
                mc "Gabe? Y-Yeah, I'm just having a headache."
                g "Is it bad?"
                mc "N-No, I'll manage."
                g "You better go home straight away [mc]. I'll cover for ya."
                mc "Oh, th-thanks. Yeah, I should go home."
                g "You want me to walk you home?"
                mc "No, no, I'm fine. Thanks."
                g "Ok, be careful now."
                mc "I will."
                scene villageback with fade
                mc "\"Must get home... must... not... faint...\""
                "You somehow manage to get home."
                scene mcroomblur with fade
                show worriedmc
                show talksadhappymc
                mc "*sigh* I made it."
                if thealives == 1:
                    show normalth
                    show talknth
                    th "[mc]! You're early today."
                    mc "Oh, hey Thea. Yeah, I wasn't feeling well so I came home."
                    show worriedth
                    th "Oh no, are you sick?"
                    mc "Nah, I'm just tired, that's all."
                    show talksth
                    hide worriedth
                    hide talknth
                    th "You have... been away from home a lot recently."
                    mc "You're right, I've been on this important quest for a while now. I'm sorry, I didn't get a chance to tell you."
                    th "It's ok, I'm sure you've been very busy."
                    mc "Yeah."
                    show gambaruth
                    th "Then I suggest you go to bed straight away!"
                    show normalth
                    mc "Hahaha, I will."
                scene roomnew
                "You fall onto the bed and instantly fall asleep."
                $ time = 3
                $ protectionspell += 1
                jump home

            if protectionspell == 1:
                show normalm
                show smilemc
                show talkmc
                s "So, are we ready for the next phase?"
                mc "Yeah, I hope I'll be able to walk home today."
                s "Hahaha. Don't worry, it won't be that hard today."
                mc "I'll take your word for it."
                show black with dissolve
                "Scarlet zaps you with the red beam again. You somewhat feel less discomfort than the last time."
                hide black
                show thinkmc with flash
                s "Ok! We're done here. How do you feel?"
                mc "Urr... nothing special."
                s "That means it worked. Now be careful. And remember, the effects of the spell will wear off after some time."
                mc "Got it. Thank you, Scarlet. None of this would've been possible if it wasn't for you."
                s "Awww. Don't mention it [mc], it's been a pleasure."
                mc "See you then."
                $ time += 1
                s "Good luck kid"
                $ protectionspell += 1
                $ bothpath += 1
                jump academy

        "Ask about the seal" if bothpath >= 2 and rightsealspell == 0:
            if spellintroscarlet == 0:
                show normalm
                show smilemc
                show talkmc
                mc "Scarlet, do you know about seals?"
                show talkwam
                s "Uh... yeah."
                mc "See, I found this door while I was in a quest. And when I tried to open it, some kind mark apeared and pushed my hands back."
                s "Ahh. A doorway seal."
                mc "Yeah, something like that. What are they?"
                s "To put it into simple terms; They're basically magical locks. They can't be broken down by force."
                mc "Oh... so is there no way to break it?"
                s "There is. You can break it with magic, but that takes a lot of mana. The easiest way is to find the right spell and unlock it."
                mc "How do we do that?"
                s "You identify the type of seal by its mark."
                mc "Like the one that appeared when I tried to open the door?"
                s "Exactly."
                mc "Then... can you teach me how to open that door?"
                s "Sure I can!"
                mc "So, how do I do it?"
                s "First, do you remember the mark you saw on the seal?"
                mc "Urrrrr..."
                s "What kind of door was it? In what region did you find it?"
                mc "It... was a Elven door."
                s "An Elven door? Huh... You're in luck. Elves only have 8 seals, so I think you might be able to find it. Wait a minute."
                "Scarlet casts a spell and opens one of her drawers. She takes a book and shows it to you."
                scene sealspellbook with fade
                pause
                m "Here are the 8 signs, can you remember which one it was?"
                pause
                window hide
                menu:
                    "1":
                        mc "The first one."
                        s "Ok."
                        $ wrongsealspell = 1
                        "Scarlet pulls out a small rock and saps it with her staff."
                        jump sealtalk

                    "2":
                        mc "The second one."
                        s "Ok."
                        $ wrongsealspell = 1
                        "Scarlet pulls out a small rock and saps it with her staff."
                        jump sealtalk

                    "3":
                        mc "The third one."
                        s "Ok."
                        $ rightsealspell += 1
                        "Scarlet pulls out a small rock and saps it with her staff."
                        jump sealtalk

                    "4":
                        mc "The fourth one."
                        s "Ok."
                        $ wrongsealspell = 1
                        "Scarlet pulls out a small rock and saps it with her staff."
                        jump sealtalk

                    "5":
                        mc "The fifth one."
                        s "Ok."
                        $ wrongsealspell = 1
                        "Scarlet pulls out a small rock and saps it with her staff."
                        jump sealtalk


                    "6":
                        mc "The sixth one."
                        s "Ok."
                        $ wrongsealspell = 1
                        "Scarlet pulls out a small rock and saps it with her staff."
                        jump sealtalk

                    "7":
                        mc "The seventh one."
                        s "Ok."
                        $ wrongsealspell = 1
                        "Scarlet pulls out a small rock and saps it with her staff."
                        jump sealtalk

                    "8":
                        mc "The eighth one."
                        s "Ok."
                        $ wrongsealspell = 1
                        "Scarlet pulls out a small rock and saps it with her staff."
                        jump sealtalk

                    "Don't remember.":
                        $ dontrememberseal += 1
                        mc "Damn it, I can't remember."
                        s "Hmmm... I can't help you then, [mc]. Sorry."
                        mc "Urr..."
                        s "Come back if you remember it."
                        mc "Yeah, I'll try."
                        mc "\"Damn it, I have to memorize that symbol!\""
                        jump academy

            if dontrememberseal >= 1:
                mc "I remember the symbol now."
                s "Wait, let me get the book."
                jump SealBook

            mc "Um, Scarlet? ...That rune you gave me didn't work."
            s "What! No way."
            mc "Yeah, I think I showed you the wrong symbol."
            s "That has to be the reason. So do you remember the correct one?"
            mc "Yeah."
            s "Good, let me get the book."
            jump SealBook


        "Ask about an invisibility spell" if saq == 1 and invisibilityspell == 0 and peekingdone == 0:
            show normalm
            show talksadhappymc
            mc "Uhm... Hey, Scarlet..."
            show normalmc
            show talksadhappymc
            mc "...Is there something like an invisibility spell?"
            hide talksadhappymc
            show uhm
            s "An invisibility spell?"
            hide uhm
            show talkwam
            s "Yeah... why?"
            hide talkwam
            show talksadhappymc
            mc "I was wondering if you could teach me... that spell."
            hide talksadhappymc
            show wacm
            s "Why that spell in particular?"
            hide wacm
            show talksadhappymc
            menu:
                "Lie":
                    mc "Uhm... I thought... Since I'm an adventurer, now it would be useful... for... um... stealth missions!"
                    hide talksadhappymc
                    show anythingm
                    s "..........."
                    show suprisedblushmc
                    s "You wanna peep on girls, don't you?"
                    hide suprisedblushmc
                    show blushtalkhappymc
                    mc "Whaaa- How?! I mean, no, why would I do that???"
                    mc "I'm not some sick perv..."
                    hide blushtalkhappymc
                    show talkwam
                    s "Sure, sure... well, I don't care anyway."
                    s "So I'll teach you!"
                    show talkhappymc
                    hide talkwam
                    mc "What? Really?"
                    hide talkhappymc
                    show talkwam
                    s "I am a teacher, after all. Teaching is what I do."
                    s "I don't care what you do with what I teach..."
                    s "Wait... should I care?"
                    s "Ah... Nah. On second thought, I don't care."
                    scene black with fade
                    show text "{color=#fff}Scarlet teaches you the invisibility spell." at truecenter with dissolve
                    pause
                    hide text with dissolve
                    scene lecturemage1
                    show talkwanmc
                    mc "So I have to say HOLMAN and that's it?"
                    hide talkwanmc
                    show normalmc
                    show talkm
                    s "It's called chanting. And yes, you chant HOLMAN but you have to be familiar with the language of spells. How good is your Merdenese?"
                    show talkmc
                    if chartrait == 1:
                        mc "I've studied a fair amount."
                        s "Good. Make sure you are {b}fluent in Merdenese{/b}. That spell won't work if it's not pronounced correctly."
                    else:
                        mc "Not the best..."
                        s "Make sure you are at least basically {b}fluent in Merdenese{/b}. That spell won't work if it's not pronounced correctly."
                    mc "Ok, got it."
                    s "Oh and another thing, the spell only lasts for a few minutes... don't get caught doing whatever you're doing, ok?"
                    mc "I'm not doing anything... stealth missions, remember!?"
                    s "Sure. Don't get caught on your \"Stealth Mission\". "
                    mc "Thanks Scar."
                    hide talkhappymc
                    hide normalmc
                    show sadsmilem
                    $ invisibilityspell += 1
                    scene academytalkblr with fade
                    show normalmc
                    mc "So I learned the spell. Now I just have to use the Eye Orb."
                    $ q1 += 1
                    jump academy

        "Nothing.":
            show talksadhappymc
            hide talkwam
            mc "Nothing really."
            show talkm
            s "What?"
            s "Weirdo."
            jump academy
    return


label SealBook:

 scene sealspellbook with fade
 pause
 menu:
    "1":
        mc "The first one."
        s "Ok."
        $ wrongsealspell = 1
        "Scarlet pulls out a small rock and saps it with her staff."
        s "Here you go."
        mc "Thanks."
        jump academy

    "2":
        mc "The second one."
        s "Ok."
        $ wrongsealspell = 1
        "Scarlet pulls out a small rock and saps it with her staff."
        s "Here you go."
        mc "Thanks."
        jump academy

    "3":
        mc "The third one."
        s "Ok."
        $ rightsealspell = 1
        $ wrongsealspell = 0
        "Scarlet pulls out a small rock and saps it with her staff."
        s "Here you go."
        mc "Thanks."
        jump academy

    "4":
        mc "The fourth one."
        s "Ok."
        $ wrongsealspell = 1
        "Scarlet pulls out a small rock and saps it with her staff."
        s "Here you go."
        mc "Thanks."
        jump academy

    "5":
        mc "The fifth one."
        s "Ok."
        $ wrongsealspell = 1
        "Scarlet pulls out a small rock and saps it with her staff."
        s "Here you go."
        mc "Thanks."
        jump academy

    "6":
        mc "The sixth one."
        s "Ok."
        $ wrongsealspell = 1
        "Scarlet pulls out a small rock and saps it with her staff."
        s "Here you go."
        mc "Thanks."
        jump academy

    "7":
        mc "The seventh one."
        s "Ok."
        $ wrongsealspell = 1
        "Scarlet pulls out a small rock and saps it with her staff."
        s "Here you go."
        mc "Thanks."
        jump academy

    "8":
        mc "The eighth one."
        s "Ok."
        $ wrongsealspell = 1
        "Scarlet pulls out a small rock and saps it with her staff."
        s "Here you go."
        mc "Thanks."
        jump academy
 return


label sealtalk:

    scene lecturemage1
    show talkwanmc
    show normalm
    mc "What's this?"
    show talkwam
    s "A rune."
    mc "What do I do with it?"
    s "If you have this on your hand you can go through the barrier."
    show talkwamc
    mc "Woah, really? I thought I would have to learn a spell or something!"
    s "Normally you do, but... these are elf seals, even a Class B Mage has a hard time with this sort of stuff."
    mc "So what's special about this rune?"
    s "Well, I already did the hard part so you don't have to. The rune is already enchanted, you just have to hold it in your hand. Easy-peasy."
    mc "Wow. Thanks, Scarlet."
    show teethecm
    s "No problemo, kid. That's what teachers are for. Hahaha."
    show thinkmc
    mc "\"I thought teachers are supposed to teach students, not do it for them.\""
    mc "Say Scarlet, that book, doesn't having it make the seals kinda useless. Anyone can open the seal by looking at the book."
    show teethm
    s "Hehehe. Good point."
    s "Here's a little secret."
    s "This book is one of a kind, the only book in Merdian."
    mc "WHAT?! How did you get it?!"
    show talksleepm
    s "Hehehe. I have my ways."
    mc "No way."
    show talkwam
    hide talksleepm
    hide teethm
    hide teethecm
    s "Now don't go blabbering this to everyone you meet, it's a secret, ok?"
    mc "Fine."
    s "Good."
    mc "Thank you for this, Scarlet. I'll be going then."
    s "Ok."
    scene academytalkblr with fade
    mc "\"Ok, I got the spell! Hope it's the right one.\""
    $ spellintroscarlet += 1
    jump academy
    return

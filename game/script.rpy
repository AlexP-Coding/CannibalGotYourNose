# Script for "Oops a Cannibal Got Your Nose!"


###########
### SETUP  ###
###########


# DYNAMIC MEDIA

## Img position
transform middle:
    yalign 0.25
    xalign 0.5
    zoom 1.20

## Img speed
define fastDissolve = Dissolve(0.3)
define slowDissolve = Dissolve(0.8)
define slowishDissolve = Dissolve(0.5)
define superslowdissolve = Dissolve(3.0)

## Txt Speed


# COLORS

## Character Colors
define protagColor = "#10c05ada"
define cannibalColor = "#da28cb"

define bgCharColorA = "#1d53a5"

## Text Colors
define baddieColor = "#ff00ea"
define deathColor = "#ca0a0a"


# STYLES

### define gui.dialogue_text_outlines = [(1, "#0000", 0, 0)]

style slay:
    color baddieColor
    outlines [ (1,  "#ffffff", 0.5, 0.5) ]

style slayBig is slay:
    take slay
    size 65

style death:
    color deathColor
    outlines [( 1, "#ffffff", 0, 0)]

style loud:
    size 34

style quiet:
    size 10


# Characters used in this game

## Main Characters
define narrator = Character(what_italic=True)
define charYou = Character("You", color = protagColor)
## Not A Cannibal vs Cannibal
define charNac = Character("Ash", color=cannibalColor)
define charCan = Character("Your Friend the Cannibal", color=cannibalColor)
define charDad = Character("Dad")
define charMom = Character("Mom")
define charUnk = Character("?")


###############
### BASE SCRIPT  ###
###############

label start:
    # Introduction


    # play a song / sound effect
    play sound "sfx/birds.mp3"
    # Show a background with fade
    scene bedroom with fade
    "Ridley wakes up to the sound of birds chirping outside her window."
    play sound "sfx/phone.mp3"
    "Then, she receives a call from her friend."

    # Character sprite
    show ridley with dissolve 

    charNac "Hey, Ridley! Wanna hang out?" 
    play sound "sfx/birds.mp3"
    charYou "Sure, where to?" 
    charNac "A camp. Say bye to your parents and make sure to leave your will!" 
    charYou "Wait? What do you-"
    play sound "sfx/hang-up.mp3"


    "Ridley realizes that Ash had already hung up." 
    "Thinking it's just their friend being odd, Ridley ignores it." 
    play sound "sfx/birds.mp3"

    hide ridley with fade
    "Packing stuff for later, Ridley notices her parents standing by the door."

    show mother with dissolve
    show father at right with dissolve

    charDad "Hey, where are you going?" 
    show ridley at left with dissolve
    charYou "Camping." 
    "Ridley answered while shrugging"

  
    charMom "Okay, just be sure to have your phone with you at all times." 
    charYou "Sure!"

    hide father with fade
    hide mother with fade

    play sound "sfx/footsteps.mp3"
    scene house with fade
    "After packing and taking a shower, Ridley decides to go downstairs to eat breakfast with her parents"
    "And after eating, Ridley heads out to see Ash."


    scene street with fade
    play sound "sfx/cars.mp3"
    scene police with fade
    show ridley with dissolve 
    "As she approaches the restaurant owned by her friend's family, Ridley hears an ambulance."
    play sound "sfx/police.mp3"
    "Getting even closer, she sees some police officers taking care of a crowd."
    play sound "sfx/police.mp3"
    "It seems that part of the road has been sealed off due to a recent crime."
    play sound "sfx/footsteps.mp3"
    "Not wanting to trespass, she decides to go around the block to reach the restaurant." 
    scene street2 with fade
    play music "music/notScary.mp3"
    "As she does so, she suddenly feels a hand on her shoulder."
    charNac "It's chomping time!" 
    "a voice exclaims"
    play music "music/happy.mp3"
    "She quickly turns around to see her silly friend laughing on the ground."
    show ridley at left with dissolve
    charYou "This is why you don’t have many friends." 
    show ash with dissolve
    charNac "Right, because of that…" 
    "Ash says with a remorseful face"
    charYou "Say, do you know what all that is about?" 
    "You point at all the commotion happening close to your friend's home"
    charNac "Some idiot pretending to be a vampire or whatever." 
    charNac "Anyways, it's cool now, or so I think."
    charYou "You think?!"
    charNac "We can’t go eat at our restaurant for some time, though."
    charYou "That’s weird." 
    charYou "Did anything bad happen there?"
    play sound "sfx/oof.mp3" 
    charNac "I don’t know..." 
    charNac "But, speaking of eating, let's grab something to eat in that other restaurant."
    charNac "I could eat a whole cow right about now." 
    charYou "Sure…" 
    play music "music/happy.mp3"
    "Ridley agrees while looking at the clock and realizing why her friend was starving."
    charYou "Let's go, then."
    play music "music/happy.mp3"
    scene street3 with fade
    hide ash with dissolve
    hide ridley with dissolve


    "They decide on what to order as they made their way to the restaurant when Ash remembered something crucial."
    scene restaurant1 with fade
    show ash with dissolve
    charNac "Oh!"
    show ridley at left with dissolve
    charYou "What?"
    charNac "I forgot to pack some condiments for dinner!" 
    charNac "You know I can't live without peppering my food before eating it."
    charNac "...especially campfire-cooked food."
    "her friend says, kneeling on the ground"
    charYou "You always like to overreact."
    charYou  "Can't you just bear with it for today?" 
    charNac "I can but..."
    charNac "Don't be surprised if I feel like running around in search of deliciously seasoned meat." 
    "Ridley throws an annoying look at Ash"
    charYou "Well, enough chatting." 
    charYou "Let's just go inside this place." 


    "Ridley says while reaching for the restaurant's door handle"
    scene restaurant2 with fade
    play music "music/restaurant.mp3"
    "They ordered their food as soon as they found a table for themselves." 
    "After an hour of talking  about trivial matters, they finished their meal." 
    "It's worth mentioning that Ridley thought it was pretty strange how Ash looked completely satisfied after a long bathroom break."
    "They decided to grab some kitchen tools to make dinner at the campsite later that day."


    scene warehouse with fade
    play music "music/warehouse.mp3"
    "With minimal hassle, they arrived at a store and purchased the necessary items." 
    play sound "sfx/radio.mp3"
    "All the while a disturbing bathroom murder was being reported on the radio."
    "As the sun began to set, and with everyone else retreating to the safety of their homes due to the threat of a serial killer on the loose."
    scene taxi with fade
    play sound "sfx/footsteps2.mp3"
    play sound "sfx/cars2.mp3"

    "Now equipped with everything they needed."

    play sound "sfx/horn.mp3"
    "Ridley and Ash decided to call a taxi to take them to the campsite."
    scene campsite with fade
    play music "music/campsite.mp3"
    "An hour later, they arrive at the campsite."
    show ash with dissolve
    charNac "That place looks good."
    charNac "Let's stay there."
    "Ash said, as she pointed to an isolated part of the campsite."
    show ridley at left with dissolve
    charYou "Sure."
    "Ridley goes along, with not much choice on the matter, on also staying in that place for the evening."
    scene campsite with fade
    # This ends the introduction.

default menuset = set()

# used to test endings

menu endings:

    set menuset
    "Where should I go?"

    "Sure, let's go!":
        jump badEnd  
    "No, I have other plans.":
        jump goodEnd  
    "No, thanks bro!":
        jump trueEnd  

return

label badEnd:
    # Got Your Nose ending 
    # End up with all limbs eaten (by not tricking enough).

    scene street0 with fade
    play sound "sfx/cars2.mp3"
    # ridley sprite without limbs
    show ridley with dissolve 

    "Not having the energy or limbs to escape, you try to call out for anyone to help you run away from your fiendish friend." 
    "No one ever appears, and you end up crying on the floor"

    charYou "Well, I guess this is it."
    "You think about all the times you were happy and realize that many of those times were due to your friend."

    play sound "sfx/footsteps.mp3"
    "As you slowly drift away, your friend appears on the scene and says."
    play music "music/mystery2.mp3"
    show ash at right with dissolve
    charNac "You always did have the prettiest nose." 

    play sound "sfx/limb-lost.mp3"
    charNac "Let me fix that."
    "You feel a tingling sensation on your face."
    "Suddenly, you realize you lack the power to even breathe."
    play sound "sfx/oof.mp3"
    hide ridley with dissolve
    hide ash with dissolve
    "Oops a Cannibal Got Your Nose!"
    "The End..."
    play sound "sfx/oof.mp3"
    # This ends the bad end.
    return

label goodEnd:
    # Canni-boom! ending (cannibal gets so full he ends up exploding)
    # Ridley has to have a cane/pistol/chainsaw/knife and has to survive 3 or more scenarios.

    scene street8 with fade
    play sound "sfx/running.mp3"
    show ridley with dissolve

    "As you continue running away, anger starts to creep into your thoughts"
    "Why do I have to keep running away from someone who could never beat me to the last lamb sandwich in the school's canteen?"
    "You ponder"

    scene street6 with fade
    charYou "I'm so done with this! Can no one help me?"
    "You yell out, hoping someone will hear"
    play sound "sfx/bloody-floor.mp3"
    z "Hehehe."
    "You hear laughter not too far away, and as you look around, you realize where you've just run into."
    scene alley with fade
    play sound "sfx/cannibal-footstep.mp3"

    "You look at your friend, who is now barely visible."
    show ridley with dissolve
    charYou "All of these people..."
    charYou "Was it really you who did this?"
    charNac "I sure have a big appetite. I thought you already knew that."
    "As you try not to throw up, you attempt to stand your ground"
    charYou "Do you realize what you've just done?" 
    charYou "These were people like you and me." 
    charYou "They had futures!"
    charNac "Don't you realize how much they mocked me when they asked my parents to make them non-vegan food?" 
    charNac "It sickens me to this day how much they enjoy not caring about the world."
    charYou "This has to stop!"
    charNac "I agree." 
    charNac "Chasing you has been quite time-consuming." 
    charNac "I even missed out on my favorite show."

    play sound "sfx/determinator.mp3"
    "Now seeing how far your friend has fallen, you decide to take matters into your own hands."
    #inflated ash
    show ash at right with dissolve
    "Ash, now clearly visible, can hardly move as her stomach has ballooned from overeating."
    "Yet, even with a chance to run away, you are determined to end it here."
    play sound "sfx/explosion.mp3"
    "You wield your weapon, and then, your friend blows up in a grotesque manner."
    "You are so shocked by this that you end up unconscious" 

    scene hospital with fade
    play sound "sfx/birds.mp3"
    "The next day, you open your eyes in a hospital bed, nearby you see your parents asleep in their chairs."
    "You turn on the TV to see that the news is talking about a serial killer who was recently arrested for life—your friend."
    "You breathe a sigh of relief as you realize that you no longer have to run away."
    "Yet..."
    "You feel a bit sad about your friend, Ash."

    "The End."
    # This ends the good end.
    return

label trueEnd:
    #  Become a Cannibal ending 
    #  Sacrificed/ Tricked 2 or more people.

    scene street7 with fade
    play sound "sfx/running.mp3"
    "After a long night, you find yourself exhausted and in dire need of nutrition." 

    scene bench with fade
    play sound "sfx/dark.mp3"
    "You sit on a bench that was close to you and wonder out loud"
    show ridley with dissolve
    charYou "When will this ever stop?" 
    charYou "I sacrificed so many good people, only for Ash to still be chasing me!"
    play sound "sfx/laugh.mp3"
    "You hear sounds of people having fun."
    charYou "This has to be the worst day of my life, and yet they are having a happy day..."
    play sound "sfx/dark.mp3"
    "Suddenly, you hear footsteps of someone approaching close by."
    show ash at right with dissolve
    charNac "Hey! I heard what you were saying."
    charYou "What?"

    "You get up from the bench to start running away but you are grabbed"
    
    charNac "Listen, I didn’t know I was hurting you all this time."
    play music "music/mystery2.mp3" 
    charNac "I just really wanted to get some of your happiness for myself."
    "You give up on running away and sit next to your friend."
    charYou "Eating me is not the solution to that." 
    charYou "Have you considered talking to me before?" 
    charYou "About all of this?" 
    charYou "And that happiness, to me, was being friends with you."
    "You continue."
    charYou "Is human meat all that great for you to decide to cut ties with me?"
    "Your friend makes an expression that you've never seen before and says."
    charNac "You don't know until you try it!"
    "Your friend shows you a human arm, and right then and there, you succumb to your exhaustion and decide to eat it."
    "Turns out you liked it."
    charNac "See? We can still be friends, and you get revenge on this city for not having helped you."

    play sound "sfx/oof.mp3"
    "You realize that you are being manipulated, but as you still want to be friends, you decide to go with the flow."
    scene street6 with fade
    "You look around at all the people walking around and get hungrier and hungrier, and with the help of your friend, you end up going for a midnight snack."

    "The End!"
    # This ends the true end.
    return



####################
### DISTRACT CANNIBAL ###
####################

## Distract 01
label distract_01:
    "Your dear friend is munching on a juicy leg you've brought him."
    "He is making loud approving sounds as he eats."

    cCannibal "{i}* mouth full *{/i}  You have to bring me more like this one. Yummers."
    
    cPlayer "I’m glad you enjoy it…"
    cPlayer "So if you don’t mind-"

    cCannibal "Don’t worry, I will enjoy you too."
    cCannibal "Even if you taste worse."
    cCannibal "Which you probably will."

    cPlayer "Well, why don’t I get you something a bit more tasty than me? I bet I taste really sour."
    
    cCannibal "No. You’re next! Don’t worry!"

    cPlayer "Uhh…"
    cPlayer "{i}{size=*0.5}What to do…{/i}"

    menu:
        "Search pockets for extra meat":
            jump distract_01_choice01a
        "Plead and cry like a baby":
            jump distract_01_choice01b

    return

label distract_01_choice01a:
    "You fumble around, desperately looking for anything in your pockets."
    "Until you find {i}it{/i}."
    "A perfectly intact leg!"
    "Well, maybe perfect and intact are a bit too strong of words to describe this leg."
    "{cps=*0.5} How long has it been in there?{/cps}"
    "Well, either way, that sounds like a problem for your friend, not you."

    cPlayer "Hey, buddy. Look what I found. It’s the pair for that leg!"

    cCannibal "{i}* chewing *{/i}  Wait really?"
    cCannibal "{i}* swallows and approaches *{/i}"
    cCannibal "That… doesn’t look like the same person."
    cCannibal "It smells nasty, and it’s kind of green? It’s missing some toes…"
    cCannibal "{cps=*0.2}{b}{i}Are you trying to trick me?{/i}{/b}{/cps}"

    cPlayer "{cps=*0.2} Nooo.{/cps} I swear!"
    cPlayer "It’s aaa… dipped in a special french sauce."
    cPlayer "You see, it makes it like cheese. The moldier and stinkier the better!"

    return

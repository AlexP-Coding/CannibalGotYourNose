# Script for "Oops a Cannibal Got Your Nose!"

# Characters used in this game

define a = Character("Ridley")
define b = Character("Ash")
define c = Character("Father")
define d = Character("Mother")
define z = Character("?")

label start:
    # Introduction


    # play a song / sound effect
    play music "birds.mp3"
    # Show a background with fade
    scene bedroom with fade
    "Ridley wakes up to the sound of birds chirping outside her window."
    play music "phone.mp3"
    "Then, she receives a call from her friend."

    # Character sprite
    show ridley with dissolve 

    b "Hey, Ridley! Wanna hang out?" 
    play music "birds.mp3"
    a "Sure, where to?" 
    b "A camp. Say bye to your parents and make sure to leave your will!" 
    a "Wait? What do you-"
    play music "hang-up.mp3"


    "Ridley realizes that Ash had already hung up." 
    "Thinking it's just their friend being odd, Ridley ignores it." 
    play music "birds.mp3"

    hide ridley with fade
    "Packing stuff for later, Ridley notices her parents standing by the door."

    show mother with dissolve
    show father at right with dissolve

    c "Hey, where are you going?" 
    show ridley at left with dissolve
    a "Camping." 
    "Ridley answered while shrugging"

  
    d "Okay, just be sure to have your phone with you at all times." 
    a "Sure!"

    hide father with fade
    hide mother with fade

    play music "footsteps.mp3"
    scene house with fade
    "After packing and taking a shower, Ridley decides to go downstairs to eat breakfast with her parents"
    "And after eating, Ridley heads out to see Ash."


    scene street with fade
    play music "cars.mp3"
    scene police with fade
    show ridley with dissolve 
    "As she approaches the restaurant owned by her friend's family, Ridley hears an ambulance."
    play music "police.mp3"
    "Getting even closer, she sees some police officers taking care of a crowd."
    play music "police.mp3"
    "It seems that part of the road has been sealed off due to a recent crime."
    play music "footsteps.mp3"
    "Not wanting to trespass, she decides to go around the block to reach the restaurant." 
    scene street2 with fade
    play music "notScary.mp3"
    "As she does so, she suddenly feels a hand on her shoulder."
    b "It's chomping time!" 
    "a voice exclaims"
    play music "happy.mp3"
    "She quickly turns around to see her silly friend laughing on the ground."
    show ridley at left with dissolve
    a "This is why you don’t have many friends." 
    show ash with dissolve
    b "Right, because of that…" 
    "Ash says with a remorseful face"
    a "Say, do you know what all that is about?" 
    "You point at all the commotion happening close to your friend's home"
    b "Some idiot pretending to be a vampire or whatever." 
    b "Anyways, it's cool now, or so I think."
    a "You think?!"
    b "We can’t go eat at our restaurant for some time, though."
    a "That’s weird." 
    a "Did anything bad happen there?"
    play music "oof.mp3" 
    b "I don’t know..." 
    b "But, speaking of eating, let's grab something to eat in that other restaurant."
    b "I could eat a whole cow right about now." 
    a  "Sure…" 
    play music "happy.mp3"
    "Ridley agrees while looking at the clock and realizing why her friend was starving."
    a "Let's go, then."
    play music "happy.mp3"
    scene street3 with fade
    hide ash with dissolve
    hide ridley with dissolve


    "They decide on what to order as they made their way to the restaurant when Ash remembered something crucial."
    scene restaurant1 with fade
    show ash with dissolve
    b "Oh!"
    show ridley at left with dissolve
    a "What?"
    b "I forgot to pack some condiments for dinner!" 
    b "You know I can't live without peppering my food before eating it."
    b "...especially campfire-cooked food."
    "her friend says, kneeling on the ground"
    a "You always like to overreact."
    a  "Can't you just bear with it for today?" 
    b "I can but..."
    b "Don't be surprised if I feel like running around in search of deliciously seasoned meat." 
    "Ridley throws an annoying look at Ash"
    a "Well, enough chatting." 
    a "Let's just go inside this place." 


    "Ridley says while reaching for the restaurant's door handle"
    scene restaurant2 with fade
    play music "restaurant.mp3"
    "They ordered their food as soon as they found a table for themselves." 
    "After an hour of talking  about trivial matters, they finished their meal." 
    "It's worth mentioning that Ridley thought it was pretty strange how Ash looked completely satisfied after a long bathroom break."
    "They decided to grab some kitchen tools to make dinner at the campsite later that day."


    scene warehouse with fade
    play music "warehouse.mp3"
    "With minimal hassle, they arrived at a store and purchased the necessary items." 
    play music "radio.mp3"
    "All the while a disturbing bathroom murder was being reported on the radio."
    "As the sun began to set, and with everyone else retreating to the safety of their homes due to the threat of a serial killer on the loose."
    scene taxi with fade
    play music "footsteps2.mp3"
    play music "cars2.mp3"

    "Now equipped with everything they needed."

    play music "horn.mp3"
    "Ridley and Ash decided to call a taxi to take them to the campsite."
    scene campsite with fade
    play music "campsite.mp3"
    "An hour later, they arrive at the campsite."
    show ash with dissolve
    b "That place looks good."
    b "Let's stay there."
    "Ash said, as she pointed to an isolated part of the campsite."
    show ridley at left with dissolve
    a "Sure."
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
    play music "cars2.mp3"
    # ridley sprite without limbs
    show ridley with dissolve 

    "Not having the energy or limbs to escape, you try to call out for anyone to help you run away from your fiendish friend." 
    "No one ever appears, and you end up crying on the floor"

    a "Well, I guess this is it."
    "You think about all the times you were happy and realize that many of those times were due to your friend."

    play music "footsteps.mp3"
    "As you slowly drift away, your friend appears on the scene and says."
    play music "mystery2.mp3"
    show ash at right with dissolve
    b "You always did have the prettiest nose." 

    play music "limb-lost.mp3"
    b "Let me fix that."
    "You feel a tingling sensation on your face."
    "Suddenly, you realize you lack the power to even breathe."
    play music "oof.mp3"
    hide ridley with dissolve
    hide ash with dissolve
    "Oops a Cannibal Got Your Nose!"
    "The End..."
    play music "oof.mp3"
    # This ends the bad end.
    return

label goodEnd:
    # Canni-boom! ending (cannibal gets so full he ends up exploding)
    # Ridley has to have a cane/pistol/chainsaw/knife and has to survive 3 or more scenarios.

    scene street8 with fade
    play music "running.mp3"
    show ridley with dissolve

    "As you continue running away, anger starts to creep into your thoughts"
    "Why do I have to keep running away from someone who could never beat me to the last lamb sandwich in the school's canteen?"
    "You ponder"

    scene street6 with fade
    a "I'm so done with this! Can no one help me?"
    "You yell out, hoping someone will hear"
    play music "bloody-floor.mp3"
    z "Hehehe."
    "You hear laughter not too far away, and as you look around, you realize where you've just run into."
    scene alley with fade
    play music "cannibal-footstep.mp3"

    "You look at your friend, who is now barely visible."
    show ridley with dissolve
    a "All of these people..."
    a "Was it really you who did this?"
    b "I sure have a big appetite. I thought you already knew that."
    "As you try not to throw up, you attempt to stand your ground"
    a "Do you realize what you've just done?" 
    a "These were people like you and me." 
    a "They had futures!"
    b "Don't you realize how much they mocked me when they asked my parents to make them non-vegan food?" 
    b "It sickens me to this day how much they enjoy not caring about the world."
    a "This has to stop!"
    b "I agree." 
    b "Chasing you has been quite time-consuming." 
    b "I even missed out on my favorite show."

    play music "determinator.mp3"
    "Now seeing how far your friend has fallen, you decide to take matters into your own hands."
    #inflated ash
    show ash at right with dissolve
    "Ash, now clearly visible, can hardly move as her stomach has ballooned from overeating."
    "Yet, even with a chance to run away, you are determined to end it here."
    play music "explosion.mp3"
    "You wield your weapon, and then, your friend blows up in a grotesque manner."
    "You are so shocked by this that you end up unconscious" 

    scene hospital with fade
    play music "birds.mp3"
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
    play music "running.mp3"
    "After a long night, you find yourself exhausted and in dire need of nutrition." 

    scene bench with fade
    play music "dark.mp3"
    "You sit on a bench that was close to you and wonder out loud"
    show ridley with dissolve
    a "When will this ever stop?" 
    a "I sacrificed so many good people, only for Ash to still be chasing me!"
    play music "laugh.mp3"
    "You hear sounds of people having fun."
    a "This has to be the worst day of my life, and yet they are having a happy day..."
    play music "dark.mp3"
    "Suddenly, you hear footsteps of someone approaching close by."
    show ash at right with dissolve
    b "Hey! I heard what you were saying."
    a "What?"

    "You get up from the bench to start running away but you are grabbed"
    
    b "Listen, I didn’t know I was hurting you all this time."
    play music "mystery2.mp3" 
    b "I just really wanted to get some of your happiness for myself."
    "You give up on running away and sit next to your friend."
    a "Eating me is not the solution to that." 
    a "Have you considered talking to me before?" 
    a "About all of this?" 
    a "And that happiness, to me, was being friends with you."
    "You continue."
    a "Is human meat all that great for you to decide to cut ties with me?"
    "Your friend makes an expression that you've never seen before and says."
    b "You don't know until you try it!"
    "Your friend shows you a human arm, and right then and there, you succumb to your exhaustion and decide to eat it."
    "Turns out you liked it."
    b "See? We can still be friends, and you get revenge on this city for not having helped you."

    play music "oof.mp3"
    "You realize that you are being manipulated, but as you still want to be friends, you decide to go with the flow."
    scene street6 with fade
    "You look around at all the people walking around and get hungrier and hungrier, and with the help of your friend, you end up going for a midnight snack."

    "The End!"
    # This ends the true end.
    return
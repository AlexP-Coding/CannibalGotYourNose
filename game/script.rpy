# The script of the game goes in this file.


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

define gui.dialogue_text_outlines = [(1, "#0000", 0, 0)]

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


# CHARACTERS
define e = Character("Eileen")

## Main characters
define narrator = Character(what_italic=True)
define cPlayer = Character("", color = protagColor)
define cCannibal = Character("Your friend the cannibal", color=cannibalColor)





# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return

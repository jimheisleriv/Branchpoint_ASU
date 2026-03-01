# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define g = Character("Gary")
default gameScript = "Level1"
default gameScriptInit = ""
default tutorialMode = False
default currentEvents = []
default event = ""
default tutorialOfficeBypass = False
default eventText = ""
default john = ""

default choice = "1"
default talkBack = ""
default response1 = ""
default reply1 = ""
default response2 = ""
default reply2 = ""
default response3 = ""
default reply3 = ""

default officeEventToView = False
default copyEventToView = False

# The game starts here.

label start:

    show bg cityscape

    "The Almighty CEO" "Whoa now, we haven't even finished the infrastructure yet."

    "The Almighty CEO" "I get that you're eager... but at least let the construction crew finish before you come waltzing in."

    scene bg room
    
    "well, I suppose you've got everything under control, then."

    "Best of luck!"
    
    call screen role_select

    $ gameScriptInit = "mainHandle" + gameScript

    jump expression gameScriptInit

    "Cool"

    return

label eventConclusion:
    if tutorialMode:
        call tutorialConclusion
    $ officeEventToView = False
    $ copyEventToView = False
    $ event = ""
    call screen mainGameplayLoop


#label checkback:
#    jump eventUpdater
#    call screen mainGameplayLoop        

label mainOfficeGeneral:

    #init python:
    #    nonsense = ['one', 'two', 'eight']

    #$event = renpy.random.choice(nonsense)

    menu:
        "[event]" if officeEventToView:
            call eventLookup
            call screen eventViewer
        "Never mind...":
                if tutorialMode and tutorialOfficeBypass == False:
                    g "Well, sometimes all you have to do is give it a minute. There's always something to do around here."
                    g "Whether or not it's immediately obvious... Well, it usually is."
                    $ event = "Stolen cake"
                    $ officeEventToView = True
                    $ tutorialOfficeBypass = True
                call screen mainGameplayLoop

label copyRoomGeneral:

    menu:
        "[event]" if copyEventToView:
            call eventLookup
            call screen eventViewer
        "Never mind...":
                if tutorialMode and tutorialOfficeBypass == False:
                    g "Well, sometimes all you have to do is give it a minute. There's always something to do around here."
                    g "Whether or not it's immediately obvious... Well, it usually is."
                    $ event = "Stolen cake"
                    $ officeEventToView = True
                    $ tutorialOfficeBypass = True
                call screen mainGameplayLoop

label eventLookup:
    if event == "Stolen cake":
        $ eventText = "Someone's cake was stolen out of the break room earlier today. As you are obviously the best employee for the job, how do you respond?"
        $ response1 = "Let's track them down."
        $ reply1 = "Haha, we could always use a hothead like you around. I appreciate your enthusiasm."
        $ response2 = "Well... let's let bygones be bygones."
        $ reply2 = "A nonconfrontational approach. Well, at the end of the day it is just food after all."
        $ response3 = "Should we just get them another one?"
        $ reply3 = "Out of your own pocket, I would hope. We can't solve everything by throwing money at it."

    if event == "Copier threat":
        $ eventText = "A vague threat of a cyber attack made its way out of the copier. All the employees swear it wasn't them... What's your take?"
        $ response1 = "Someone must've forgotten to lock down the copier when they installed it. They have a history of being security weakpoints."
        $ reply1 = "Well, that's true. I suppose that implies whoever broke in has access to a decent number of our print records now."
        $ response2 = "Must be a prank from someone in the department. Let's look at which employee computer printed it."
        $ reply2 = "That's a reasonable decision. One always has to ask, if it could've happened for a long time, why hasn't it happened /iyet/i?"
        $ response3 = "Just take it offline and call it a day. IT departments don't need to print a whole lot on a day-to-day anyway"

    #else:
    #    $ eventText = "No event found"
    #    $ response1 = "Option 1"
    #    $ reply1 = "Text 1"
    #    $ response2 = "Option 2"
    #    $ reply2 = "Text 2"
    #    $ response3 = "Option 3"
    #    $ reply3 = "Text 3"
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define g = Character("Gary")
default gameScript = "Level1"
default gameScriptInit = ""
default tutorialMode = False
default currentEvents = []
default departmentsViewed = []
default event = ""
default tutorialOfficeBypass = False
default eventText = ""
default eventResponses = 5
default cisoEventTrigger = False

default choice = "1"
default talkBack = ""
default response1 = ""
default reply1 = ""
default response2 = ""
default reply2 = ""
default response3 = ""
default reply3 = ""
default response4 = ""
default reply4 = ""
default response5 = ""
default reply5 = ""

default mainOfficeHovered = False
default researchDevHovered = False
default helpDeskHovered = False
default cyberSecHovered = False
default serverRoomHovered = False
default cubicleHovered = False
default deviceStorageHovered = False
default copyRoomHovered = False
default titleScreenHovered = False


default officeEventToView = False
default rdEventToView = False
default deskEventToView = False
default cyberEventToView = False
default serverEventToView = False
default cubicleEventToView = False
default storageEventToView = False
default copyEventToView = False

# The game starts here.

label start:

    show bg cityscape

    "The Almighty CEO" "Whoa now, we haven't even finished the infrastructure yet."

    "The Almighty CEO" "I get that you're eager... but at least let the construction crew finish before you come waltzing in."

    #scene bg room
    
    #"well, I suppose you've got everything under control, then."

    #"Best of luck!"
    
    #call screen role_select

    #$ gameScriptInit = "mainHandle" + gameScript

    #jump expression gameScriptInit

    #"Cool"

    return

#TODO: REFACTOR THIS NONSENSE; this code does NOTHING but reset the game to a "default" state and is already behind the curve!
label eventConclusion:
    if tutorialMode:
        call tutorialConclusion
    $ officeEventToView = False
    $ cubicleEventToView = False
    call screen mainGameplayLoop


#label checkback:
#    jump eventUpdater
#    call screen mainGameplayLoop       

label mainOfficeSwitch:
    if tutorialMode:
        jump tutorialOfficeGeneral
    else:
        jump mainOfficeGeneral

label researchDevSwitch:
    if tutorialMode:
        jump tutorialResDevGeneral
    else:
        jump researchDevGeneral

label helpDeskSwitch:
    if tutorialMode:
        jump tutorialHelpDeskGeneral
    else:
        jump helpDeskGeneral

label cyberSecSwitch:
    if tutorialMode:
        jump tutorialCyberSecGeneral
    else:
        jump cyberSecGeneral

label serverRoomSwitch:
    if tutorialMode:
        jump tutorialServersGeneral
    else:
        jump serverRoomGeneral

label cubicleSwitch:
    if tutorialMode:
        jump tutorialCubicleGeneral
    else:
        jump cubicleGeneral

label deviceStorageSwitch:
    if tutorialMode:
        jump tutorialStorageGeneral
    else:
        jump deviceStorageGeneral

label copyRoomSwitch:
    if tutorialMode:
        jump tutorialCopierGeneral
    else:
        jump copyRoomGeneral


#Label to handle event trees for CISO Office.
label mainOfficeGeneral:
    menu:
        #If event to view, use the name of the event and display it as a button. Does not support multiple events for the same department. Ditto for all other departments.
        #TODO: Abstract number of events per department to allow multiple at once. REPEAT THIS TO-DO AD INFINITUM FOR ALL DEPARTMENTS.
        "[event]" if officeEventToView:
            call eventLookup
            call screen eventViewer
        "Never mind...":
                call screen mainGameplayLoop

#Label to handle event trees for R&D Department.
label researchDevGeneral:
    menu:
        "[event]" if copyEventToView:
            call eventLookup
            call screen eventViewer
        "Never mind...":
                call screen mainGameplayLoop

#Label to handle event trees for Helpdesk.
label helpDeskGeneral:
    menu:
        "[event]" if deskEventToView:
            call eventLookup
            call screen eventViewer
        "Never mind...":
                call screen mainGameplayLoop

#Label to handle event trees for Cybersecurity.
label cyberSecGeneral:
    menu:
        "[event]" if cyberEventToView:
            call eventLookup
            call screen eventViewer
        "Never mind...":
                call screen mainGameplayLoop

#Label to handle event trees for Server Room.
label serverRoomGeneral:
    menu:
        "[event]" if serverEventToView:
            call eventLookup
            call screen eventViewer
        "Never mind...":
                call screen mainGameplayLoop

#Label to handle event trees for Cubicles.
label cubicleGeneral:
    menu:
        "[event]" if cubicleEventToView:
            "When handling an event, a list of 2 to 5 options will appear. What response you choose can and will affect your score at the end of the game, and may even end your game early."
            "Much like the real world, there is, more often than not, no truly correct or incorrect answer."
            "Most importantly, these events are chosen randomly from a pool. You may see the same event four times, not at all, or face impossible tasks. How you handle it is, once again, up to you."
            call eventLookup
            call screen eventViewer
        "Never mind...":
                call screen mainGameplayLoop

#Label to handle event trees for Device Storage.
label deviceStorageGeneral:
    menu:
        "[event]" if storageEventToView:
            call eventLookup
            call screen eventViewer
        "Never mind...":
                call screen mainGameplayLoop

#Label to handle event trees for Copy Room.
label copyRoomGeneral:
    menu:
        "[event]" if copyEventToView:
            call eventLookup
            call screen eventViewer
        "Never mind...":
                call screen mainGameplayLoop

#Lookup table for events
#TODO THIS SUCKS; please for the love of god make a more efficient way to handle this.
#   i forgot what i was gonna say
label eventLookup:
    if event == "Stolen cake":
        $ eventResponses = 3
        $ eventText = "Someone's cake was stolen out of the break room earlier today. As you are obviously the best employee for the job, how do you respond?"
        $ response1 = "Let's track them down."
        $ reply1 = "Haha, we could always use a hothead like you around. I appreciate your enthusiasm."
        $ response2 = "Well... let's let bygones be bygones."
        $ reply2 = "A nonconfrontational approach. Well, at the end of the day it is just food after all."
        $ response3 = "Should we just get them another one?"
        $ reply3 = "Out of your own pocket, I would hope. We can't solve everything by throwing money at it."
    elif event == "Copier threat":
        $ eventResponses = 5
        $ eventText = "A vague threat of a cyber attack made its way out of the copier. All the employees swear it wasn't them... What's your take?"
        $ response1 = "Someone must've forgotten to lock down the copier when they installed it. They have a history of being security weakpoints."
        $ reply1 = "Well, that's true. I suppose that implies whoever broke in has access to a decent number of our print records now."
        $ response2 = "Must be a prank from someone in the department. Let's look at which employee computer printed it."
        $ reply2 = "That's a reasonable decision. One always has to ask, if it could've happened for a long time, why hasn't it happened /iyet/i?"
        $ response3 = "Just take it offline and call it a day. IT departments don't need to print a whole lot on a day-to-day anyway"
        $ reply3 = "ligma"
        $ response4 = "sigma"
        $ reply4 = "he made a statement so ass his whole gang clowned him"
        $ response5 = "library"
        $ reply5 = "fuck it we ball"

    #else:
    #    $ eventText = "No event found"
    #    $ response1 = "Option 1"
    #    $ reply1 = "Text 1"
    #    $ response2 = "Option 2"
    #    $ reply2 = "Text 2"
    #    $ response3 = "Option 3"
    #    $ reply3 = "Text 3"
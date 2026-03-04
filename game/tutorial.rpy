default departmentsViewed = []
default tutorialOfficeBypass = False
default cisoEventTrigger = False
default tutorialComplete = False
default officeWarning = True


label tutorial:
    $ tutorialMode = True

    $ officeEventToView = True
    $ rdEventToView = True
    $ deskEventToView = True
    $ cyberEventToView = True
    $ serverEventToView = True
    $ cubicleEventToView = True
    $ storageEventToView = True 
    $ copyEventToView = True

    scene bg main_hq_hall

    ""

    "It's your first day on the job..."

    "Despite the fact the keycard in your hand is clearly labeled 'Intern', you're determined to do the job right."

    "The main door to the wing opens, and a somewhat friendly face greets you as you enter."

    scene bg helpdesk_1

    show b_happy

    b "Welcome in! What is it this time, laptop trouble? Authenticator on the fritz? Access permission issues?"

    b "Ohh, a green keycard? So you're the intern they were telling me about."

    b "Well, we're glad to have you! I know this place ain't much, but we hope you'll excel while you're here!"

    b "Personally, I'm about to head to lunch, but I'll hand it off to our main-man Gary and he'll show you the ropes."

    hide b_happy
    show g_mad

    g "I'm the head of the Cybersecurity department. Doesn't mean a lot since there's only three of us here, but still."

    g "If you have any questions about what each department is, or what it does for us, just ask."

    g "Now then. We have a tour to attend to."

    hide g_mad

    scene bg eventfocus

    # This ends the game.

    #jump start

    call screen mainGameplayLoop

    return
label tutorialConclusion:
    g "[talkBack]"
    g "Well, looks like you're getting the hang of things. I think we'd do well to keep you around even after your time here is up."
    g "That said... I've still got work to do. Come swing by my department if you need a hand."
    g "Otherwise, I think you're on your own for now."
    "You have now completed the tutorial. When you wish to play the full game, return to the title screen."
    $ tutorialComplete = True
    $ cisoEventTrigger = False
    $ cubicleEventToView = False
    call screen mainGameplayLoop

#Tutorial label to handle event trees for CISO Office.
label tutorialOfficeGeneral:
    if "CISO" not in departmentsViewed:
        g "This is the CISO's office. Maybe you'll end up here one day. This is where a large number of managerial decisions happen, obviously."
        $ officeEventToView = False
        $ departmentsViewed.append("CISO")
    menu:
        #If event to view, use the name of the event and display it as a button. Does not support multiple events for the same department YET. Ditto for all other departments.
        #TODO: Abstract number of events per department to allow multiple at once. REPEAT THIS TO-DO AD INFINITUM FOR ALL DEPARTMENTS.
        "[event]" if officeEventToView and len(event)>0 and event != "Stolen cake":
            call eventLookup
            call screen eventViewer
        "Could you repeat the department's function?":
            $ departmentsViewed.remove("CISO")
            jump tutorialOfficeGeneral
        "... An \"event\"\?" if len(departmentsViewed) > 7:
            if tutorialComplete:
                "Events will be marked by an exclamation mark next to their respective department."
                "The bottom option will always take you back to the department list, no strings attached."
            else:
                g "There's always something to do around here."
                g "Whether or not it's immediately obvious... Well, it usually is."
                g "Speak of the devil, looks like something's going on in the cubicles. Let's go have a look."
                $ officeWarning = False
                $ cisoEventTrigger = False
                $ event = "Stolen cake"
                $ cubicleEventToView = True
            jump tutorialOfficeGeneral
        "Never mind.":
                call screen mainGameplayLoop

#Tutorial label to handle event trees for R&D Department.
label tutorialResDevGeneral:
    if "R&D" not in departmentsViewed:
        g "This is the R&D department. A lot of the future-facing projects are handled here, so treat them with respect. Our future banks on them doing their jobs."
        $ rdEventToView = False
        $ departmentsViewed.append("R&D")
    if len(departmentsViewed) > 7 and officeWarning and cisoEventTrigger == False:
        g "We should go to the CISO's office. I've been told there might be an \"event\" there worth looking at."
        $ cisoEventTrigger = True
    menu:
        "[event]" if rdEventToView and len(event) > 0:
            call eventLookup
            call screen eventViewer
        "Could you repeat the department's function?":
            $ departmentsViewed.remove("R&D")
            jump tutorialResDevGeneral
        "Never mind.":
                call screen mainGameplayLoop

#Tutorial label to handle event trees for Helpdesk.
label tutorialHelpDeskGeneral:
    if "Helpdesk" not in departmentsViewed:
        g "Welcome to the Help Desk. Were you a regular employee at our company, you'd come here to get your things fixed. Since you're on the other side of the glass, you're gonna be doing the fixing."
        $ deskEventToView = False
        $ departmentsViewed.append("Helpdesk")
    if len(departmentsViewed) > 7 and officeWarning and cisoEventTrigger == False:
        g "We should go to the CISO's office. I've been told there might be an \"event\" there worth looking at."
        $ cisoEventTrigger = True
    menu:
        "[event]" if deskEventToView and len(event) > 0:
            call eventLookup
            call screen eventViewer
        "Could you repeat the department's function?":
            $ departmentsViewed.remove("Helpdesk")
            jump tutorialHelpDeskGeneral
        "Never mind.":
                call screen mainGameplayLoop

#Tutorial label to handle event trees for Cybersecurity.
label tutorialCyberSecGeneral:
    if "Cybersecurity" not in departmentsViewed:
        g "I'm sure the Cybersecurity department needs no introduction. They're the people responsible for making sure everything here stays safe and secure."
        $ cyberEventToView = False
        $ departmentsViewed.append("Cybersecurity")
    if len(departmentsViewed) > 7 and officeWarning and cisoEventTrigger == False:
        g "We should go to the CISO's office. I've been told there might be an \"event\" there worth looking at."
        $ cisoEventTrigger = True
    menu:
        "[event]" if cyberEventToView and len(event) > 0:
            call eventLookup
            call screen eventViewer
        "Could you repeat the department's function?":
            $ departmentsViewed.remove("Cybersecurity")
            jump tutorialCyberSecGeneral
        "Never mind.":
                call screen mainGameplayLoop

#Tutorial label to handle event trees for Server Room.
label tutorialServersGeneral:
    if "Servers" not in departmentsViewed:
        g "This is the Server room. As you might expect, it holds all of our servers. If something goes wrong in here, it might be lights-out for a while."
        $ serverEventToView = False
        $ departmentsViewed.append("Servers")
    if len(departmentsViewed) > 7 and officeWarning and cisoEventTrigger == False:
        g "We should go to the CISO's office. I've been told there might be an \"event\" there worth looking at."
        $ cisoEventTrigger = True
    menu:
        "[event]" if serverEventToView and len(event) > 0:
            call eventLookup
            call screen eventViewer
        "Could you repeat the department's function?":
            $ departmentsViewed.remove("Servers")
            jump tutorialServersGeneral
        "Never mind.":
                call screen mainGameplayLoop

#Tutorial label to handle event trees for Cubicles.
label tutorialCubicleGeneral:
    if "Cubicles" not in departmentsViewed:
        g "These are the Cubicles. Our main work force for the department is in here."
        g "While you might write this off initially, workplace politics here can get pretty heated. I'd try to avoid that if you can."
        $ cubicleEventToView = False
        $ departmentsViewed.append("Cubicles")
    if len(departmentsViewed) > 7 and officeWarning and cisoEventTrigger == False:
        g "We should go to the CISO's office. I've been told there might be an \"event\" there worth looking at."
        $ cisoEventTrigger = True
    menu:
        "[event]" if cubicleEventToView and len(event) > 0:
            "When handling an event, a list of 2 to 5 options will appear. What response you choose can and will affect your score at the end of the game, and may even end your game early."
            "Much like the real world, there is, more often than not, no truly correct or incorrect answer."
            "Most importantly, these events are chosen randomly from a pool. You may see the same event four times, not at all, or face impossible tasks. How you handle it is, once again, up to you."
            call eventLookup
            call screen eventViewer
        "Could you repeat the department's function?" if cubicleEventToView == False:
            $ departmentsViewed.remove("Cubicles")
            jump tutorialCubicleGeneral
        "Repeat how the events play out." if cubicleEventToView == False and event == "Stolen cake":
            "When handling an event, a list of 2 to 5 options will appear. What response you choose can and will affect your score at the end of the game, and may even end your game early."
            "Much like the real world, there is, more often than not, no truly correct or incorrect answer."
            "Most importantly, these events are chosen randomly from a pool. You may see the same event four times, not at all, or face impossible tasks. How you handle it is, once again, up to you."
            jump tutorialCubicleGeneral
        "Never mind.":
                call screen mainGameplayLoop

#Tutorial label to handle event trees for Device Storage.
label tutorialStorageGeneral:
    if "Storage" not in departmentsViewed:
        g "Welcome to the Storage closet. Our backup devices, authenticator cards, loaner laptops, and everything in between stays in here."
        g "Well... Now that I think about it, we should probably get you some stuff out of here while we're here."
        $ storageEventToView = False
        $ departmentsViewed.append("Storage")
    if len(departmentsViewed) > 7 and officeWarning and cisoEventTrigger == False:
        g "We should go to the CISO's office. I've been told there might be an \"event\" there worth looking at."
        $ cisoEventTrigger = True
    menu:
        "[event]" if storageEventToView and len(event) > 0:
            call eventLookup
            call screen eventViewer
        "Could you repeat the department's function?":
            $ departmentsViewed.remove("Storage")
            jump tutorialStorageGeneral
        "Never mind.":
                call screen mainGameplayLoop

#Tutorial label to handle event trees for Copy Room.
label tutorialCopierGeneral:
    if "Copier" not in departmentsViewed:
        g "This is the copy room. Between you and me, these printers are colossal headaches... Not to mention they're a nightmare to keep secure."
        g "You didn't hear that from me though."
        $ copyEventToView = False
        $ departmentsViewed.append("Copier")
    if len(departmentsViewed) > 7 and officeWarning and cisoEventTrigger == False:
        g "We should go to the CISO's office. I've been told there might be an \"event\" there worth looking at."
        $ cisoEventTrigger = True
    menu:
        "[event]" if copyEventToView and len(event) > 0:
            call eventLookup
            call screen eventViewer
        "Could you repeat the department's function?":
            $ departmentsViewed.remove("Copier")
            jump tutorialCopierGeneral
        "Never mind.":
                call screen mainGameplayLoop
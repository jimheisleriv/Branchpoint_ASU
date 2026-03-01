define b = Character("Brendan")

label tutorial:
    $ tutorialMode = True

    scene bg main_hq_hall

    "It's your first day on the job..."

    "Despite the fact the keycard in your hand is clearly labeled 'Intern', you're determined to do the job right."

    "The main door to the wing opens, and a somewhat friendly face greets you as you enter."

    scene bg helpdesk_1

    show b_happy

    b "Welcome in! What is it this time, laptop trouble? Authenticator on the fritz? Access permission issues?"

    b "Ohh, a green keycard? So you're the intern they were telling me about."

    b "Well, we're glad to have you! I know this place ain't much, but we hope you'll excel while you're here!"

    b "Personally, I'm about to head to lunch, but I'll hand it off to main-man Gary and he'll show you the ropes."

    hide b_happy
    show g_mad

    g "Yeah we just kinda keep the beeps beepin and the boops boopin"

    g "lmao"

    hide g_mad

    # This ends the game.

    #jump start

    call screen mainGameplayLoop

    return
label tutorialConclusion:
    g "[talkBack]"
    g "Well, looks like you're getting the hang of things. I think we'd do well to keep you around even after your time here is up."
    g "That said... I've still got work to do. Come swing by my department if you need a hand."
    g "Otherwise, I think you're on your own for now."
    $ event = "Copier threat"

label tutorialEventLibrary:

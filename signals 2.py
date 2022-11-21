signals = [".",
           "Weather warning: there is a storm approaching",
           "~",
           "Helicopter arriving McMurdo station 10:00 Tuesday",
           "**",
           "First aid kit needed at far camp",
           "*&_)*&^%^&*%^$~@:~",
           "Food delivery drop will be delayed by 48 hours",
           "Repairs needed at the observation platform",
           "Urgent - update all anti-virus systems",
           "Please re-send meteorological data",
           "234724u2u23u888",
           ".."
           "asjdha## djhaidj# ddjiadj#",
           "Medical officer requested at main base",
           " %",
           "43umcu3rg0ucthgm@:;<",
           "Penguin migration has begun 2 weeks early",
           "Solar flare may affect radio communication",
        "-"]
good_signals = []
bad_signals = []

for i in signals:
    if len(i) < 3:
        bad_signals.append(i)
    else:
        if "#" in i:
            bad_signals.append(i)
        else:
            if " " in i:
                good_signals.append(i)
            else:
                bad_signals.append(i)

print("Good signals" , good_signals)
print("Bad signals" , bad_signals)
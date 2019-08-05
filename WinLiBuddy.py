# import pyperclip
# import re

# rin = pyperclip.paste()
# rin is an input string variable I am using inside this script
rin = input("Bitte gib deinen Link ein")
rout = None
# rout is the output string variable I am unsing inside this script. The start has to be empty
print("This input is detected: ", + rin)

if rin.find("/"):
    print("Path in Linux format detected")
    liste = rin.split("/")
    rout = "\\strongbow" # start value, works only on server with name strongbow for moment. Has to changed to a variable which can be detemined inside a setting file
    for n in liste
        if liste[n] = "/"
            rout = (rout, "\")
        else
            rout = (rout, + liste[n])
#    pyperclip.copy(r)
    print("the path ", + rout, + " has been copied to clipboard. This is Windows Format")
elif rin.find("\""):
    print("Path in Windows format detected")
    liste = r.split("\")
    rout = None  # maybe this makes no sense
    rout = "shares/"  # start value, works only on strongbow server for moment. Has to changed to a variable which can be detemined inside a setting file
    for n in liste:
        if liste[n] = "\":
            rout = (rout, "/")
        else:
            rout = (rout, + liste[n])
#    pyperclip.copy(r)
    print("the path ", + rout, + " has been copied to clipboard. This is Linux Format")
else:
    print("I could not detect anything")

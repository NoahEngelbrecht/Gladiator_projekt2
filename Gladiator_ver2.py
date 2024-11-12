# I detta projekt ska jag skapa ett textbaserat gladiatorspel där spelaren väljer en gladiator och slåss mot en AI motståndare
# Spelaren ska få flera olika val på attacker. Spelaren kommer även kunna välja vapen och påverkas av en publik som avgör gladiatorns öde.
# Målet med detta spel är att spelaren ska få en unik och dynamisk upplevelse med unika gladiatorer och strategiska val. 

# Detta är min start för mitt projekt som kan kommer basera på min tidigare kod på baserat på mitt tidigare spel Drakborgs stridsspel.
import random

hälsopoäng = 10
motståndare = 10
attacker = ["slag", "spark", "kast"]


print("Välkommen till Gladiatorspelet.\n")
print("Du har tre olika attacksalternativ, slag, spark och kast")
print("De olika attackerna kan göra olika mycket skada, slag mellan 1-3, spark mellan 1-3 och kast mellan 2-5")
print("De olika attackerna har även en chans att missa så det är inte alltid bäst att kasta.\n")


# Val mellan blodiga eller barnvänliga beskrivningar
beskrivning_val = input("Vill du ha blodiga beskrivningar eller barnvänliga beskrivningar? (blodiga/barnvänliga): ").lower()

if beskrivning_val == "blodiga":
    blodiga = True
elif beskrivning_val == "barnvänliga":
    blodiga = False
else:
    print("Ogiltigt val! Vi väljer barnvänliga beskrivningar åt dig.")
    blodiga = False

strid = True

while strid:
    dator = random.choice(attacker)

    print("Du har just nu", hälsopoäng, "hälsopoäng kvar.")
    print("Din fiende har", motståndare, "hälsopoäng kvar.")

    val = input("Vilket väljer du: slag, spark eller kast? ").lower()
    print("Du valde:", val)
    print("Din motståndare valde:", dator)

    # Bestämmer chansen för en attack att missa.
    # Sedan slumpas chasen i nästa if sats.
    if val == "slag":
        miss_chans = 0.2
    elif val == "spark":
        miss_chans = 0.31415926538
    elif val == "kast":
        miss_chans = 0.33333333333

    if dator == "slag":
        misschans_dator = 0.271828
    elif dator == "spark":
        misschans_dator = 0.33333333
    elif dator == "kast":
        misschans_dator = 0.377

    if random.random() < miss_chans:
        skada = random.randint(1,2)
        print("Din attack missade!")
        hälsopoäng -= skada
    elif random.random() < misschans_dator:
        skada = random.randint(1,2)
        print("Motståndarens attack missade!")
        motståndare -= skada

    elif val == dator:
        print("Ni valde samma. Båda missar. Ni stirrar på varandra med lömsk blick.")
    else:
        if val == "slag" and dator == "spark":
            skada = random.randint(1, 3)
            if blodiga:
                print("Din motståndare sparkade dig i magen, du känner blodsmak!")
            else:
                print("Din motståndare sparkade dig, det gjorde ont!")
            hälsopoäng -= skada
        elif val == "slag" and dator == "kast":
            skada = random.randint(2, 5)
            if blodiga:
                print("Din motståndare kastade ner dig, blodet rinner!")
            else:
                print("Din motståndare kastade ner dig på marken.")
            hälsopoäng -= skada
        elif val == "spark" and dator == "slag":
            skada = random.randint(1, 3)
            if blodiga:
                print("Du sparkade din motståndare i ansiktet, blod stänker!")
            else:
                print("Du sparkade din motståndare, vilken träff!")
            motståndare -= skada
        elif val == "spark" and dator == "kast":
            skada = random.randint(2, 5)
            if blodiga:
                print("Din spark krossar motståndarens ben!")
            else:
                print("Du sparkade din motståndare, effektivt!")
            motståndare -= skada
        elif val == "kast" and dator == "spark":
            skada = random.randint(1, 3)
            if blodiga:
                print("Din motståndare sparkade dig så hårt att blodet forsar!")
            else:
                print("Motståndaren sparkade dig hårt!")
            hälsopoäng -= skada
        elif val == "kast" and dator == "slag":
            skada = random.randint(2, 5)
            if blodiga:
                print("Du kastade ner motståndaren i marken, blod överallt!")
            else:
                print("Du kastade ner motståndaren på marken!")
            motståndare -= skada

    if hälsopoäng <= 0:
        print("Du har förlorat striden!")
        strid = False
    elif motståndare <= 0:
        print("Du har vunnit striden!")
        strid = False
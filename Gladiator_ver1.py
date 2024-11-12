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
print("De olika attackerna kan göra olika mycket skada, slag mellan 1-3, spark mellan 1-3 och kast mellan 2-5\n")

strid = True

while strid:
    dator = random.choice(attacker)

    print("Du har just nu", hälsopoäng, "hälsopoäng kvar.")
    print("Din fiende har", motståndare, "hälsopoäng kvar.")

    val = input("Vilket väljer du: slag, spark eller kast? ").lower()
    print("Du valde:", val)
    print("Din motståndare valde:", dator)

    if val == "slag":
        miss_chans = 0.2
    elif val == "spark":
        miss_chans = 0.3
    elif val == "kast":
        miss_chans = 0.4

    if random.random() < miss_chans:
        skada = random.randint(1,2)
        print(f"Din attack missade!\nDu förlorade {hälsopoäng} hälsopoäng")
        hälsopoäng -= skada
    elif val == dator:
        print("Ni valde samma. Båda missar. Ni stirrar på varandra med lömsk blick.")
    elif val == "slag" and dator == "spark":
        skada = random.randint(1,3)
        print("Din motståndare landade en spark på dig.")
        hälsopoäng -= skada
    elif val == "slag" and dator == "kast":
        skada = random.randint(2,5)
        print("Din motståndare kastade ner dig på marken.")
        hälsopoäng -= skada
    elif val == "spark" and dator == "slag":
        skada = random.randint(1,3)
        print("Du landade en spark på din motståndare.")
        motståndare -= skada
    elif val == "spark" and dator == "kast":
        skada = random.randint(2,5)
        print("Spark är mer effektivt än kast och du sparkar motståndaren.")
        motståndare -= skada
    elif val == "kast" and dator == "spark":
        skada = random.randint(1,3)
        print("Spark är mer effektivt än kast och du motståndaren landar en spark på dig.")
        hälsopoäng -= skada
    elif val == "kast" and dator == "slag":
        skada = random.randint(2,5)
        print("Kast är mer effektivt än slag och du kastar motståndaren mot marken.")
        motståndare -= skada

    if hälsopoäng <= 0:
        print("Du har förlorat striden!")
        strid = False
    elif motståndare <= 0:
        print("Du har vunnit striden!")
        strid = False

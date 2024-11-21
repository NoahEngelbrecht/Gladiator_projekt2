import random

# Gladiatorval med specifika egenskaper
gladiatorer = {
    "Murmillo": {
        "hälsopoäng": 25,
        "specialattack": "sköldstöt",
        "beskrivning": "En tungt beväpnad gladiator med stor sköld."
    },
    "Retiarius": {
        "hälsopoäng": 18,
        "specialattack": "nätkast",
        "beskrivning": "En snabb och smidig gladiator med ett nät och treudd."
    },
    "Thraex": {
        "hälsopoäng": 22,
        "specialattack": "snabbt hugg",
        "beskrivning": "En offensiv gladiator med böjt svärd."
    }
}

# Välj gladiator
print("Välj din gladiator:")
for namn, egenskaper in gladiatorer.items():
    print(f"{namn}: {egenskaper['beskrivning']} (Hälsa: {egenskaper['hälsopoäng']}, Specialattack: {egenskaper['specialattack']})")

# Spelaren väljer en gladiator; default är "Murmillo" vid ogiltigt val
gladiator_val = input("Välj din gladiator (Murmillo, Retiarius, Thraex): ").capitalize()
if gladiator_val not in gladiatorer:
    print("Ogiltigt val! Vi väljer Murmillo åt dig.")
    gladiator_val = "Murmillo"

# Tilldela hälsopoäng och specialattack baserat på spelarens valda gladiator
hälsopoäng = gladiatorer[gladiator_val]["hälsopoäng"]
specialattack = gladiatorer[gladiator_val]["specialattack"]

# Hälsopoäng för motståndaren
motståndare = 20

# Vapenval med specifika attacker och egenskaper
if gladiator_val == "Murmillo":
    print("Du valde gladiatorn Murmillo och har därför en extra attack där du kan kasta din sköld. \n")
    vapen = {
    "Gladius": {
        "attacker": ["hugg", "parering", "stöt", "skölda"],
        "träffchanser": [1, 0.7, 0.55, 0.60],  # Chans att träffa med respektive attack
        "skador": [(1, 3), (1, 2), (2, 5), (3,4)],  # Skadespann för varje attack
        "beskrivning": "Ett snabbt och balanserat svärd."
    },
    "Trident": {
        "attacker": ["stöt", "blockering", "slunga", "skölda"],
        "träffchanser": [0.6, 0.8, 0.35, 0.7],
        "skador": [(2, 4), (1, 2), (3, 6), (3, 4)], 
        "beskrivning": "En kraftfull treudd med hög skada men låg träffchans."
    },
    "Thraex": {
        "attacker": ["stick", "kasta", "skydda","skölda"],
        "träffchanser": [0.5, 0.37, 0.7, 0.65],
        "skador": [(1, 4), (3, 5), (1, 2), (3,4)],
        "beskrivning": "Ett långt spjut med räckvidd och skada."
    }
}

if gladiator_val == "Retiarius":
    print("Du valde gladiatorn Retiarius och har därför en extra attack där du kan kasta ett nät. \n")
    vapen = {
    "Gladius": {
        "attacker": ["hugg", "parering", "stöt", "nät"],
        "träffchanser": [0.8, 0.9, 0.69, 0.23],  # Chans att träffa med respektive attack
        "skador": [(1, 3), (1, 2), (2, 5), (8,10)],  # Skadespann för varje attack
        "beskrivning": "Ett snabbt och balanserat svärd."
    },
    "Trident": {
        "attacker": ["stöt", "blockering", "slunga", "nät"],
        "träffchanser": [0.7, 0.8, 0.65, 0.23],
        "skador": [(2, 4), (1, 2), (3, 6), (8, 10)], 
        "beskrivning": "En kraftfull treudd med hög skada men låg träffchans."
    },
    "Spear": {
        "attacker": ["stick", "kasta", "skydda", "nät"],
        "träffchanser": [0.70, 0.55, 0.8, 0.23],
        "skador": [(1, 4), (3, 5), (1, 2), (8,10)],
        "beskrivning": "Ett långt spjut med räckvidd och skada."
    }
}

if gladiator_val == "Thraex":
    print("Du valde gladiatorn Thraex och har därför en extra attack där du kan göra ett snabbt hugg. \n")
    vapen = {
    "Gladius": {
        "attacker": ["hugg", "parering", "stöt"],
        "träffchanser": [1, 0.8, 0.55, 0.80],  # Chans att träffa med respektive attack
        "skador": [(1, 3), (1, 2), (2, 5), (3,4)],  # Skadespann för varje attack
        "beskrivning": "Ett snabbt och balanserat svärd."
    },
    "Trident": {
        "attacker": ["stöt", "blockering", "slunga", "hugg"],
        "träffchanser": [0.7, 0.8, 0.45, 1],
        "skador": [(2, 4), (1, 2), (3, 6), (1, 3)], 
        "beskrivning": "En kraftfull treudd med hög skada men låg träffchans."
    },
    "Spear": {
        "attacker": ["stick", "kasta", "skydda","hugg"],
        "träffchanser": [0.6, 0.45, 0.7, 1],
        "skador": [(1, 4), (3, 5), (1, 2), (1,3)],
        "beskrivning": "Ett långt spjut med räckvidd och skada."
    }
}

# Välj vapen
print("\nVälj ditt vapen:")
for namn, egenskaper in vapen.items():
    print(f"{namn}: {egenskaper['beskrivning']}")

# Spelaren väljer ett vapen; default är "Gladius" vid ogiltigt val
vapen_val = input("Välj ditt vapen (Gladius, Trident, Spear): ").capitalize()
if vapen_val not in vapen:
    print("Ogiltigt val! Vi väljer Gladius åt dig.")
    vapen_val = "Gladius"

# Tilldelar attacker, träffchanser och skador baserat på spelarens valda vapen
attacker, träffchanser, skador = vapen[vapen_val]["attacker"], vapen[vapen_val]["träffchanser"], vapen[vapen_val]["skador"]

# Välj om spelet ska ha blodiga eller barnvänliga beskrivningar
blodiga = input("Vill du ha blodiga eller barnvänliga beskrivningar? (blodiga/barnvänliga): ").lower() == "blodiga"

# Funktion för att hantera träffar och missar under striden
def hantera_attack(val, dator):
    # Index för spelarens och datorns val, för att hämta träffchanser och skador
    val_index, dator_index = attacker.index(val), attacker.index(dator)
    
    # Slumpar missar för både spelare och dator baserat på deras träffchanser
    miss_spelare = random.random() > träffchanser[val_index]
    miss_dator = random.random() > träffchanser[dator_index]

    # Tilldelar skada baserat på om träffen lyckades eller missade
    skada_dator = random.randint(*skador[dator_index]) if not miss_dator else 0
    skada_spelare = random.randint(*skador[val_index]) if not miss_spelare else 0

    # Utskrift beroende på träffar och missar
    if miss_spelare and miss_dator:
        print("Båda missade!")
    elif miss_spelare:
        print("Din attack missade!")
        print(f"Motståndaren attackerar dig och gör {skada_dator} skada")
    elif miss_dator:
        print("Motståndarens attack missade!")
        print(f"Du träffar motståndaren och gör {skada_spelare} skada")
    else:
        # Blodig eller barnvänlig beskrivning beroende på spelarens val
        print(f"Du attackerar blodigt! Motståndaren förlorar {skada_spelare} hälsopoäng men du tappar {skada_dator} hälsopoäng" if blodiga else f"Du träffar din motståndare! Motståndaren förlorar {skada_spelare} men du tar {skada_dator} skada.")
    
    return skada_dator, skada_spelare  # Returnerar skadan som utdelats av både dator och spelare

# Stridens huvudloop
while hälsopoäng > 0 and motståndare > 0:
    # Datorn väljer slumpmässigt en attack från tillgängliga attacker
    dator = random.choice(attacker)
    print(f"\nDin hälsa: {hälsopoäng}, Motståndarens hälsa: {motståndare}")
    
    # Spelaren väljer en attack
    val = input(f"Välj en attack ({', '.join(attacker)}): ").lower()

    # Kontrollera om spelarens val är en giltig attack
    if val in attacker:
        # Kalla på attackfunktionen för att hantera träffar och skador
        dator_skada, spelare_skada = hantera_attack(val, dator)
        
        # Justera hälsopoäng baserat på utdelad skada
        hälsopoäng -= dator_skada
        motståndare -= spelare_skada
    else:
        print("Ogiltigt val!")  # Meddelande vid ogiltig inmatning

# Utskrift av slutresultat beroende på vem som förlorar alla hälsopoäng
if hälsopoäng <= 0:
    print("Du förlorade striden!")
else:
    print("Du har vunnit striden")

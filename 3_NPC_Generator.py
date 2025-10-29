import streamlit as st
from streamlit_extras.row import row
import random
from profanityfilter import ProfanityFilter

pf = ProfanityFilter()

classification_roll = 0
ancestry_roll = 0
class_roll = 0
gender_roll = 0
level = 0
disposition_roll = 0
alignment_roll = 0
goaltivation_roll = 0

name = ""
ancestryoptions = ["Choose Classification First."]
ancestry = None
dndclass = None
classification = None
gender = None
disposition = None
alignment = None
goaltivation = None

disallow_generation = False
No_HOF = True

def random_roll(min_value, max_value, modifier=0):
    return random.randint(min_value, max_value)+modifier

## Use session_state and a callback so generated values persist across reruns
# Initialize required session keys with defaults if missing
for key, val in {
    "generated": False,
    "name": name,
    "classification": classification,
    "ancestry": ancestry,
    "dndclass": dndclass,
    "level": level,
    "gender": gender,
    "disposition": disposition,
    "alignment": alignment,
    "goaltivation": goaltivation,
    "No_HOF": No_HOF
}.items():
    if key not in st.session_state:
        st.session_state[key] = val

def generate_npc():
    # use globals (values set earlier in the run from widgets are available)
    global classification, ancestry, dndclass, name, level, gender, disposition, alignment, goaltivation, No_HOF

    # Generate Classification
    if classification is None:
        if st.session_state.accurate_distributions:
            classification_roll = random_roll(1, 12)
            if classification_roll <= 6:
                classification = "Naturalborn"
            elif classification_roll <= 10:
                classification = "Oddity"
            else:
                classification = "Outlander"
        else:
            classification_roll = random_roll(1, 3)
            if classification_roll == 1:
                classification = "Naturalborn"
            elif classification_roll == 2:
                classification = "Oddity"
            else:
                classification = "Outlander"

    # Generate Ancestry
    if ancestry is None:
        ancestry_roll = random_roll(1, 200)
        if classification == "Naturalborn":
            # (the same series of conditions as before — condensed here for brevity)
            if ancestry_roll <= 3:
                ancestry = "Aasimar"
            elif ancestry_roll <= 11:
                ancestry = "Dragonborn (Chromatic)"
            elif ancestry_roll <= 19:
                ancestry = "Dragonborn (Metallic)"
            elif ancestry_roll <= 22:
                ancestry = "Dwarf (Gray) [Duergar]"
            elif ancestry_roll <= 26:
                ancestry = "Dwarf (Hill)"
            elif ancestry_roll <= 30:
                ancestry = "Dwarf (Mountain)"
            elif ancestry_roll <= 32:
                ancestry = "Dwarf (Seaborn)"
            elif ancestry_roll <= 35:
                ancestry = "Dwarf (Strongblood)"
            elif ancestry_roll <= 37:
                ancestry = "Elf (Ash)"
            elif ancestry_roll <= 40:
                ancestry = "Elf (Dark) [Drow]"
            elif ancestry_roll <= 45:
                ancestry = "Elf (High)"
            elif ancestry_roll <= 47:
                ancestry = "Elf (Sea)"
            elif ancestry_roll <= 52:
                ancestry = "Elf (Wood)"
            elif ancestry_roll <= 53:
                ancestry = "Faunus (Bear)"
            elif ancestry_roll <= 54:
                ancestry = "Faunus (Bird)"
            elif ancestry_roll <= 55:
                ancestry = "Faunus (Cat)"
            elif ancestry_roll <= 56:
                ancestry = "Faunus (Cow/Bull)"
            elif ancestry_roll <= 57:
                ancestry = "Faunus (Deer)"
            elif ancestry_roll <= 58:
                ancestry = "Faunus (Dog)"
            elif ancestry_roll <= 59:
                ancestry = "Faunus (Fox)"
            elif ancestry_roll <= 60:
                ancestry = "Faunus (Horse)"
            elif ancestry_roll <= 61:
                ancestry = "Faunus (Pig)"
            elif ancestry_roll <= 62:
                ancestry = "Faunus (Rabbit)"
            elif ancestry_roll <= 63:
                ancestry = "Faunus (Raccoon)"
            elif ancestry_roll <= 64:
                ancestry = "Faunus (Sheep/Goat)"
            elif ancestry_roll <= 65:
                ancestry = "Faunus (Wolf)"
            elif ancestry_roll <= 69:
                ancestry = "Gnome (Deep)"
            elif ancestry_roll <= 74:
                ancestry = "Gnome (Forest)"
            elif ancestry_roll <= 78:
                ancestry = "Gnome (Rock)"
            elif ancestry_roll <= 81:
                ancestry = "Goblin"
            elif ancestry_roll <= 84:
                ancestry = "Goblin (Hoardshine)"
            elif ancestry_roll <= 86:
                ancestry = "Goliath"
            elif ancestry_roll <= 87:
                ancestry = "Goliath (Cloudborn)"
            elif ancestry_roll <= 88:
                ancestry = "Goliath (Fireborn)"
            elif ancestry_roll <= 89:
                ancestry = "Goliath (Frostborn)"
            elif ancestry_roll <= 90:
                ancestry = "Goliath (Hillborn)"
            elif ancestry_roll <= 91:
                ancestry = "Goliath (Stoneborn)"
            elif ancestry_roll <= 104:
                ancestry = "Half-Elf"
            elif ancestry_roll <= 110:
                ancestry = "Half-Orc"
            elif ancestry_roll <= 113:
                ancestry = "Half-Orc (Coldheart)"
            elif ancestry_roll <= 118:
                ancestry = "Halfling (Lightfoot)"
            elif ancestry_roll <= 121:
                ancestry = "Halfling (Lotusden)"
            elif ancestry_roll <= 125:
                ancestry = "Halfling (Stout)"
            elif ancestry_roll <= 141:
                ancestry = "Human"
            elif ancestry_roll <= 147:
                ancestry = "Kobold"
            elif ancestry_roll <= 156:
                ancestry = "Leonin"
            elif ancestry_roll <= 169:
                ancestry = "Orc"
            elif ancestry_roll <= 175:
                ancestry = "Tabaxi"
            elif ancestry_roll <= 178:
                ancestry = "Tabaxi (Softpaw)"
            elif ancestry_roll <= 191:
                ancestry = "Tiefling"
            else:
                ancestry = "Tortle"
        elif classification == "Oddity":
            if ancestry_roll <= 12:
                ancestry = "Aarakocra"
            elif ancestry_roll <= 18:
                ancestry = "Aasimar (Mystic)"
            elif ancestry_roll <= 26:
                ancestry = "Dragonborn (Gem)"
            elif ancestry_roll <= 32:
                ancestry = "Dragonborn (Radiant)"
            elif ancestry_roll <= 40:
                ancestry = "Elf (Pallid)"
            elif ancestry_roll <= 46:
                ancestry = "Halfling (Jinx)"
            elif ancestry_roll <= 52:
                ancestry = "Kalashtar"
            elif ancestry_roll <= 57:
                ancestry = "Kenku"
            elif ancestry_roll <= 60:
                ancestry = "Kenku (Harrowfeather)"
            elif ancestry_roll <= 63:
                ancestry = "Kenku (Shroudeye)"
            elif ancestry_roll <= 64:
                ancestry = "Lineage (Dhamphir)"
            elif ancestry_roll <= 65:
                ancestry = "Lineage (Disembodied)"
            elif ancestry_roll <= 66:
                ancestry = "Lineage (Hexblood)"
            elif ancestry_roll <= 68:
                ancestry = "Lineage (Reborn)"
            elif ancestry_roll <= 71:
                ancestry = "Lupin (Fabled)"
            elif ancestry_roll <= 74:
                ancestry = "Lupin (Isolated)"
            elif ancestry_roll <= 77:
                ancestry = "Lupin (Leader)"
            elif ancestry_roll <= 84:
                ancestry = "Lupin (Pack)"
            elif ancestry_roll <= 85:
                ancestry = "Lustrous (Ore)"
            elif ancestry_roll <= 87:
                ancestry = "Lustrous (Precious)"
            elif ancestry_roll <= 89:
                ancestry = "Lustrous (Semi-Precious)"
            elif ancestry_roll <= 101:
                ancestry = "Macawkra"
            elif ancestry_roll <= 103:
                ancestry = "Nymph (Alseid)"
            elif ancestry_roll <= 105:
                ancestry = "Nymph (Asteria)"
            elif ancestry_roll <= 108:
                ancestry = "Nymph (Aurae)"
            elif ancestry_roll <= 110:
                ancestry = "Nymph (Dryad)"
            elif ancestry_roll <= 112:
                ancestry = "Nymph (Lampad)"
            elif ancestry_roll <= 114:
                ancestry = "Nymph (Naiad)"
            elif ancestry_roll <= 116:
                ancestry = "Nymph (Oread)"
            elif ancestry_roll <= 128:
                ancestry = "Owlin"
            elif ancestry_roll <= 134:
                ancestry = "Rakin (Posskin)"
            elif ancestry_roll <= 140:
                ancestry = "Rakin (Tanukin)"
            elif ancestry_roll <= 146:
                ancestry = "Rakin (Urkin)"
            elif ancestry_roll <= 152:
                ancestry = "Ratfolk (Packrat)"
            elif ancestry_roll <= 158:
                ancestry = "Ratfolk (Ratical)"
            elif ancestry_roll <= 164:
                ancestry = "Ratfolk (Scourgerat)"
            elif ancestry_roll <= 170:
                ancestry = "Tengu"
            elif ancestry_roll <= 182:
                ancestry = "Tiefling (Amethyst Bloodline)"
            elif ancestry_roll <= 194:
                ancestry = "Tiefling (Gold Bloodline)"
            else:
                ancestry = "Warforged"
        else:  # Outlander
            if ancestry_roll <= 9:
                ancestry = "Aasimar (Cosmic)"
            elif ancestry_roll <= 17:
                ancestry = "Aasimar (Elfriche)"
            elif ancestry_roll <= 28:
                ancestry = "Changeling"
            elif ancestry_roll <= 44:
                ancestry = "Dragonborn (Faerie)"
            elif ancestry_roll <= 55:
                ancestry = "Dragonborn (Moonstone)"
            elif ancestry_roll <= 71:
                ancestry = "Elf (Eladrin)"
            elif ancestry_roll <= 87:
                ancestry = "Elf (Shadar-Kai)"
            elif ancestry_roll <= 93:
                ancestry = "Elf (Snow)"
            elif ancestry_roll <= 104:
                ancestry = "Firbolg"
            elif ancestry_roll <= 110:
                ancestry = "Genasi (Air)"
            elif ancestry_roll <= 116:
                ancestry = "Genasi (Earth)"
            elif ancestry_roll <= 122:
                ancestry = "Genasi (Fire)"
            elif ancestry_roll <= 128:
                ancestry = "Genasi (Water)"
            elif ancestry_roll <= 131:
                ancestry = "Lunarran (Bloodmoon)"
            elif ancestry_roll <= 134:
                ancestry = "Lunarran (Bluemoon)"
            elif ancestry_roll <= 137:
                ancestry = "Lunarran (Crescent)"
            elif ancestry_roll <= 140:
                ancestry = "Lunarran (Waning)"
            elif ancestry_roll <= 148:
                ancestry = "Metallus (Alloy)"
            elif ancestry_roll <= 156:
                ancestry = "Metallus (Gold)"
            elif ancestry_roll <= 164:
                ancestry = "Opteran (Cityborn)"
            elif ancestry_roll <= 172:
                ancestry = "Opteran (Naturalborn)"
            elif ancestry_roll <= 181:
                ancestry = "Tlakah (High Senye)"
            elif ancestry_roll <= 190:
                ancestry = "Tlakah (Low Senye)"
            else:
                ancestry = "Tlakah (Mid Senye)"

    # Generate Class
    if dndclass is None:
        if st.session_state.player_classes_only:
            class_roll = random_roll(1, 13)
            if class_roll == 1:
                dndclass = "Artificer"
            elif class_roll == 2:
                dndclass = "Fighter"
            elif class_roll == 3:
                dndclass = "Wizard"
            elif class_roll == 4:
                dndclass = "Rogue"
            elif class_roll == 5:
                dndclass = "Cleric"
            elif class_roll == 6:
                dndclass = "Ranger"
            elif class_roll == 7:
                dndclass = "Paladin"
            elif class_roll == 8:
                dndclass = "Bard"
            elif class_roll == 9:
                dndclass = "Druid"
            elif class_roll == 10:
                dndclass = "Monk"
            elif class_roll == 11:
                dndclass = "Warlock"
            elif class_roll == 12:
                dndclass = "Sorcerer"
            else:
                dndclass = "Barbarian"
        else:
            class_roll = random_roll(1, 200)
            if class_roll <= 160:
                dndclass = "Commoner"
            elif class_roll <= 162:
                dndclass = "Alchemist"
            elif class_roll <= 163:
                dndclass = "Artificer"
            elif class_roll <= 165:
                dndclass = "Blacksmith"
            elif class_roll <= 167:
                dndclass = "Brewer"
            elif class_roll <= 168:
                dndclass = "Carpenter"
            elif class_roll <= 169:
                dndclass = "Cobbler"
            elif class_roll <= 171:
                dndclass = "Cook"
            elif class_roll <= 174:
                dndclass = "Enchanter"
            elif class_roll <= 176:
                dndclass = "Engineer"
            elif class_roll <= 177:
                dndclass = "Jeweler"
            elif class_roll <= 178:
                dndclass = "Leatherworker"
            elif class_roll <= 180:
                dndclass = "Mason"
            elif class_roll <= 181:
                dndclass = "Painter"
            elif class_roll <= 182:
                dndclass = "Poisoner"
            elif class_roll <= 183:
                dndclass = "Scroll Scriber"
            elif class_roll <= 184:
                dndclass = "Tailor"
            elif class_roll <= 185:
                dndclass = "Tinkerer"
            elif class_roll <= 186:
                dndclass = "Wand Whittler"
            elif class_roll <= 187:
                dndclass = "Weaver"
            elif class_roll <= 188:
                dndclass = "Wood Carver"
            elif class_roll <= 189:
                dndclass = "Barbarian"
            elif class_roll <= 190:
                dndclass = "Bard"
            elif class_roll <= 191:
                dndclass = "Cleric"
            elif class_roll <= 192:
                dndclass = "Druid"
            elif class_roll <= 193:
                dndclass = "Fighter"
            elif class_roll <= 194:
                dndclass = "Monk"
            elif class_roll <= 195:
                dndclass = "Paladin"
            elif class_roll <= 196:
                dndclass = "Ranger"
            elif class_roll <= 197:
                dndclass = "Rogue"
            elif class_roll <= 198:
                dndclass = "Sorcerer"
            elif class_roll <= 199:
                dndclass = "Warlock"
            else:
                dndclass = "Wizard"

    # Level NPCs with PC Classes 
    if dndclass in ["Artificer", "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"] and level == 0:
        No_HOF = False
        level = 1
        coinflip = random_roll(1, 2)
        while coinflip == 1 and level < 20:
            level += 1
            coinflip = random_roll(1, 2)

    # Generate Gender
    if gender is None:
        gender_roll = random_roll(1, 10)
        if gender_roll <= 3:
            gender = "Male"
        elif gender_roll <= 6:
            gender = "Female"
        elif gender_roll == 7:
            gender = "Non-Binary"
        elif gender_roll == 8:
            gender = "Effeminate Male"
        elif gender_roll == 9:
            gender = "Masculine Female"
        else:
            gender = "Gender Nonconforming"

    # Generate Disposition
    if disposition is None:
        disposition_roll = random_roll(1,6)
        if disposition_roll == 1:
            disposition = "Hostile"
        elif disposition_roll <= 3:
            disposition = "Friendly"
        else:
            disposition = "Indifferent"

    # Generate Alignment
    if alignment is None:
        alignment_roll = random_roll(1,9)
        match alignment_roll:
            case 1:
                alignment = "Lawful Good"
            case 2:
                alignment = "Lawful Unaligned"
            case 3:
                alignment = "Lawful Evil"
            case 4:
                alignment = "Neutral Good"
            case 5:
                alignment = "Neutral Unaligned"
            case 6:
                alignment = "Neutral Evil"
            case 7:
                alignment = "Chaotic Good"
            case 8:
                alignment = "Chaotic Unaligned"
            case 9:
                alignment = "Chaotic Evil"

    # TO-DO: Generate Goaltivation
    if goaltivation is None:
        goaltivation_roll = random_roll(1,200)
        match goaltivation_roll:
            case 1:
                goaltivation = "The NPC wants to return to their homeland or place of origin."
            case 2:
                goaltivation = "The NPC wants to escape their current situation."
            case 3:
                goaltivation = "The NPC wants to obtain romantic love."
            case 4:
                goaltivation = "The NPC wants to obtain fame and adoration."
            case 5:
                goaltivation = "The NPC wants to atone for a past crime."
            case 6:
                goaltivation = "The NPC wants to find a lost relative or friend."
            case 7:
                goaltivation = "The NPC wants to obtain a particular item (a gemstone to make into a wedding ring; a magical sword; a book of secret spells; etc.)."
            case 8:
                goaltivation = "The NPC wants to be the first at something (first to discover a rumored land; first to break a record; etc)."
            case 9:
                goaltivation = "The NPC wants revenge on a rival or hated foe."
            case 10:
                goaltivation = "The NPC wants to build and expand a business."
            case 11:
                goaltivation = "The NPC wants to found a religion."
            case 12:
                goaltivation = "The NPC wants to found a secular organization or brotherhood."
            case 13:
                goaltivation = "The NPC wants to find a cure for a disease, curse, or ailment."
            case 14:
                goaltivation = "The NPC wants to write or create a masterpiece book, song, or piece of art."
            case 15:
                goaltivation = "The NPC wants to complete or add to a collection."
            case 16:
                goaltivation = "The NPC wants to free an enslaved people."
            case 17:
                goaltivation = "The NPC wants to make a lot of money."
            case 18:
                goaltivation = "The NPC wants to sabotage a rival group or organization."
            case 19:
                goaltivation = "The NPC wants to establish peace between rival/warring factions or governments."
            case 20:
                goaltivation = "The NPC wants a family."
            case 21:
                goaltivation = "The NPC just wants someone to take over for a while so they can rest."
            case 22:
                goaltivation = "The NPC wants to fix a broken but necessary piece of equipment, machinery, or other apparatus."
            case 23:
                goaltivation = "The NPC wants to prove that they have surpassed their old master."
            case 24:
                goaltivation = "The NPC wants to learn more about a relative who died or vanished before they were born."
            case 25:
                goaltivation = "The NPC wants to learn a new skill or trade."
            case 26:
                goaltivation = "The NPC wants to end their own life or existence (this goal may not be appropriate for all groups; talk to your players first and reroll if necessary)."
            case 27:
                goaltivation = "The NPC wants to see a fantastical creature in person (a unicorn, a dragon, etc.)."
            case 28:
                goaltivation = "The NPC wants to spread their religion to the uninitiated (possibly even by force)."
            case 29:
                goaltivation = "The NPC wants to avoid a prophesied outcome."
            case 30:
                goaltivation = "The NPC wants to have children (or some other heir to carry on their legacy)."
            case 31:
                goaltivation = "The NPC wants to make a new friend."
            case 32:
                goaltivation = "The NPC wants to shirk their duties and responsibilities."
            case 33:
                goaltivation = "The NPC wants to break up a relationship or drive a wedge between two people (not necessarily a romantic relationship)."
            case 34:
                goaltivation = "The NPC wants relief from a chronic malady, wound, or illness that they suffer from."
            case 35:
                goaltivation = "The NPC wants to make their family (or a respected mentor) proud."
            case 36:
                goaltivation = "The NPC wants to regain something that was lost (wealth, fame, an item, the family property)."
            case 37:
                goaltivation = "The NPC wants to put a stop to criminal activity."
            case 38:
                goaltivation = "The NPC wants to mend a rift between two people (reunite with an estranged father; help two rival blacksmiths work together; etc.)."
            case 39:
                goaltivation = "The NPC wants to solve an ongoing mystery."
            case 40:
                goaltivation = "The NPC wants to protect a friend or family member from something."
            case 41:
                goaltivation = "The NPC wants to reinvent themselves as a new identity."
            case 42:
                goaltivation = "The NPC wants to foster trade between two groups (tribes, countries, cities, etc.)"
            case 43:
                goaltivation = "The NPC wants to reestablish a forgotten holiday or cultural custom."
            case 44:
                goaltivation = "The NPC wants to make people laugh."
            case 45:
                goaltivation = "The NPC wants to prove their power."
            case 46:
                goaltivation = "The NPC wants to prove a theory."
            case 47:
                goaltivation = "The NPC wants to destroy a rival or hated foe."
            case 48:
                goaltivation = "The NPC wants their kingdom or country to expand."
            case 49:
                goaltivation = "The NPC wants to prove a rumor about them is wrong."
            case 50:
                goaltivation = "The NPC wants to win a game or competition."
            case 51:
                goaltivation = "The NPC wants to travel to a thus-far unreachable place (space; time travel; a different dimension; etc.)."
            case 52:
                goaltivation = "The NPC wants to prove something they believe in exists."
            case 53:
                goaltivation = "The NPC wants to destroy or kill a class of people or creatures."
            case 54:
                goaltivation = "The NPC wants to preserve nature at all costs."
            case 55:
                goaltivation = "The NPC wants to decipher a puzzle or something written in a code or ancient language."
            case 56:
                goaltivation = "The NPC wants to repay a debt (not necessarily financial in nature)."
            case 57:
                goaltivation = "The NPC wants to join an elite group or organization."
            case 58:
                goaltivation = "The NPC wants to stay anonymous and not be noticed."
            case 59:
                goaltivation = "The NPC wants to change a law or local custom."
            case 60:
                goaltivation = "The NPC wants to overcome their fear of something."
            case 61:
                goaltivation = "The NPC wants to be more beautiful or attractive."
            case 62:
                goaltivation = "The NPC wants to redeem a villain."
            case 63:
                goaltivation = "The NPC wants to break a bad habit."
            case 64:
                goaltivation = "The NPC wants to remedy something about their personality (an inability to trust people; an explosive temper; always refusing to admit when they're wrong; etc.)"
            case 65:
                goaltivation = "The NPC wants to profess their love to someone they admire."
            case 66:
                goaltivation = "The NPC wants to be taken seriously by someone who doesn't give them due credit."
            case 67:
                goaltivation = "The NPC wants to fix an inaccuracy in the culture's accepted knowledge (prove that the world isn't flat; that there is a passage that connects two continents; etc.)."
            case 68:
                goaltivation = "The NPC wants to dominate or control another person or group."
            case 69:
                goaltivation = "The NPC wants to finish someone else's unfinished work."
            case 70:
                goaltivation = "The NPC wants to avenge a slain or defeated ally."
            case 71:
                goaltivation = "The NPC wants to unbalance an ongoing stalemate."
            case 72:
                goaltivation = "The NPC wants to surprise someone with a gift."
            case 73:
                goaltivation = "The NPC wants to play a prank on someone (harmful? or malicious?)."
            case 74:
                goaltivation = "The NPC wants to restore their home to its former glory (home could take the form of dwelling, town, country, etc.)."
            case 75:
                goaltivation = "The NPC wants to achieve divinity, enlightenment, or godhood."
            case 76:
                goaltivation = "The NPC wants to fulfill a prophesy they believe to be about themselves (but is it really?)."
            case 77:
                goaltivation = "The NPC wants to break someone out of prison."
            case 78:
                goaltivation = "The NPC wants to prove their innocence."
            case 79:
                goaltivation = "The NPC wants to be inspired or motivated by someone or something."
            case 80:
                goaltivation = "The NPC wants to do something that is 100% absolutely impossible to do."
            case 81:
                goaltivation = "The NPC wants to win a bet."
            case 82:
                goaltivation = "The NPC wants to cheat at a competition or clash."
            case 83:
                goaltivation = "The NPC wants to bind an entity to their power (a demon lord bound by runes; a rival merchant bound by contract; etc.)."
            case 84:
                goaltivation = "The NPC wants to learn a new language -- maybe even one that isn't spoken anymore."
            case 85:
                goaltivation = "The NPC wants to catch an elusive quarry (a burglar that leaves no trace; a massive mythical fish; etc.)."
            case 86:
                goaltivation = "The NPC wants to keep their family or organization from splitting up due to infighting."
            case 87:
                goaltivation = "The NPC wants to overcome an addiction."
            case 88:
                goaltivation = "The NPC wants to be left alone to engage in self-destructive acts (excessive drinking, gambling, etc.)."
            case 89:
                goaltivation = "The NPC wants to follow the route or path of someone who came before them (a prior expedition; a pilgrim following a messiah's path to the holy city; etc.)."
            case 90:
                goaltivation = "The NPC wants to teach their skills or methods to others."
            case 91:
                goaltivation = "The NPC wants to be remembered."
            case 92:
                goaltivation = "The NPC wants to build something (a house, a castle, a colony, etc.)."
            case 93:
                goaltivation = "The NPC wants to show support for a cause or person."
            case 94:
                goaltivation = "The NPC wants to understand a confusing person or culture."
            case 95:
                goaltivation = "The NPC wants to serve a lord, leader, or god."
            case 96:
                goaltivation = "The NPC wants to decide between two or more choices."
            case 97:
                goaltivation = "The NPC wants to harass or intimidate another person or group."
            case 98:
                goaltivation = "The NPC wants to honor or pay homage to someone they respect who has fallen or died."
            case 99:
                goaltivation = "The NPC wants to condition a person or group to respond in a certain way to certain stimuli."
            case 100:
                goaltivation = "The NPC wants to separate two things (opposing relics; feuding brothers; warring tribes; etc.)."
            case 101:
                goaltivation = "Gold. This PC is desperate to earn coin. He's a good guy who's made some bad choices lately and is willing to work to earn it."
            case 102:
                goaltivation = "Gold. This PC is a shrewd business person, who never gets the short end of a negotiation. They can get you rare items but the price is exorbitant."
            case 103:
                goaltivation = "Food: this NPC is a gourmet, always searching for the best cheese, the best wine... Compatible with the money motivation"
            case 104:
                goaltivation = "Heroism: this NPC believes they are a hero, and that the actions they takes are for the world. As the hero, anything they does can only be the right thing to do. Strong narcisism, and an ability to find a \"good\" explanation to anything they does or says."
            case 105:
                goaltivation = "Agoraphobia: this NPC only desires to be left alone, to find a place where nobody will bother him or try to become close to him. Could become violent if approached the wrong way, or try to help if it makes the heroes go away quicker"
            case 106:
                goaltivation = "Altruism: this character strives to help the others, especially the weak. Taking care of an orphanage, providing charity..."
            case 107:
                goaltivation = "Love: they have been alone in the wilderness for a long time, but returned to civilization in search of companionship."
            case 108:
                goaltivation = "Love: since they announced their chosen profession, their father has been distant sand, at times, cruel. They want to prove their worth to earn their trust."
            case 109:
                goaltivation = "Something lost: the family's prized antique sword had only sentimental value - but it is a matter of honor to retrieve it."
            case 110:
                goaltivation = "Something lost: their child left to play in the woods and didn't come back. Still, they know in their heart that the child is out there somewhere, alive, waiting for them."
            case 111:
                goaltivation = "Something lost: their former lover left town but promised to write every week. For the past month, there have been no letters. Something is wrong."
            case 112:
                goaltivation = "Safety: some strange fungus has been growing on their back, and they are desperately searching for a cure while also trying to keep it a secret"
            case 113:
                goaltivation = "Passion: the NPC is vigorously and even violently in favor of a cause and believes the PC to be so as well."
            case 114:
                goaltivation = "Research: their study involves a creature or place the party has seen or is going. they trades information but drills the party on the specific details of their experience"
            case 115:
                goaltivation = "Reputation: As a merchant with a reputation for quality goods, they puts this at the top of their priority list. they refuses to trade in low quality goods of any kind."
            case 116:
                goaltivation = "Paranoia: this person did something bad and is worried someone will find out."
            case 117:
                goaltivation = "Paranoia: this person wronged a powerful nobleman and now assumes everyone is an assassin."
            case 118:
                goaltivation = "Thrill. there is no challenge that this person won't accept, whether that be wrestling a bear, climbing to the peak of the bell tower, or testing an unknown potion's effects."
            case 119:
                goaltivation = "Security. this person has crates of salted pork, barrels of wheat grain, a cold cellar stacked with sacks of root vegetables, and enough firewood split and seasoned to last through the harshest and longest winter."
            case 120:
                goaltivation = "Security. this merchant keeps all their wares under lock and key. Not only that, they sell some of the finest locks in the kingdom; most require two different keys and are designed to 'break' stuck shut when attempted to be picked."
            case 121:
                goaltivation = "Security. Financial. This person has immense wealth hidden away and is extremely frugal, usually attempting to barter down even a few coppers off the price of any purchase. \"A copper saved is a copper earned!\""
            case 122:
                goaltivation = "Sickness: this character suffers from a mysterious/rare/legendary sickness, which they are trying to cure."
            case 123:
                goaltivation = "Contagious: the character suffers from a curse/mutation which can be give to others. Unable to bear this alone, they wants to give it to others and forge their own community."
            case 124:
                goaltivation = "Immortality: this characters suffers from being an Immortal, due to fate/curse/luck/joke of the gods. they wishes to find a way to die, which might or might not be known to him."
            case 125:
                goaltivation = "Collector: this eccentric - and generally rich - NPC cannot bear the idea of it's collection lacking a piece. Good choice for fetching plants/animals quests in far areas or stealing rare artifacts."
            case 126:
                goaltivation = "Collector: (Vanity) seeks rare items, not as part of a set, but just to have because no one else does."
            case 127:
                goaltivation = "(un)holy zealotry: This person believes what they are doing is a mission gifted to them by their god or patron (in the case of warlocks) despite potential evidence to the contrary."
            case 128:
                goaltivation = "(un)holy purpose: This person DID have a purpose given to them by their god/patron and are fullfilling it out of loyalty"
            case 129:
                goaltivation = "Fear: This person is terrified of someone. That someone has given them a task. The NPC will try their best to fulfill the task so they don't get punished."
            case 130:
                goaltivation = "Wanderlust: This person just wants to travel, see the world, meet new people, and experience new things."
            case 131:
                goaltivation = "Serve a Purpose: This person just wants to be a part of something greater than themselves. Purpose may involve (church, king, rebellion, state, the greater good, unifying the country, freeing the people, etc)"
            case 132:
                goaltivation = "Needs Writing Material: This person is trying to write a book or play. They have run out of ideas, so they seek new ideas where ever they can find them."
            case 133:
                goaltivation = "Redemption: This person has done things, bad things, in their past. They seek to correct the mistakes of their past. If they can not right the wrongs of their past, they seek to help others."
            case 134:
                goaltivation = "Insanity: Motivations change like minute to minute with no rhyme or reason."
            case 135:
                goaltivation = "Insanity: This person is desperately trying to ignore the voices in their head."
            case 136:
                goaltivation = "Monster: This person has a strong desire to do Bad Things. They have chosen to limit their victims to bad people."
            case 137:
                goaltivation = "Revolutionary: Desire to change the (government, guild, nation, system, world)"
            case 138:
                goaltivation = "Generosity. This person grew up dirt-poor, and so now they share their modest wealth with those who need it most."
            case 139:
                goaltivation = "Generosity. This person grew up as a laborer, back-breaking work in the fields, and so now they spread their substantial wealth among the working class, offering above average wages and respectful working conditions."
            case 140:
                goaltivation = "Generosity. This person grew up ridiculously wealthy and only recently learned that there are people who are poor. They have decided to be extremely philanthropic, giving money to whomever asks, though they do work up written contracts with the recipient to assure that the money goes to good use."
            case 141:
                goaltivation = "Gluttony. This person grew up hungry, and now fears ever going without food again. They'll eat as much as is offered and ask for seconds. As such, they are well able to identify various rare ingredients by smell and taste, and are highly sought after by the Aristocracy to be food-taster."
            case 142:
                goaltivation = "Buried their mother under a sapling in a distant grove long ago, and has recently learned from a long-forgotten diary that they had swallowed a fine string of pearls before passing, either out of spite or to pay for their passage to the afterlife. A recent string of financial setbacks means this NPCs needs that money now, and BAD. Oh and the sapling is likely now fully grown and thus impossible to single out from all the others around it."
            case 143:
                goaltivation = "This NPC hasn't slept well in weeks, and swears that somebody's always watching him. Desperate consultations with mystics and seers have failed to identify the cause, and it's driving him crazy. Nobody thinks much of it, until one of the party members notices a second set of tracks trailing after the NPC on a nearby beach."
            case 144:
                goaltivation = "On a drunken night out long ago, was given a mug of something by a beautiful girl in a tavern similar to, but not quite like, the ones in the village. The drink was the best thing this NPC has ever had, and they would kill for another drop. But subsequent nights so far have yielded little other than massive hangovers."
            case 145:
                goaltivation = "Desperate to prevent their sister from marrying into a household that this NPC is certain are vampires. The Rembils never leave their abode without heavy layers of clothes, and rarely, if ever eat in public. they could be right, or it could be that the whole family suffers from a genetic, and very painful skin condition instead."
            case 146:
                goaltivation = "Wants to leave the city and start a new life as a priest/shepherd/bounty hunter but is bound by an old oath to care for their late wife's grandmother until their death. But the old crone is ungrateful, arrogant and mean, and in no hurry to die at 93. Maybe she's just lucky, or maybe this is the cause of a demonic pact."
            case 147:
                goaltivation = "Found an old rusty key on a moonlit walk a fortnight ago. Since then, this NPC has been plagued by dreams of locked doors, long hallways leading to dead ends, and things with keyholes for eyes. Believes that finding what the key unlocks will relieve him, and fears losing the key more than anything."
            case 148:
                goaltivation = "Was fed an odd, pungent medicine once a month since they was a child by their mother, but they recently passed away without revealing the recipe to him, or what it did. Now the end of the month approaches, and this NPC is growing restless and worried."
            case 149:
                goaltivation = "This NPC prides himself on being able to eat anything served at a pub or tavern that their proprietors label as “food”. He's recently heard of an incredibly spicy delicacy eaten only by a sect of fire-breathers in a faraway land, and wants more than anything to try it."
            case 150:
                goaltivation = "This NPC inherited a scroll with strange runes on it from a barely-familiar distant relative. they are incredibly possessive and refuses to let anyone read it, lest they “use up it's magic”, but is unable to read it himself. It could be a spell, or it could be a spiteful prank by the dead relative."
            case 151:
                goaltivation = "An NPC was raised by an only mother without ever knowing their father. they thought that their late mother calling their father “the wind” was a poetic figure of speech, but he's recently found that they can hear whispers carried past him on the breeze."
            case 152:
                goaltivation = "Wishes to become a travelling violinist, going from city to city and spreading tales of adventure, mirth and tragedy among the people. Only problem is, they had their fingers bitten off by a Greelik, a minor demon of pranks, as a kid, and will need to summon him to get them back."
            case 153:
                goaltivation = "This NPC always thought they was an only child, until their parents passed in an accident, and they found a charcoal painting among their possessions. It depicted their parents as young adults, as well as himself, and another, very similar child, as babies."
            case 154:
                goaltivation = "Once bought a crate of “Moonlight Blue Wine” from a seasonal travelling salesman, and though it tasted terrible at first, has become obsessed with it. Now he's down to two bottles, and the salesman has missed their usual appearance at this season's town festival."
            case 155:
                goaltivation = "This NPC swallowed a compass as a child, and since then, has an impossibly accurate sense for directions. Recently though, he's started to get a tugging feeling that indicates the location of the nearest still-birth, and it's creeping him out enough that they wants to get the compass out."
            case 156:
                goaltivation = "An unmarried NPC has prayed for years for a child to be given to him by the gods, and had their prayers go unanswered. Until last week, when they triumphantly presented a small boy of 4 or 5 years to their neighbors. Interestingly, nobody understands the boy's speech, and they has only four fingers on each hand."
            case 157:
                goaltivation = "This NPC has corresponded for years with a penpal from the neighboring village (over the mountains, or through a dangerous forest) but their friend has recently stopped responding to letters."
            case 158:
                goaltivation = "Recently visited their ancestral home and found that their family had been killed by a madman. Vowing to stop at nothing to get their revenge, the fact that the madman had been executed by the local sheriff is, to him, a mere inconvenience."
            case 159:
                goaltivation = "Having lived their entire life in a landlocked city, this NPC has always felt the wide-open beauty of the sea calling to him. But because of nearly being drowned in a washbasin by an inattentive mother/sister/nanny as a child, has a deathly fear of drowning. Memory-altering magic may prove useful."
            case 160:
                goaltivation = "This NPC has raised horses for years, and for years has tried to train their horses to talk to him. Recently, he's been going around town claiming to have succeeded with a new mare, and though their horse has surprisingly intelligent, almost human eyes, nobody else has ever heard it say a word."
            case 161:
                goaltivation = "This hunter has hunted for years in the local woods, straying farther and farther from the known areas in search of ever bigger game. Recently, he's claimed to have seen a glorious golden stag, and is convinced it is their life's goal to hunt down the creature."
            case 162:
                goaltivation = "To retrieve a stolen relic from a faraway land."
            case 163:
                goaltivation = "To kill their possessed parent."
            case 164:
                goaltivation = "To retrieve their sibling's soul."
            case 165:
                goaltivation = "To buy back the family farm."
            case 166:
                goaltivation = "To become nobility."
            case 167:
                goaltivation = "To spread their faith to distant lands."
            case 168:
                goaltivation = "To buy a rival's farm."
            case 169:
                goaltivation = "To find their lost weapon."
            case 170:
                goaltivation = "To buy a rival's business."
            case 171:
                goaltivation = "To recover their teacher's instrument."
            case 172:
                goaltivation = "To complete their research."
            case 173:
                goaltivation = "To buy an inn."
            case 174:
                goaltivation = "To reunite their old squad."
            case 175:
                goaltivation = "To take their rightful place amongst the devils."
            case 176:
                goaltivation = "To rebuild their family's ancestral home."
            case 177:
                goaltivation = "To buy back their family's land."
            case 178:
                goaltivation = "To thwart their destiny."
            case 179:
                goaltivation = "To start their own mercenary group."
            case 180:
                goaltivation = "To find and use an ancient artifact."
            case 181:
                goaltivation = "To kill a demon."
            case 182:
                goaltivation = "To hunt down the person that killed their family."
            case 183:
                goaltivation = "To ruin a rival's business."
            case 184:
                goaltivation = "To build a temple dedicated to their god."
            case 185:
                goaltivation = "To sample every kind of mead in the world."
            case 186:
                goaltivation = "To return a stolen item to a king in a faraway land."
            case 187:
                goaltivation = "To reclaim the lands of their clan."
            case 188:
                goaltivation = "To start their own trade caravan."
            case 189:
                goaltivation = "To hunt down their mutinous crew."
            case 190:
                goaltivation = "To restore their family's honor."
            case 191:
                goaltivation = "To bring their lost love back from the dead."
            case 192:
                goaltivation = "To avenge their fallen comrades."
            case 193:
                goaltivation = "To break their family curse."
            case 194:
                goaltivation = "To find their real family."
            case 195:
                goaltivation = "To captain their own ship."
            case 196:
                goaltivation = "To find their long lost sibling."
            case 197:
                goaltivation = "To prove they deserve their parents' love."
            case 198:
                goaltivation = "To find a lost city."
            case 199:
                goaltivation = "To steal their soul back."
            case 200:
                goaltivation = "To find a lost relic of their temple."

    # Persist generated values into session_state for rendering after rerun
    st.session_state.name = name
    st.session_state.classification = classification
    st.session_state.ancestry = ancestry
    st.session_state.dndclass = dndclass
    st.session_state.level = level
    st.session_state.gender = gender
    st.session_state.disposition = disposition
    st.session_state.alignment = alignment
    st.session_state.goaltivation = goaltivation
    # st.session_state.classification_roll = classification_roll
    # st.session_state.ancestry_roll = ancestry_roll
    # st.session_state.class_roll = class_roll
    # st.session_state.gender_roll = gender_roll
    # st.session_state.disposition_roll = disposition_roll
    # st.session_state.alignment_roll = alignment_roll
    st.session_state.No_HOF = No_HOF
    st.session_state.generated = True

## Title Section

st.markdown("<h1 style='text-align: center;'>Alyrian NPC Generator</h1>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: left;'>Generate unique non-player characters (NPCs) with Alyraian Homebrew.</h6>", unsafe_allow_html=True)
st.write("")
st.markdown("---", unsafe_allow_html=True)

## Options Section
st.markdown("<h4 style='text-align: center;'>Generation Options</h4>", unsafe_allow_html=True) 

Gen_Options_1 = row(5, vertical_align="center", gap="small")
direct_edit = Gen_Options_1.checkbox("Directly Edit NPC?", value=False)
Gen_Options_1.checkbox("Accurate Classification Distribution?", value=True, key="accurate_distributions")
Gen_Options_1.checkbox("Player Classes Only?", value=True, key="player_classes_only")

if direct_edit: # Direct Editor
    st.markdown("---")
    st.markdown("<h4 style='text-align: center;'>Direct Options</h4>", unsafe_allow_html=True)
    Edit_Options_1 = row(5, vertical_align="center", gap="small")
    name = Edit_Options_1.text_input("Name", placeholder="Enter NPC Name")
    classification = Edit_Options_1.selectbox("Classification", options=["Naturalborn", "Oddity", "Outlander"], index=None)
    
    if classification == "Naturalborn":
        ancestryoptions = [
            "Aasimar",
            "Dragonborn (Chromatic)",
            "Dragonborn (Metallic)",
            "Dwarf (Gray) [Duergar]",
            "Dwarf (Hill)",
            "Dwarf (Mountain)",
            "Dwarf (Seaborn)",
            "Dwarf (Strongblood)",
            "Elf (Ash)",
            "Elf (Dark) [Drow]",
            "Elf (High)",
            "Elf (Sea)",
            "Elf (Wood)",
            "Faunus (Bear)",
            "Faunus (Bird)",
            "Faunus (Cat)",
            "Faunus (Cow/Bull)",
            "Faunus (Deer)",
            "Faunus (Dog)",
            "Faunus (Fox)",
            "Faunus (Horse)",
            "Faunus (Pig)",
            "Faunus (Rabbit)",
            "Faunus (Raccoon)",
            "Faunus (Sheep/Goat)",
            "Faunus (Wolf)",
            "Gnome (Deep)",
            "Gnome (Forest)",
            "Gnome (Rock)",
            "Goblin",
            "Goblin (Hoardshine)",
            "Goliath",
            "Goliath (Cloudborn)",
            "Goliath (Fireborn)",
            "Goliath (Frostborn)",
            "Goliath (Hillborn)",
            "Goliath (Stoneborn)",
            "Half-Elf",
            "Half-Orc",
            "Half-Orc (Coldheart)",
            "Halfling (Lightfoot)",
            "Halfling (Lotusden)",
            "Halfling (Stout)",
            "Human",
            "Kobold",
            "Leonin",
            "Orc",
            "Tabaxi",
            "Tabaxi (Softpaw)",
            "Tiefling",
            "Tortle"
        ]
    elif classification == "Oddity":
        ancestryoptions = [
            "Aarakocra",
            "Aasimar (Mystic)",
            "Dragonborn (Gem)",
            "Dragonborn (Radiant)",
            "Elf (Pallid)",
            "Halfling (Jinx)",
            "Kalashtar",
            "Kenku",
            "Kenku (Harrowfeather)",
            "Kenku (Shroudeye)",
            "Lineage (Dhamphir)",
            "Lineage (Disembodied)",
            "Lineage (Hexblood)",
            "Lineage (Reborn)",
            "Lupin (Fabled)",
            "Lupin (Isolated)",
            "Lupin (Leader)",
            "Lupin (Pack)",
            "Lustrous (Ore)",
            "Lustrous (Precious)",
            "Lustrous (Semi-Precious)",
            "Macawkra",
            "Nymph (Alseid)",
            "Nymph (Asteria)",
            "Nymph (Aurae)",
            "Nymph (Dryad)",
            "Nymph (Lampad)",
            "Nymph (Naiad)",
            "Nymph (Oread)",
            "Owlin",
            "Rakin (Posskin)",
            "Rakin (Tanukin)",
            "Rakin (Urkin)",
            "Ratfolk (Packrat)",
            "Ratfolk (Ratical)",
            "Ratfolk (Scourgerat)",
            "Tengu",
            "Tiefling (Amethyst Bloodline)",
            "Tiefling (Gold Bloodline)",
            "Warforged"
        ]
    elif classification == "Outlander": 
        ancestryoptions = [
            "Aasimar (Cosmic)",
            "Aasimar (Elfriche)",
            "Changeling",
            "Dragonborn (Faerie)",
            "Dragonborn (Moonstone)",
            "Elf (Eladrin)",
            "Elf (Shadar-Kai)",
            "Elf (Snow)",
            "Firbolg",
            "Genasi (Air)",
            "Genasi (Earth)",
            "Genasi (Fire)",
            "Genasi (Water)",
            "Lunarran (Bloodmoon)",
            "Lunarran (Bluemoon)",
            "Lunarran (Crescent)",
            "Lunarran (Waning)",
            "Metallus (Alloy)",
            "Metallus (Gold)",
            "Opteran (Cityborn)",
            "Opteran (Naturalborn)",
            "Tlakah (High Senye)",
            "Tlakah (Low Senye)",
            "Tlakah (Mid Senye)"
        ]
    elif ancestry == "Choose Classification First.":
        disallow_generation = True
    
    ancestry = Edit_Options_1.selectbox("Ancestry", options=ancestryoptions, index=None)
    dndclass = Edit_Options_1.selectbox("Class", options=["Commoner", "Alchemist", "Artificer", "Blacksmith", "Brewer", "Carpenter", "Cobbler", "Cook", "Enchanter", "Engineer", "Jeweler", "Leatherworker", "Mason", "Painter", "Poisoner", "Scroll Scriber", "Tailor", "Tinkerer", "Wand Whittler", "Weaver", "Wood Carver", "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"], index=None)
    
    if dndclass != None:
        level = Edit_Options_1.number_input(label ="Choose a Level.",min_value=0, max_value=20, value=0)
        No_HOF = True
    else:
        No_HOF = False
    
    Edit_Options_2 = row(5, vertical_align="center", gap="small")
    gender = Edit_Options_2.selectbox("Gender", options=["Male", "Female", "Non-Binary", "Effeminate Male", "Masculine Female", "Gender Nonconforming"], index=None)
    disposition = Edit_Options_2.selectbox("Disposition", options=["Hostile", "Friendly", "Indifferent"], index=None)
    alignment = Edit_Options_2.selectbox("Alignment", options=["Lawful Good", "Lawful Unaligned", "Lawful Evil", "Neutral Good", "Neutral Unaligned", "Neutral Evil", "Chaotic Good", "Chaotic Unaligned", "Chaotic Evil"], index=None)

    goaltivation_options = [
    "The NPC wants to return to their homeland or place of origin.",
    "The NPC wants to escape their current situation.",
    "The NPC wants to obtain romantic love.",
    "The NPC wants to obtain fame and adoration.",
    "The NPC wants to atone for a past crime.",
    "The NPC wants to find a lost relative or friend.",
    "The NPC wants to obtain a particular item (a gemstone to make into a wedding ring; a magical sword; a book of secret spells; etc.).",
    "The NPC wants to be the first at something (first to discover a rumored land; first to break a record; etc).",
    "The NPC wants revenge on a rival or hated foe.",
    "The NPC wants to build and expand a business.",
    "The NPC wants to found a religion.",
    "The NPC wants to found a secular organization or brotherhood.",
    "The NPC wants to find a cure for a disease, curse, or ailment.",
    "The NPC wants to write or create a masterpiece book, song, or piece of art.",
    "The NPC wants to complete or add to a collection.",
    "The NPC wants to free an enslaved people.",
    "The NPC wants to make a lot of money.",
    "The NPC wants to sabotage a rival group or organization.",
    "The NPC wants to establish peace between rival/warring factions or governments.",
    "The NPC wants a family.",
    "The NPC just wants someone to take over for a while so they can rest.",
    "The NPC wants to fix a broken but necessary piece of equipment, machinery, or other apparatus.",
    "The NPC wants to prove that they have surpassed their old master.",
    "The NPC wants to learn more about a relative who died or vanished before they were born.",
    "The NPC wants to learn a new skill or trade.",
    "The NPC wants to end their own life or existence (this goal may not be appropriate for all groups; talk to your players first and reroll if necessary).",
    "The NPC wants to see a fantastical creature in person (a unicorn, a dragon, etc.).",
    "The NPC wants to spread their religion to the uninitiated (possibly even by force).",
    "The NPC wants to avoid a prophesied outcome.",
    "The NPC wants to have children (or some other heir to carry on their legacy).",
    "The NPC wants to make a new friend.",
    "The NPC wants to shirk their duties and responsibilities.",
    "The NPC wants to break up a relationship or drive a wedge between two people (not necessarily a romantic relationship).",
    "The NPC wants relief from a chronic malady, wound, or illness that they suffer from.",
    "The NPC wants to make their family (or a respected mentor) proud.",
    "The NPC wants to regain something that was lost (wealth, fame, an item, the family property).",
    "The NPC wants to put a stop to criminal activity.",
    "The NPC wants to mend a rift between two people (reunite with an estranged father; help two rival blacksmiths work together; etc.).",
    "The NPC wants to solve an ongoing mystery.",
    "The NPC wants to protect a friend or family member from something.",
    "The NPC wants to reinvent themselves as a new identity.",
    "The NPC wants to foster trade between two groups (tribes, countries, cities, etc.)",
    "The NPC wants to reestablish a forgotten holiday or cultural custom.",
    "The NPC wants to make people laugh.",
    "The NPC wants to prove their power.",
    "The NPC wants to prove a theory.",
    "The NPC wants to destroy a rival or hated foe.",
    "The NPC wants their kingdom or country to expand.",
    "The NPC wants to prove a rumor about them is wrong.",
    "The NPC wants to win a game or competition.",
    "The NPC wants to travel to a thus-far unreachable place (space; time travel; a different dimension; etc.).",
    "The NPC wants to prove something they believe in exists.",
    "The NPC wants to destroy or kill a class of people or creatures.",
    "The NPC wants to preserve nature at all costs.",
    "The NPC wants to decipher a puzzle or something written in a code or ancient language.",
    "The NPC wants to repay a debt (not necessarily financial in nature).",
    "The NPC wants to join an elite group or organization.",
    "The NPC wants to stay anonymous and not be noticed.",
    "The NPC wants to change a law or local custom.",
    "The NPC wants to overcome their fear of something.",
    "The NPC wants to be more beautiful or attractive.",
    "The NPC wants to redeem a villain.",
    "The NPC wants to break a bad habit.",
    "The NPC wants to remedy something about their personality (an inability to trust people; an explosive temper; always refusing to admit when they're wrong; etc.)",
    "The NPC wants to profess their love to someone they admire.",
    "The NPC wants to be taken seriously by someone who doesn't give them due credit.",
    "The NPC wants to fix an inaccuracy in the culture's accepted knowledge (prove that the world isn't flat; that there is a passage that connects two continents; etc.).",
    "The NPC wants to dominate or control another person or group.",
    "The NPC wants to finish someone else's unfinished work.",
    "The NPC wants to avenge a slain or defeated ally.",
    "The NPC wants to unbalance an ongoing stalemate.",
    "The NPC wants to surprise someone with a gift.",
    "The NPC wants to play a prank on someone (harmful? or malicious?).",
    "The NPC wants to restore their home to its former glory (home could take the form of dwelling, town, country, etc.).",
    "The NPC wants to achieve divinity, enlightenment, or godhood.",
    "The NPC wants to fulfill a prophesy they believe to be about themselves (but is it really?).",
    "The NPC wants to break someone out of prison.",
    "The NPC wants to prove their innocence.",
    "The NPC wants to be inspired or motivated by someone or something.",
    "The NPC wants to do something that is 100% absolutely impossible to do.",
    "The NPC wants to win a bet.",
    "The NPC wants to cheat at a competition or clash.",
    "The NPC wants to bind an entity to their power (a demon lord bound by runes; a rival merchant bound by contract; etc.).",
    "The NPC wants to learn a new language -- maybe even one that isn't spoken anymore.",
    "The NPC wants to catch an elusive quarry (a burglar that leaves no trace; a massive mythical fish; etc.).",
    "The NPC wants to keep their family or organization from splitting up due to infighting.",
    "The NPC wants to overcome an addiction.",
    "The NPC wants to be left alone to engage in self-destructive acts (excessive drinking, gambling, etc.).",
    "The NPC wants to follow the route or path of someone who came before them (a prior expedition; a pilgrim following a messiah's path to the holy city; etc.).",
    "The NPC wants to teach their skills or methods to others.",
    "The NPC wants to be remembered.",
    "The NPC wants to build something (a house, a castle, a colony, etc.).",
    "The NPC wants to show support for a cause or person.",
    "The NPC wants to understand a confusing person or culture.",
    "The NPC wants to serve a lord, leader, or god.",
    "The NPC wants to decide between two or more choices.",
    "The NPC wants to harass or intimidate another person or group.",
    "The NPC wants to honor or pay homage to someone they respect who has fallen or died.",
    "The NPC wants to condition a person or group to respond in a certain way to certain stimuli.",
    "The NPC wants to separate two things (opposing relics; feuding brothers; warring tribes; etc.).",
    "Gold. This PC is desperate to earn coin. He's a good guy who's made some bad choices lately and is willing to work to earn it.",
    "Gold. This PC is a shrewd business person, who never gets the short end of a negotiation. They can get you rare items but the price is exorbitant.",
    "Food: this NPC is a gourmet, always searching for the best cheese, the best wine... Compatible with the money motivation",
    "Heroism: this NPC believes they are a hero, and that the actions they takes are for the world. As the hero, anything they does can only be the right thing to do. Strong narcisism, and an ability to find a \"good\" explanation to anything they does or says.",
    "Agoraphobia: this NPC only desires to be left alone, to find a place where nobody will bother him or try to become close to him. Could become violent if approached the wrong way, or try to help if it makes the heroes go away quicker",
    "Altruism: this character strives to help the others, especially the weak. Taking care of an orphanage, providing charity...",
    "Love: they have been alone in the wilderness for a long time, but returned to civilization in search of companionship.",
    "Love: since they announced their chosen profession, their father has been distant sand, at times, cruel. They want to prove their worth to earn their trust.",
    "Something lost: the family's prized antique sword had only sentimental value - but it is a matter of honor to retrieve it.",
    "Something lost: their child left to play in the woods and didn't come back. Still, they know in their heart that the child is out there somewhere, alive, waiting for them.",
    "Something lost: their former lover left town but promised to write every week. For the past month, there have been no letters. Something is wrong.",
    "Safety: some strange fungus has been growing on their back, and they are desperately searching for a cure while also trying to keep it a secret",
    "Passion: the NPC is vigorously and even violently in favor of a cause and believes the PC to be so as well.",
    "Research: their study involves a creature or place the party has seen or is going. they trades information but drills the party on the specific details of their experience",
    "Reputation: As a merchant with a reputation for quality goods, they puts this at the top of their priority list. they refuses to trade in low quality goods of any kind.",
    "Paranoia: this person did something bad and is worried someone will find out.",
    "Paranoia: this person wronged a powerful nobleman and now assumes everyone is an assassin.",
    "Thrill. there is no challenge that this person won't accept, whether that be wrestling a bear, climbing to the peak of the bell tower, or testing an unknown potion's effects.",
    "Security. this person has crates of salted pork, barrels of wheat grain, a cold cellar stacked with sacks of root vegetables, and enough firewood split and seasoned to last through the harshest and longest winter.",
    "Security. this merchant keeps all their wares under lock and key. Not only that, they sell some of the finest locks in the kingdom; most require two different keys and are designed to 'break' stuck shut when attempted to be picked.",
    "Security. Financial. This person has immense wealth hidden away and is extremely frugal, usually attempting to barter down even a few coppers off the price of any purchase. \"A copper saved is a copper earned!\"",
    "Sickness: this character suffers from a mysterious/rare/legendary sickness, which they are trying to cure.",
    "Contagious: the character suffers from a curse/mutation which can be give to others. Unable to bear this alone, they wants to give it to others and forge their own community.",
    "Immortality: this characters suffers from being an Immortal, due to fate/curse/luck/joke of the gods. they wishes to find a way to die, which might or might not be known to him.",
    "Collector: this eccentric - and generally rich - NPC cannot bear the idea of it's collection lacking a piece. Good choice for fetching plants/animals quests in far areas or stealing rare artifacts.",
    "Collector: (Vanity) seeks rare items, not as part of a set, but just to have because no one else does.",
    "(un)holy zealotry: This person believes what they are doing is a mission gifted to them by their god or patron (in the case of warlocks) despite potential evidence to the contrary.",
    "(un)holy purpose: This person DID have a purpose given to them by their god/patron and are fullfilling it out of loyalty",
    "Fear: This person is terrified of someone. That someone has given them a task. The NPC will try their best to fulfill the task so they don't get punished.",
    "Wanderlust: This person just wants to travel, see the world, meet new people, and experience new things.",
    "Serve a Purpose: This person just wants to be a part of something greater than themselves. Purpose may involve (church, king, rebellion, state, the greater good, unifying the country, freeing the people, etc)",
    "Needs Writing Material: This person is trying to write a book or play. They have run out of ideas, so they seek new ideas where ever they can find them.",
    "Redemption: This person has done things, bad things, in their past. They seek to correct the mistakes of their past. If they can not right the wrongs of their past, they seek to help others.",
    "Insanity: Motivations change like minute to minute with no rhyme or reason.",
    "Insanity: This person is desperately trying to ignore the voices in their head.",
    "Monster: This person has a strong desire to do Bad Things. They have chosen to limit their victims to bad people.",
    "Revolutionary: Desire to change the (government, guild, nation, system, world)",
    "Generosity. This person grew up dirt-poor, and so now they share their modest wealth with those who need it most.",
    "Generosity. This person grew up as a laborer, back-breaking work in the fields, and so now they spread their substantial wealth among the working class, offering above average wages and respectful working conditions.",
    "Generosity. This person grew up ridiculously wealthy and only recently learned that there are people who are poor. They have decided to be extremely philanthropic, giving money to whomever asks, though they do work up written contracts with the recipient to assure that the money goes to good use.",
    "Gluttony. This person grew up hungry, and now fears ever going without food again. They'll eat as much as is offered and ask for seconds. As such, they are well able to identify various rare ingredients by smell and taste, and are highly sought after by the Aristocracy to be food-taster.",
    "Buried their mother under a sapling in a distant grove long ago, and has recently learned from a long-forgotten diary that they had swallowed a fine string of pearls before passing, either out of spite or to pay for their passage to the afterlife. A recent string of financial setbacks means this NPCs needs that money now, and BAD. Oh and the sapling is likely now fully grown and thus impossible to single out from all the others around it.",
    "This NPC hasn't slept well in weeks, and swears that somebody's always watching him. Desperate consultations with mystics and seers have failed to identify the cause, and it's driving him crazy. Nobody thinks much of it, until one of the party members notices a second set of tracks trailing after the NPC on a nearby beach.",
    "On a drunken night out long ago, was given a mug of something by a beautiful girl in a tavern similar to, but not quite like, the ones in the village. The drink was the best thing this NPC has ever had, and they would kill for another drop. But subsequent nights so far have yielded little other than massive hangovers.",
    "Desperate to prevent their sister from marrying into a household that this NPC is certain are vampires. The Rembils never leave their abode without heavy layers of clothes, and rarely, if ever eat in public. they could be right, or it could be that the whole family suffers from a genetic, and very painful skin condition instead.",
    "Wants to leave the city and start a new life as a priest/shepherd/bounty hunter but is bound by an old oath to care for their late wife's grandmother until their death. But the old crone is ungrateful, arrogant and mean, and is no hurry to die at 93. Maybe she's just lucky, or maybe this is the cause of a demonic pact.",
    "Found an old rusty key on a moonlit walk a fortnight ago. Since then, this NPC has been plagued by dreams of locked doors, long hallways leading to dead ends, and things with keyholes for eyes. Believes that finding what the key unlocks will relieve him, and fears losing the key more than anything.",
    "Was fed an odd, pungent medicine once a month since they was a child by their mother, but they recently passed away without revealing the recipe to him, or what it did. Now the end of the month approaches, and this NPC is growing restless and worried.",
    "This NPC prides himself on being able to eat anything served at a pub or tavern that their proprietors label as 'food'. He's recently heard of an incredibly spicy delicacy eaten only by a sect of fire-breathers in a faraway land, and wants more than anything to try it.",
    "This NPC inherited a scroll with strange runes on it from a barely-familiar distant relative. they are incredibly possessive and refuses to let anyone read it, lest they 'use up it's magic', but is unable to read it himself. It could be a spell, or it could be a spiteful prank by the dead relative.",
    "An NPC was raised by an only mother without ever knowing their father. they thought that their late mother calling their father 'the wind' was a poetic figure of speech, but he's recently found that they can hear whispers carried past him on the breeze.",
    "Wishes to become a travelling violinist, going from city to city and spreading tales of adventure, mirth and tragedy among the people. Only problem is, they had their fingers bitten off by a Greelik, a minor demon of pranks, as a kid, and will need to summon him to get them back.",
    "This NPC always thought they was an only child, until their parents passed in an accident, and they found a charcoal painting among their possessions. It depicted their parents as young adults, as well as himself, and another, very similar child, as babies.",
    "Once bought a crate of 'Moonlight Blue Wine' from a seasonal travelling salesman, and though it tasted terrible at first, has become obsessed with it. Now he's down to two bottles, and the salesman has missed their usual appearance at this season's town festival.",
    "This NPC swallowed a compass as a child, and since then, has an impossibly accurate sense for directions. Recently though, he's started to get a tugging feeling that indicates the location of the nearest still-birth, and it's creeping him out enough that they wants to get the compass out.",
    "An unmarried NPC has prayed for years for a child to be given to him by the gods, and had their prayers go unanswered. Until last week, when they triumphantly presented a small boy of 4 or 5 years to their neighbors. Interestingly, nobody understands the boy's speech, and they has only four fingers on each hand.",
    "This NPC has corresponded for years with a penpal from the neighboring village (over the mountains, or through a dangerous forest) but their friend has recently stopped responding to letters.",
    "Recently visited their ancestral home and found that their family had been killed by a madman. Vowing to stop at nothing to get their revenge, the fact that the madman had been executed by the local sheriff is, to him, a mere inconvenience.",
    "Having lived their entire life in a landlocked city, this NPC has always felt the wide-open beauty of the sea calling to him. But because of nearly being drowned in a washbasin by an inattentive mother/sister/nanny as a child, has a deathly fear of drowning. Memory-altering magic may prove useful.",
    "This NPC has raised horses for years, and for years has tried to train their horses to talk to him. Recently, he’s been going around town claiming to have succeeded with a new mare, and though their horse has surprisingly intelligent, almost human eyes, nobody else has ever heard it say a word.",
    "This hunter has hunted for years in the local woods, straying farther and farther from the known areas in search of ever bigger game. Recently, he’s claimed to have seen a glorious golden stag, and is convinced it is their life’s goal to hunt down the creature.",
    "To retrieve a stolen relic from a faraway land.",
    "To kill their possessed parent.",
    "To retrieve their sibling’s soul.",
    "To buy back the family farm.",
    "To become nobility.",
    "To spread their faith to distant lands.",
    "To buy a rival’s farm.",
    "To find their lost weapon.",
    "To buy a rival’s business.",
    "To recover their teacher’s instrument.",
    "To complete their research.",
    "To buy an inn.",
    "To reunite their old squad.",
    "To take their rightful place amongst the devils.",
    "To rebuild their family’s ancestral home.",
    "To buy back their family’s land.",
    "To thwart their destiny.",
    "To start their own mercenary group.",
    "To find and use an ancient artifact.",
    "To kill a demon.",
    "To hunt down the person that killed their family.",
    "To ruin a rival’s business.",
    "To build a temple dedicated to their god.",
    "To sample every kind of mead in the world.",
    "To return a stolen item to a king in a faraway land.",
    "To reclaim the lands of their clan.",
    "To start their own trade caravan.",
    "To hunt down their mutinous crew.",
    "To restore their family’s honor.",
    "To bring their lost love back from the dead.",
    "To avenge their fallen comrades.",
    "To break their family curse.",
    "To find their real family.",
    "To captain their own ship.",
    "To find their long lost sibling.",
    "To prove they deserve their parents’ love.",
    "To find a lost city.",
    "To steal their soul back.",
    "To find a lost relic of their temple."
    ]
    goaltivation = Edit_Options_2.selectbox("Goaltivation", options=goaltivation_options, index=None)

st.button("Generate NPC", type="primary", use_container_width=True, disabled=disallow_generation, on_click=generate_npc)

# Render the generated UI only when generation has happened (persisted in session_state)
if st.session_state.generated:
    # Output NPC Details (use session_state values)
    st.markdown("---", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>Generated NPC</h4>", unsafe_allow_html=True)

    # Censoring

    if pf.is_clean(name) and name != "":
        NPC_Output = f"Name: {st.session_state.name}\nClassification: {st.session_state.classification}\nAncestry: {st.session_state.ancestry}\nClass: {st.session_state.dndclass}\nLevel: {st.session_state.level}\nGender: {st.session_state.gender}\nDisposition: {st.session_state.disposition}\nAlignment: {st.session_state.alignment}\nGoaltivation: {st.session_state.goaltivation}"
        No_HOF = False
        st.code(NPC_Output, height="content")
    else:
        NPC_Output = f"Name: {st.session_state.ancestry} {st.session_state.dndclass} ({st.session_state.level})\nClassification: {st.session_state.classification}\nAncestry: {st.session_state.ancestry}\nClass: {st.session_state.dndclass}\nLevel: {st.session_state.level}\nGender: {st.session_state.gender}\nDisposition: {st.session_state.disposition}\nAlignment: {st.session_state.alignment}\nGoaltivation: {st.session_state.goaltivation}"
        st.code(NPC_Output, height="content")
        if pf.is_profane(name):
            No_HOF = True

    # Hall of Fame

    if st.session_state.level >= 1 and st.session_state.No_HOF != True: 
        st.markdown("<h6 style='text-align: center; color: #e3256b;'>High-Level NPC Generated!</h6>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: center; color: #e3256b;'>Consider adding them to the Hall of Fame below.</h6>", unsafe_allow_html=True)
        if st.button("Add to Hall of Fame", type="secondary", use_container_width=True, disabled=st.session_state.No_HOF):
            with open("NPC_Hall_of_Fame.txt", "a") as hof: # Maybe write as json instead, just for clarity in the future.
                hof.write(f"Name: {st.session_state.ancestry} {st.session_state.dndclass} ({st.session_state.level}), Classification: {st.session_state.classification}, Ancestry: {st.session_state.ancestry}, Class: {st.session_state.dndclass}, Level: {st.session_state.level}, Gender: {st.session_state.gender}, Disposition: {st.session_state.disposition}, Alignment: {st.session_state.alignment}, Goaltivation: {st.session_state.goaltivation}\n") 
            st.session_state.No_HOF = True
            st.rerun() # Makes the HOF button immediately disappear after being clicked.

st.markdown("---", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Hall of Fame</h4>", unsafe_allow_html=True)

# Show Hall of Fame contents as cards that you can cycle through
try:
    with open("NPC_Hall_of_Fame.txt", "r") as hof:
        hof_lines = hof.readlines()
        for line in hof_lines:
            hof_names = [l.split(",")[0].replace("Name: ","").strip() for l in hof_lines]
        if hof_lines:
            HOF_Row1 = row(7, vertical_align="center", gap="small")
            HOF_Row1.text("")
            HOF_Row1.text("")
            HOF_Row1.text("")
            index = HOF_Row1.selectbox("Select NPC to View", range(len(hof_lines)), format_func=lambda x: hof_names[x])
            HOF_Row1.text("")
            HOF_Row1.text("")
            HOF_Row1.text("")
            selected_npc = hof_lines[index].strip()
            st.markdown(f"<h3 style='text-align: center;'>{selected_npc}</h3>", unsafe_allow_html=True)
except FileNotFoundError:
    st.markdown("<h6 style='text-align: center;'>No NPCs in the Hall of Fame yet.</h6>", unsafe_allow_html=True)

        


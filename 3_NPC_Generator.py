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
#    "classification_roll": classification_roll,
    "ancestry": ancestry,
#    "ancestry_roll": ancestry_roll,
    "dndclass": dndclass,
#    "class_roll": class_roll,
    "level": level,
    "gender": gender,
    "disposition": disposition,
    "alignment": alignment,
#    "gender_roll": gender_roll,
#    "disposition_roll": disposition_roll,
#    "alignment_roll": alignment_roll,
    "No_HOF": No_HOF
}.items():
    if key not in st.session_state:
        st.session_state[key] = val

def generate_npc():
    # use globals (values set earlier in the run from widgets are available)
    global classification, ancestry, dndclass, name, level, classification_roll, ancestry_roll, class_roll, gender, gender_roll, disposition, disposition_roll, alignment, alignment_roll, No_HOF

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

    # Persist generated values into session_state for rendering after rerun
    st.session_state.name = name
    st.session_state.classification = classification
    st.session_state.ancestry = ancestry
    st.session_state.dndclass = dndclass
    st.session_state.level = level
    st.session_state.gender = gender
    st.session_state.disposition = disposition
    st.session_state.alignment = alignment
    st.session_state.classification_roll = classification_roll
    st.session_state.ancestry_roll = ancestry_roll
    st.session_state.class_roll = class_roll
    st.session_state.gender_roll = gender_roll
    st.session_state.disposition_roll = disposition_roll
    st.session_state.alignment_roll = alignment_roll
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

st.button("Generate NPC", type="primary", use_container_width=True, disabled=disallow_generation, on_click=generate_npc)

print(No_HOF, st.session_state.No_HOF)

# Render the generated UI only when generation has happened (persisted in session_state)
if st.session_state.generated:
    # Output NPC Details (use session_state values)
    st.markdown("---", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>Generated NPC</h4>", unsafe_allow_html=True)

    # Censoring

    if pf.is_clean(name) and name != "":
        NPC_Output = f"Name: {st.session_state.name}\nClassification: {st.session_state.classification}\nAncestry: {st.session_state.ancestry}\nClass: {st.session_state.dndclass}\nLevel: {st.session_state.level}\nGender: {st.session_state.gender}\nDisposition: {st.session_state.disposition}\nAlignment: {st.session_state.alignment}"
        No_HOF = False
        st.code(NPC_Output)
    else:
        st.code(f"Name: {st.session_state.ancestry} {st.session_state.dndclass} ({st.session_state.level})\nClassification: {st.session_state.classification}\nAncestry: {st.session_state.ancestry}\nClass: {st.session_state.dndclass}\nLevel: {st.session_state.level}\nGender: {st.session_state.gender}\nDisposition: {st.session_state.disposition}\nAlignment: {st.session_state.alignment}", height="content")
        if pf.is_profane(name):
            No_HOF = True

    # Hall of Fame

    if st.session_state.level >= 5 and st.session_state.No_HOF != True: 
        st.markdown("<h6 style='text-align: center; color: #e3256b;'>High-Level NPC Generated!</h6>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: center; color: #e3256b;'>Consider adding them to the Hall of Fame below.</h6>", unsafe_allow_html=True)
        if st.button("Add to Hall of Fame", type="secondary", use_container_width=True, disabled=st.session_state.No_HOF):
            with open("NPC_Hall_of_Fame.txt", "a") as hof: # Maybe write as json instead, just for clarity in the future.
                hof.write(f"Name: {st.session_state.ancestry} {st.session_state.dndclass} ({st.session_state.level}), Classification: {st.session_state.classification}, Ancestry: {st.session_state.ancestry}, Class: {st.session_state.dndclass}, Level: {st.session_state.level}, Gender: {st.session_state.gender}, Disposition: {st.session_state.disposition}\n") 
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

        


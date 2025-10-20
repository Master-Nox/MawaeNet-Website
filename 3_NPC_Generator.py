import streamlit as st
from streamlit_extras.row import row
import random

def random_roll(min_value, max_value, modifier=0):
    return random.randint(min_value, max_value)+modifier

st.markdown("<h1 style='text-align: center;'>Alyrian NPC Generator</h1>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: left;'>Generate unique non-player characters (NPCs) with Alyraian Homebrew.</h6>", unsafe_allow_html=True)
st.write("")
st.markdown("---", unsafe_allow_html=True)

## Options Section
st.markdown("<h4 style='text-align: center;'>Options</h4>", unsafe_allow_html=True) 

st.checkbox("Accurate Distributions?", value=True, key="accurate_distributions")
st.checkbox("Player Classes Only?", value=True, key="player_classes_only")

if st.button("Generate NPC", type="primary", use_container_width=True):
    st.markdown("---", unsafe_allow_html=True)

## Generate Classification
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
    st.markdown(f"<h6 style='text-align: left;'>Classification: {classification}</h6>", unsafe_allow_html=True)
    st.write(f"Roll: {classification_roll}")

## Generate Ancestry
    ancestry_roll = random_roll(1, 200)
    if classification == "Naturalborn":
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

## Generate Class
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
        else:
            dndclass = "I'm comin back later to finish this :3"

    # Output NPC Details
    st.markdown("---", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>Generated NPC</h4>", unsafe_allow_html=True) # Replace with actual generated name, Ancestry, Classification, and other details later
    NPC_Details_Row1 = row([0.05,0.1,0.85], vertical_align="center", gap="small", )
    NPC_Details_Row1.markdown(f"<h6 style='text-align: left;'>Roll: [Placeholder]</h6>", unsafe_allow_html=True)
    NPC_Details_Row1.markdown("<h3 style='text-align: left;'>Name: </h3>", unsafe_allow_html=True)
    NPC_Details_Row1.markdown("<h3 style='text-align: left;'>[Placeholder] </h3>", unsafe_allow_html=True)

    NPC_Details_Row2 = row([0.05,0.1,0.85], vertical_align="center", gap="small")
    NPC_Details_Row2.markdown(f"<h6 style='text-align: left;'>Roll: {classification_roll}</h6>", unsafe_allow_html=True)
    NPC_Details_Row2.markdown(f"<h3 style='text-align: left;'>Classification: </h3>", unsafe_allow_html=True)
    NPC_Details_Row2.markdown(f"<h3 style='text-align: left;'>{classification}</h3>", unsafe_allow_html=True)

    NPC_Details_Row3 = row([0.05,0.1,0.85], vertical_align="center", gap="small")
    NPC_Details_Row3.markdown(f"<h6 style='text-align: left;'>Roll: {ancestry_roll}</h6>", unsafe_allow_html=True)
    NPC_Details_Row3.markdown(f"<h3 style='text-align: left;'>Ancestry: </h3>", unsafe_allow_html=True)
    NPC_Details_Row3.markdown(f"<h3 style='text-align: left;'>{ancestry}</h3>", unsafe_allow_html=True)

    NPC_Details_Row4 = row([0.05,0.1,0.85], vertical_align="center", gap="small")
    NPC_Details_Row4.markdown(f"<h6 style='text-align: left;'>Roll: {class_roll}</h6>", unsafe_allow_html=True)
    NPC_Details_Row4.markdown(f"<h3 style='text-align: left;'>Class: </h3>", unsafe_allow_html=True)
    NPC_Details_Row4.markdown(f"<h3 style='text-align: left;'>{dndclass}</h3>", unsafe_allow_html=True)

    # Codeblock Output for easy copying
    st.markdown("---", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center;'>Copyable</h5>", unsafe_allow_html=True)
    st.code(f"Name: [Placeholder]\nClassification: {classification}\nAncestry: {ancestry}\nClass: {dndclass}", height=150)


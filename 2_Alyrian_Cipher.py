import streamlit as st

LOWALPHABET = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
UPALPHABET = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
vowels = ["a","e","i","o","u","y", "A","E","I","O","U","Y"]
OutputText = ""

def count(string, chars):
    counter = 0
    for char in chars:
        counter += string.count(char)
    return counter
    
st.markdown("<h1 style='text-align: center;'>Alyrian Cipher Encoder</h1>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: left;'>This is a simple translator that translates English to Alyrian and vice versa. The Alyrian language is a fictional language created for the purpose of this cipher. It uses a combination of the Vigenère cipher and a custom substitution cipher based on vowel counts and word lengths.</h6>", unsafe_allow_html=True)
st.write("")

VigenereKey = st.text_input('Enter the Vigenere Key:', 'Alyra')

if VigenereKey == "":
    st.write("Please enter a key.")
    st.stop()

ToBeTranslated = st.text_area("Enter the text you want to translate to Alyrian:", height="content") # Should output tcyesllrvcit. "tlqkebut"

if ToBeTranslated == "":
    st.write("Please enter text to translate.")
    st.stop()

WordList = ToBeTranslated.split()

for Word in WordList:
    vowelcount = count(Word, vowels)
    SpecialKeyValue = []
    SpecialKeyLen = len(VigenereKey)
    keycount = 0
    VKeyIndex = 0
    CharIndex = 0
    NonCharSaver = {}
    Encrypted = ""

    for i in VigenereKey:
        SpecialKeyValue.append(i.lower())

    for character in Word: # Saves non-character symbols and removes them from the word for processing.
        if character not in LOWALPHABET and character not in UPALPHABET:
            NonCharSaver[CharIndex] = character
            Word = Word.replace(character, "")
        CharIndex += 1
    
    CharIndex = 0

    lengthforkey = len(Word) # Calculates length of the word after non-character symbols have been removed.
    while lengthforkey > 5:
        lengthforkey = lengthforkey - 6  # Ensures that B never errors if there are more than 6 vowels in a word.

    for character in Word:
        VKeyIndex += 1
        if VKeyIndex > SpecialKeyLen:
            VKeyIndex = 1
        keycount += 1
        if keycount > 3:
            keycount = 1
        if keycount == 1:
            key = LOWALPHABET[vowelcount - 1]  # How many vowels in non-translated word. First letter within key.
        elif keycount == 2:
            key = LOWALPHABET[lengthforkey]  # How many letters in non-translated word. Second letter within key.
        else:
            key = Word[0] # First letter of non-translated word. Third letter within key.
        
        LetterReplace = LOWALPHABET.index(character.lower()) + LOWALPHABET.index(SpecialKeyValue[VKeyIndex - 1])  # Uses the special key inputted above.
        if LetterReplace > 25:
            LetterReplace = LetterReplace - 26
        Encrypted += LOWALPHABET[LetterReplace]
        
    if Word == "":
        break

    A = str(LOWALPHABET[vowelcount - 1]) 
    B = str(vowels[lengthforkey - 1])
    C = str(Word[0].lower())

    length = len(Word)
    # st.write(f"Word: {Word}")
    # st.write(NonCharSaver)
    # st.write("----------------------------")
    # st.write(f"Length of Word: {length}")
    # st.write(f"Word: {Word}\n\nKey: {A} {B} {C}")

    if length % 2 == 0:
        Encrypted = A + B + C + Encrypted
    else:
        Encrypted = Encrypted + A + B + C

    if length % 2 == 0:
        for NonChar in NonCharSaver:
            # st.write(f"NonChar: {NonChar}")
            # st.write(f"Length: {length}")
            if NonChar == length-1+len(NonCharSaver):
                NonCharIndex = NonChar + 3
            elif NonChar == 0:
                NonCharIndex = 0
            else:
                NonCharIndex = NonChar + 3
            # st.write(f'Inserting "{NonCharSaver[NonChar]}" at position {NonCharIndex} in "{Encrypted}"')
            Encrypted = Encrypted[:NonCharIndex] + NonCharSaver[NonChar] + Encrypted[NonCharIndex:]
    else:
        for NonChar in NonCharSaver:
            # st.write(f"NonChar: {NonChar}")
            # st.write(f"Length: {length}")
            if NonChar == length-1+len(NonCharSaver):
                NonCharIndex = NonChar + 3
            elif NonChar == 0:
                NonCharIndex = 0
            else:
                NonCharIndex = NonChar
            # st.write(f'Inserting "{NonCharSaver[NonChar]}" at position {NonCharIndex} in "{Encrypted}"')
            Encrypted = Encrypted[:NonCharIndex] + NonCharSaver[NonChar] + Encrypted[NonCharIndex:]

    if Word[0].isupper():
        Encrypted = Encrypted.capitalize()
    OutputText += Encrypted + " "

st.subheader("Translated Text:")
st.code(OutputText, wrap_lines=True, language=None, line_numbers=True)
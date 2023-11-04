#!/usr/bin/env python3
# Author: AnalogMan, SwayStation
# Modified Date: 2023-11-03
# Purpose: Generates Bandai Vital Bracelet Name Sprites for DIM modifications
# Usage: DIMNameGen [-h] [-n name]
# Requirements: Pillow (pip3 install Pillow)

from sys import version_info, exit
if version_info <= (3,2,0):
    print('\nPython version 3.2.0+ needed to run this script.')
    exit(1)

try: 
    from PIL import Image, ImageOps # pip3 import Pillow
except:
    print('\nDependancies missing:\npip3 install Pillow\n')
    exit(1)

import os
import argparse

def load_file(file_name: str) -> str:
        return os.path.join(os.path.dirname(__file__), file_name)

def cleanFilename(sourcestring,  removestring = "%:/,.\\[]<>*?"):
    """Clean a string by removing selected characters.

    Creates a legal and 'clean' source string from a string by removing some 
    clutter and  characters not allowed in filenames.
    A default set is given but the user can override the default string.

    Args:
        | sourcestring (string): the string to be cleaned.
        | removestring (string): remove all these characters from the string (optional).

    Returns:
        | (string): A cleaned-up string.

    Raises:
        | No exception is raised.
    """
    #remove the undesireable characters
    return ''.join([c for c in sourcestring if c not in removestring])

def main():
    
    print('\n======== DIM Name Generator ========\n\n')

    # Arg parser for program options
    parser = argparse.ArgumentParser(description='Create name sprites from string for Bandai Vital Bracelet DIM modification')
    parser.add_argument('-n', '--name', help='The name string to have generated')
    
    # Check passed arguments
    args = parser.parse_args()

    # Attempt to open alphabet sprite sheet and complain if cannot
    try:
        charsheet = Image.open(load_file("assets/VB_Alphabet_ENG.png")).convert("RGB")
    except:
        print("Font Sprite Sheet missing: VB_Alphabet_ENG.png")
        exit(1)

    # Dictionary map letters to alphabet sprite sheet
    letters = {}
    letters["A"] = charsheet.crop((0, 0, 8, 15))
    letters["B"] = charsheet.crop((10, 0, 16, 15))
    letters["C"] = charsheet.crop((18, 0, 24, 15))
    letters["D"] = charsheet.crop((26, 0, 32, 15))
    letters["E"] = charsheet.crop((34, 0, 39, 15))
    letters["F"] = charsheet.crop((41, 0, 46, 15))
    letters["G"] = charsheet.crop((48, 0, 54, 15))
    letters["H"] = charsheet.crop((56, 0, 63, 15))
    letters["I"] = charsheet.crop((65, 0, 67, 15))
    letters["J"] = charsheet.crop((69, 0, 75, 15))
    letters["K"] = charsheet.crop((77, 0, 83, 15))
    letters["L"] = charsheet.crop((85, 0, 90, 15))
    letters["M"] = charsheet.crop((92, 0, 102, 15))

    letters["N"] = charsheet.crop((104, 0, 114, 15))
    letters["O"] = charsheet.crop((116, 0, 123, 15))
    letters["P"] = charsheet.crop((125, 0, 131, 15))
    letters["Q"] = charsheet.crop((133, 0, 140, 15))
    letters["R"] = charsheet.crop((142, 0, 148, 15))
    letters["S"] = charsheet.crop((150, 0, 157, 15))
    letters["T"] = charsheet.crop((159, 0, 165, 15))
    letters["U"] = charsheet.crop((167, 0, 174, 15))
    letters["V"] = charsheet.crop((176, 0, 183, 15))
    letters["W"] = charsheet.crop((185, 0, 195, 15))
    letters["X"] = charsheet.crop((197, 0, 203, 15))
    letters["Y"] = charsheet.crop((205, 0, 211, 15))
    letters["Z"] = charsheet.crop((213, 0, 219, 15))

    letters["a"] = charsheet.crop((221, 0, 226, 15))
    letters["b"] = charsheet.crop((228, 0, 233, 15))
    letters["c"] = charsheet.crop((235, 0, 240, 15))
    letters["d"] = charsheet.crop((242, 0, 247, 15))
    letters["e"] = charsheet.crop((249, 0, 254, 15))
    letters["f"] = charsheet.crop((256, 0, 260, 15))
    letters["g"] = charsheet.crop((262, 0, 268, 15))
    letters["h"] = charsheet.crop((270, 0, 276, 15))
    letters["i"] = charsheet.crop((278, 0, 279, 15))
    letters["j"] = charsheet.crop((281, 0, 284, 15))
    letters["k"] = charsheet.crop((286, 0, 291, 15))
    letters["l"] = charsheet.crop((293, 0, 294, 15))
    letters["m"] = charsheet.crop((296, 0, 305, 15))

    letters["n"] = charsheet.crop((307, 0, 313, 15))
    letters["o"] = charsheet.crop((315, 0, 320, 15))
    letters["p"] = charsheet.crop((322, 0, 327, 15))
    letters["q"] = charsheet.crop((329, 0, 334, 15))
    letters["r"] = charsheet.crop((336, 0, 341, 15))
    letters["s"] = charsheet.crop((343, 0, 348, 15))
    letters["t"] = charsheet.crop((350, 0, 354, 15))
    letters["u"] = charsheet.crop((356, 0, 361, 15))
    letters["v"] = charsheet.crop((363, 0, 368, 15))
    letters["w"] = charsheet.crop((370, 0, 379, 15))
    letters["x"] = charsheet.crop((381, 0, 387, 15))
    letters["y"] = charsheet.crop((389, 0, 396, 15))
    letters["z"] = charsheet.crop((398, 0, 403, 15))

    letters[" "] = charsheet.crop((405, 0, 407, 15))
    letters["-"] = charsheet.crop((409, 0, 411, 15))
    letters[":"] = charsheet.crop((413, 0, 414, 15))
    letters["."] = charsheet.crop((416, 0, 417, 15))
    letters["("] = charsheet.crop((419, 0, 422, 15))
    letters[")"] = charsheet.crop((424, 0, 427, 15))
    
    letters["1"] = charsheet.crop((261, 0, 264, 15))
    letters["2"] = charsheet.crop((265, 0, 270, 15))
    letters["3"] = charsheet.crop((271, 0, 276, 15))
    letters["4"] = charsheet.crop((277, 0, 283, 15))
    letters["5"] = charsheet.crop((284, 0, 289, 15))
    letters["6"] = charsheet.crop((290, 0, 296, 15))
    letters["7"] = charsheet.crop((297, 0, 302, 15))
    letters["8"] = charsheet.crop((303, 0, 309, 15))
    letters["9"] = charsheet.crop((310, 0, 316, 15))
    letters["0"] = charsheet.crop((317, 0, 323, 15))
    
    # List of serif letters
    serif = ["A", "M", "S", "V", "W"]

    white = (255, 255, 255)
    green = (0, 255, 0)
    
    # Check that only supported characters are in name string
    for elem in name:
        try:
            letters[elem]
        except:
            print("Could not find letter " + repr(elem) + " in character sheet.")
            print("Available characters: \"A-Z -:.() 0-9\"")
            exit(1)
    
    # Check if official Bandai sprite exists
    if not os.path.exists("output"):
        os.makedirs("output")
    
    if os.path.isfile(load_file("assets/" + name + ".png")):
        print("String found amoung official Bandai sprites. Using official sprite.")
        print("Saving file to output/" + name + ".png")
        Image.open(load_file("assets/" + name + ".png")).convert("RGB").save("output/" + name + ".png")
        print("Completed Successfully.")
        exit(0)
            

    # Create starter name sprite
    canvas_w = 80
    namesprite = Image.new("RGB", (canvas_w, 15), green)

    # Set X position padding
    x = 1

    # Iterate through each letter, check how close the two adjoining letters are and add space if too close.
    for elem in name:
        x += 1
        y = 3

        # If the current X position for the next letter would go beyond the sprites current width, increase width another 80px
        if x + letters[elem].width > canvas_w:
            namesprite = ImageOps.expand(namesprite, (0, 0, 80, 0), green)
            canvas_w += 80

        # This simulates the kerning style from the officially released Vital Hero name sprites
        while y <= 12:
            if letters[elem].getpixel((0, y)) != white:
                y+=1
                continue

            if (
                namesprite.getpixel((x-2, y)) == white or
                namesprite.getpixel((x-2, y-1)) == white or
                namesprite.getpixel((x-2, y-2)) == white or
                namesprite.getpixel((x-2, y+1)) == white or
                namesprite.getpixel((x-2, y+2)) == white
            ):

                x += 1

            else:
                y += 1

        # Add letter into name sprite canvas
        namesprite.paste(letters[elem], (x, 0))
        x += letters[elem].width
        
    # Get width of actual text
    text_w = canvas_w - 1
    y = 3
    while text_w > 0:
        if namesprite.getpixel((text_w, y)) == white:
            break
        elif y < 12:
            y = y + 1
        else:
            text_w = text_w - 1
            y = 3
    # Remove two pixel border on left side
    text_w = text_w - 2
    
    # Determine left padding based on canvas width
    lmargin = 0
    if canvas_w == 80:
        # Center sprite with a left margin of at least 2px
        x = (80 - text_w) // 2
        lmargin = x - 2
    elif canvas_w == 160:
        # Add a 3px or 4px left margin based on wether the first letter is serif
        x = 3 if (name[0] in serif) else 4
        if text_w + x > 160:
            lmargin = 0
        else:
            lmargin = x - 2
    else:
        # Add a 5px or 6px left margin based on wether the first letter is serif
        x = 5 if (name[0] in serif) else 6
        if text_w + x > 240:
            lmargin = 0
        else:
            lmargin = x - 2
    if lmargin < 0:
        lmargin = 0
        
    # TODO: Check if right margin is at least 2x. If not, use alternate MON kerning
    if name[-3::1] == "MON":
        if (text_w + 2 + lmargin) > (canvas_w - 3):
            if (text_w + 2 + lmargin) == (canvas_w - 1):
                x = canvas_w - 36
            else:
                x = canvas_w - 37
            namesprite.paste(letters["M"], (x, 0))
            namesprite.paste(letters[" "], (x+12, 0))
            namesprite.paste(letters["O"], (x+13, 0))
            namesprite.paste(letters[" "], (x+23, 0))
            namesprite.paste(letters["N"], (x+24, 0))
            namesprite.paste(letters[" "], (x+34, 0))
       
    # Create new canvas to paste into
    namesprite2 = Image.new("RGB", (canvas_w, 15), green)
    tmp = namesprite.copy()
    namesprite2.paste(tmp, (lmargin,0))
        

    print("Creating sprite " + name + ", width: " + str(canvas_w) + "px")
    
    # Save result to output folder       
    print("Saving file to output/" + cleanFilename(name) + ".png")
    namesprite2.save("output/" + cleanFilename(name) + ".png")

    print("Completed Successfully.")

if __name__ == '__main__':
    main()

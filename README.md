# DIM Name Gen
A utility to generate Bandai Vital Bracelet compatible name sprites

Usage: DIMNameGen.exe [-h] [-n NAME]

Running the utility by itself will bring up a prompt to type a name. The name will be saved into an output folder.
Passing the argument -n followed by a name in quotations will generate that name without the interactive prompt.

Included in the repo is an example batch file for bulk creating sprites. Create a TXT file with the names you want, one per line, then drag and drop the TXT file onto the BAT file. It will generate all the names in the TXT and name the folder the same as the TXT filename. 

This utility was written in python and converted to stand-alone executable with Nuitka.

To use the python script:

Usage: DIMNameGen.py [-h] [-n NAME]

1. Click the green Code button  towards the top followed by Download ZIP. Extract the files to any folder.
2. You will need an install of python3. Either from https://www.python.org/ or from the Windows Store.
3. Once python is installed you will need to install the Pillow dependency by opening terminal/command prompt and typing `pip install Pillow`
4. Once Pillow is installed you can run the script from terminal/command prompt with `python DIMNameGen.py` (or `python3 DIMNameGen.py`) or use the included BAT file to make use of the TXT file drag and drop.
_
_
_
SwayStation's Fork (DigiScript Mod) Notes:

Removed the uppercase only font with a new original font called DigiScript.
DigiScript has both uppecase and lowercase inputs and DIM Name Gen will now output whatever you type with case-sensitivity.

If you input a name that is found in the official Bandai sprites database, it will output a name with "Capitilization" in effect in the DigiScript font.
If you would prefer to have the name in all caps, first remove the Bandai sprite file from the "assets" folder and then input the desired name in all caps.


Future updates:
- Make GUI for macOS
- Create batch file for macOS

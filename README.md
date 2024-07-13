# simpleoramapmodder
Simple command-line OpenRA map modder written in Python.

This script will take a standard .oramap and convert it to a BI modded map, or a custom mod with some editing.

Instructions on how to use in Windows:

1. Create a folder of any name and two subfolders, append, and assets.
2. Place the standard unmodded .oramap in the folder you created.
3. Place all the mod files you want inside the assets folder, with the exception of map.bin, map.png, and map.yaml. You can use the provided assets folder for a standard BI-3.6 mod, or your own.
4. Create two .txt files in the append folder named append.txt, and category.txt, or use the provided examples for BI-3.6 rules.
5. Edit append.txt with what you want to add at the end of the map.yaml.
6. Edit category.txt with the category you want for the map chooser in game.
7. Make sure you have Python 3.x installed and required packages.
8. Cd to the folder you created.
9. To run use the command: python simpleoramapmodder.py

10. Optional: Before playing the map, open the map in the Map Editor and save it to ensure compatibility.
11. If you want to mod another map the same way, just delete the original .oramap, place another map in the same folder, and run the script again.

To change the title of the map from saying BI-3.6, edit line 51 of the script.

To change the end of the filename from _BI-3.6 to something else, edit line 86 of the script.


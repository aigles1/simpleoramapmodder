# simpleoramapmodder
Simple command-line OpenRA map modder written in Python.
Most of the code was written with the assistance of AI.

This script will take a standard .oramap and convert it to a BI modded map, or a custom mod with some editing.

Instructions on how to use in Windows:

1. Create a folder of any name and two subfolders, append, and assets.
2. Place the standard unmodded .oramap in the folder you created.
3. Place all the mod files you want inside the assets folder, with the exception of map.bin, map.png, and map.yaml. You can use the provided assets folder for a standard BI-3.6 mod, or your own.
4. Create two .txt files in the append folder named append.txt, and category.txt, or use the provided examples.
5. Edit append.txt with what you want to add at the end of the map.yaml. You can use the provided append.txt for BI-3.6 rules, or your own.
6. Edit category.txt with the category you want for the map chooser in game.
7. Make sure you have Python 3.x installed.
8. Open cmd or powershell and cd to the folder you created.
9. To run use the command: python simpleoramapmodder.py

10. Optional: Before playing the map, open the map in the Map Editor and save it to ensure compatibility.
11. If you want to mod another map the same way, just delete the original .oramap and place another map in the same folder to run the script again.

To change the title of the map from saying BI-3.6, edit line 51 of the python script in a text editor. (line += ' BI-3.6')
To change the end of the filname from _BI-3.6 to something else, edit line 86 of the python script. (new_zip_name = f"{base_name}_BI-3.6{ext}")


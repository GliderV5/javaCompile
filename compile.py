import os
import sys
os.system("clear")
os.system("javac -d bin src/passToHash/*.java")
print("")
print("######## Lancement du programme ########")
print("")
os.system('java -cp bin/ passToHash.Main')
print()

if "--jar" in sys.argv:
    os.system("jar cvfm passToHash.jar manifest.txt -C bin/ .")
    print("fichier jar créé")

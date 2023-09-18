import os
import sys
os.system("clear")
os.system("javac -d bin src/<package>/*.java")
print("")
print("######## Lancement du programme ########")
print("")
os.system('java -cp bin/ <package>.<main_class>')
print()

if "--jar" in sys.argv:
    os.system("jar cvfm <jar_name>.jar manifest.txt -C bin/ .")
    print("fichier jar créé")


import time
import easygui
import os
from os import path

counter = 0
# path = "H:\\Ordnerstruktur Barto\\Schaltplaene"
pathsp = easygui.diropenbox()
#Dateinamen
schaltplanUV = f"08_TU_175G010AA000_2019_03_06_07_52_Schaltplan_UV_1_2.pdf"
protok_unt = f"08_TU_175G010AA000_2019_03_26_07_30_Protokoll_Unterschrieben.pdf"
legende = f"Stromkreislegende_UV_1_2.pdf"
zw1 = "175G0101alt.zw1"

print("-----------Alle fehlenden Dateien/Ordner einfügen!-----------")
'''Ordnerbenennung wenn möglich mit Schlüsselwörtern wie „Lüftung", „NSHV", „Serverraum2", „Halle" und „Technikum" benennen. /n Andernfalls werden die neuen Ordner nicht aufgelistet und das Programm muss abgeändert werden./n
print('Dateibenennung nur mit „Schaltplan_", „Protokoll_Unterschrieben_", „Stromkreislegende_" und der Ordnername der die Datei beinhaltet (UV_1_2 bzw. UV-1_2, UV_Bezeichnung).'''


#Schaltplan_UV_{beforedot}_{afterdot}.pdf

sp = False
prtk = False
leg = False
zw = False


for s, (root, dirs, files) in enumerate(os.walk(pathsp)):
    if "UV" in root or "Lüftung" in root or "NSHV" in root or "Serverraum 2" in root or "Halle" in root or "Technikum" in root:
        print(f"Ordner {s -3} ({root})")
        lastpart = os.path.basename(os.path.normpath(root))
        splitin2 = lastpart.split(".")
        beforedot = splitin2[0].replace("UV ", "")
        afterdot = splitin2[-1]
        # Archiv-Format
        seclast = os.path.split(os.path.split(root)[0])[1]
        splitintwo = seclast.split(".")
        befored = splitintwo[0].replace("UV ", "")
        afterd = splitintwo[-1]

        # for-loop mit file für eine Datei..
        for file in files:
            if "Schaltplan" in file and file.endswith(".pdf"):
                print(" ".join((file, "vorhanden!")))
                counter += 1
                sp = True
            elif "Protokoll" in file and file.endswith(".pdf"):
                print(" ".join((file, "vorhanden!")))
                counter += 1
                prtk = True
            elif "legende" in file and file.endswith(".pdf"):
                print(" ".join((file, "vorhanden!")))
                counter += 1
                leg = True
            elif file.endswith(".zw1"):
                print(" ".join((file, "vorhanden!")))
                counter += 1
                zw = True
        for t in files:
            if sp == False:
                print(" ".join(f"08_TU_175G010AA000_Datum_Uhrzeit_Schaltplan_UV_{beforedot}_{afterdot}.pdf").replace(" ",""), " fehlt!")
                sp = True
            elif prtk == False:
                print(" ".join(f"08_TU_175G010AA000_Datum_Uhrzeit_Protokoll_Unterschrieben_UV_{beforedot}_{afterdot}.pdf").replace(" ",""), " fehlt!")
                prtk = True
            elif leg == False:
                print(" ".join(f"Stromkreislegende_UV_{beforedot}_{afterdot}.pdf").replace(" ",""), " fehlt!")
                leg = True
            elif zw == False:
                print(" ".join(f"175G0101_UV_{beforedot}_{afterdot}.pdf").replace(" ",""), " fehlt!")
                # print(" ".join(("Andere Datei: ", file)))
                zw = True
        # Abzweigung keine Datei existiert! (Verbesserung einbauen)
        if sp == False and prtk == False and leg == False and zw == False:
            print(" ".join(
                f"Schaltplan_UV_{beforedot}_{afterdot}.pdf, \n Protokoll_Unterschrieben_UV_{beforedot}_{afterdot}.pdf, \n Stromkreislegende_UV_{beforedot}_{afterdot}.pdf, \n "
                f"175G0101_UV_{beforedot}_{afterdot}.zw1").replace(" ", ""), "fehlen!")

        print(counter, " Dateien sind vorhanden!")
        counter = 0
        sp = False
        prtk = False
        leg = False
        zw = False

    # Aufgaben: Archiv-Ausgabe,Warnung bei ungenauen Dateinamen, Verhalten bei anderen Dateien anpassen
print("*************************************************************")
for s, (root, dirs, files) in enumerate(os.walk(pathsp)):
    if "UV" in root or "Lüftung" in root or "NSHV" in root or "Serverraum 2" in root:

        # for-loop mit file für eine Datei..
        for file in files:
            if "Schaltplan" in file and file.endswith(".pdf"):
                # print(" ".join((file, "vorhanden!")))
                counter += 1
                sp = True
            elif "Protokoll" in file and file.endswith(".pdf"):
                # print(" ".join((file, "vorhanden!")))
                counter += 1
                prtk = True
            elif "legende" in file and file.endswith(".pdf"):
                # print(" ".join((file, "vorhanden!")))
                counter += 1
                leg = True
            elif file.endswith(".zw1"):
                # print(" ".join((file, "vorhanden!")))
                counter += 1
                zw = True
        print(f"Ordner {s -3} - {counter} Dateien sind vorhanden!")

        counter = 0
        sp = False
        prtk = False
        leg = False
        zw = False

t = input("Enter zum verlassen.")

#FIXME:
#1. Archive raus
#2. bei fehlenden Dateien nur für UV-Ordner „before and afterdot" einsetzen
#3. zusätzliche Ordner bei Suche aufnehmen
#4. Casesensitive beseitigen
#5. Nummern am Anfang entfernen
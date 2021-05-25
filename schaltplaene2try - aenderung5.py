
import time
import easygui
import os
import pathlib


counter = 0
# path = "H:\\Ordnerstruktur Barto\\Schaltplaene"
pathsp = easygui.diropenbox()
#Dateinamen
# schaltplanUV = f"08_TU_175G010AA000_2019_03_06_07_52_Schaltplan_UV_1_2.pdf"
# protok_unt = f"08_TU_175G010AA000_2019_03_26_07_30_Protokoll_Unterschrieben.pdf"
# legende = f"Stromkreislegende_UV_1_2.pdf"
# zw1 = "175G0101alt.zw1"

print("-----------Alle fehlenden Dateien/Ordner einfügen!-----------")
'''Ordnerbenennung wenn möglich mit Schlüsselwörtern wie „Lüftung", „NSHV", „Serverraum2", „Halle" und „Technikum" benennen. /n Andernfalls werden die neuen Ordner nicht aufgelistet und das Programm muss abgeändert werden./n
print('Dateibenennung nur mit „Schaltplan_", „Protokoll_Unterschrieben_", „Stromkreislegende_" und der Ordnername der die Datei beinhaltet (UV_1_2 bzw. UV-1_2, UV_Bezeichnung).'''

sp = False
prtk = False
leg = False
zw = False
counterfolder = 0

for s, (root, dirs, files) in enumerate(os.walk(pathsp)):
    if "UV" in root or "Lüftung" in root or "NSHV" in root or "Serverraum 2" in root or "Halle" in root or "Technikum" in root:
        if "Archiv" in root:
            #counterfolder+=1
            pass
        else:
            counterfolder += 1
            print(f"Ordner {counterfolder} ({root})")
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
            print("Enthält: ")
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
                elif "laufplan" in file and file.endswith(".pdf"):
                    print(" ".join((file, "vorhanden!")))
                    counter += 1
                else:
                    print(" ".join((file, "eventuell anpassen!")))

            #long if with 4 conditions:
            print("Fehlt: ")
            if sp == False and prtk == False and leg == False and zw == False:
                print(" ".join(f"Schaltplan_{lastpart}.pdf, \n Protokoll_Unterschrieben_{lastpart}.pdf, \n Stromkreislegende_{lastpart}.pdf, \n "
                    f"{lastpart}.zw1").replace(" ", ""))


            elif sp == False and prtk == False and leg == False and zw == True:
                print(" ".join(f"Schaltplan_{lastpart}.pdf, \n Protokoll_Unterschrieben_{lastpart}.pdf, \n Stromkreislegende_{lastpart}.pdf").replace(" ", ""))

            elif sp == False and prtk == False and leg == True and zw == False:
                print(" ".join(f"Schaltplan_{lastpart}.pdf, \n Protokoll_Unterschrieben_{lastpart}.pdf,\n " f"{lastpart}.zw1").replace(" ", ""))

            elif sp == False and prtk == False and leg == True and zw == True:
                print(" ".join(f"Schaltplan_{lastpart}.pdf, \n Protokoll_Unterschrieben_{lastpart}.pdf").replace(" ", ""))

            elif sp == False and prtk == True and leg == False and zw == False:
                print(" ".join(f"Schaltplan_{lastpart}.pdf, \n Stromkreislegende_{lastpart}.pdf, \n " f"{lastpart}.zw1").replace(" ", ""))

            elif sp == False and prtk == True and leg == False and zw == True:
                print(" ".join(f"Schaltplan_{lastpart}.pdf, \n Stromkreislegende_{lastpart}.pdf").replace(" ", ""))

            elif sp == False and prtk == True and leg == True and zw == False:
                print(" ".join(f"Schaltplan_{lastpart}.pdf, \n" f"{lastpart}.zw1").replace(" ", ""))

            elif sp == False and prtk == True and leg == True and zw == True:
                print(" ".join(f"Schaltplan_{lastpart}.pdf").replace(" ", ""))

            elif sp == True and prtk == False and leg == False and zw == False:
                print(" ".join(f"Protokoll_Unterschrieben_{lastpart}.pdf, \n Stromkreislegende_{lastpart}.pdf, \n " f"{lastpart}.zw1").replace(" ", ""))

            elif sp == True and prtk == False and leg == False and zw == True:
                print(" ".join(f"Protokoll_Unterschrieben_{lastpart}.pdf, \n Stromkreislegende_{lastpart}.pdf").replace(" ", ""))

            elif sp == True and prtk == False and leg == True and zw == False:
                print(" ".join(f"Protokoll_Unterschrieben_{lastpart}.pdf, \n " f"{lastpart}.zw1").replace(" ", ""))

            elif sp == True and prtk == False and leg == True and zw == True:
                print(" ".join(f"Protokoll_Unterschrieben_{lastpart}.pdf").replace(" ", ""))

            elif sp == True and prtk == True and leg == False and zw == False:
                print(" ".join(f"Stromkreislegende_{lastpart}.pdf, \n " f"{lastpart}.zw1").replace(" ", ""))

            elif sp == True and prtk == True and leg == False and zw == True:
                print(" ".join(f"Stromkreislegende_{lastpart}.pdf").replace(" ", ""))

            elif sp == True and prtk == True and leg == True and zw == False:
                print(" ".join(f"{lastpart}.zw1").replace(" ", ""))

            elif sp == True and prtk == True and leg == True and zw == True:
                pass

            if counter == 1:
                print(counter, " Datei ist vorhanden!")
            else:
                print(counter, " Dateien sind vorhanden!")

            counter = 0
            sp = False
            prtk = False
            leg = False
            zw = False

    # Aufgaben: Archiv-Ausgabe,Warnung bei ungenauen Dateinamen, Verhalten bei anderen Dateien anpassen
print("**************************************************************************************************************************************************")
# for s, (root, dirs, files) in enumerate(os.walk(pathsp)):
#     if "UV" in root or "Lüftung" in root or "NSHV" in root or "Serverraum 2" in root or "Halle" in root or "Technikum" in root:
#         if "Archiv" in root:
#             pass
#         else:
#             # for-loop mit file für eine Datei..
#             for file in files:
#                 if "Schaltplan" in file and file.endswith(".pdf"):
#                     # print(" ".join((file, "vorhanden!")))
#                     counter += 1
#                     sp = True
#                 elif "Protokoll" in file and file.endswith(".pdf"):
#                     # print(" ".join((file, "vorhanden!")))
#                     counter += 1
#                     prtk = True
#                 elif "legende" in file and file.endswith(".pdf"):
#                     # print(" ".join((file, "vorhanden!")))
#                     counter += 1
#                     leg = True
#                 elif file.endswith(".zw1"):
#                     # print(" ".join((file, "vorhanden!")))
#                     counter += 1
#                     zw = True
#
#             print(f"Ordner {s - 2} - {counter} Dateien sind vorhanden!")
#
#             counter = 0
#             sp = False
#             prtk = False
#             leg = False
#             zw = False
#
# t = input("Enter zum verlassen.")

counterfolder = 0
for s, (root, dirs, files) in enumerate(os.walk(pathsp)):
    if "UV" in root or "Lüftung" in root or "NSHV" in root or "Serverraum 2" in root or "Halle" in root or "Technikum" in root:
        if "Archiv" in root:
            #counterfolder+=1
            pass
        else:
            counterfolder += 1
            path = pathlib.PurePath(root)
            paththird = path.parent.parent.name
            pathsec = path.parent.name
            pathfirst = path.name

            print(f"Ordner {counterfolder} ({paththird}\\{pathsec}\\{pathfirst}) enthält:")#root

            # print(f"Ordner {counterfolder} - {root} enthält:")
            lastpart = os.path.basename(os.path.normpath(root))
            splitin2 = lastpart.split(".")
            beforedot = splitin2[0].replace("UV ", "")
            afterdot = splitin2[-1]
            # Archiv-Format
            seclast = os.path.split(os.path.split(root)[0])[1]
            splitintwo = seclast.split(".")
            befored = splitintwo[0].replace("UV ", "")
            afterd = splitintwo[-1]

            #thirdlast = os.path.dir(_file_)

            # for-loop mit file für eine Datei..
            for file in files:
                if "Schaltplan" in file and file.endswith(".pdf"):
                    print("Schaltplan")
                    counter += 1
                    sp = True
                elif "Protokoll" in file and file.endswith(".pdf"):
                    print("Protokoll")
                    counter += 1
                    prtk = True
                elif "legende" in file and file.endswith(".pdf"):
                    print("Stromkreislegende")
                    counter += 1
                    leg = True
                elif file.endswith(".zw1"):
                    print("zw1-Datei")
                    counter += 1
                    zw = True
                elif "laufplan" in file and file.endswith(".pdf"):
                    print("Stromlaufplan")
                    counter += 1
                else:
                    print(" ".join((file, "eventuell anpassen!")))

            if counter == 1:
                print(counter, " Datei ist vorhanden!")
            else:
                print(counter, " Dateien sind vorhanden!")


            counter = 0
            sp = False
            prtk = False
            leg = False
            zw = False

t = input("Enter zum verlassen.")
#FIXME:
#1. Dritte Ordner anzeigen in Kurzübersicht
#2. Casesensitive beseitigen





# -*- coding: utf-8 -*-

# genera sidebar per dokuwiki


import csv, json

with open("MPs.csv") as file:
	lines = csv.DictReader( file, delimiter=";" )
	inici_arxiu = True
	cicle = ""
	modul = ""
	for line in lines:
		inici_cicle = False
		inici_modul = False
		if line["cicle"]:
			inici_cicle = True
			# nou cicle
			if not inici_arxiu:
				# tanquem l'anterior cicle
				print("\n<--")
				# tanquem el darrer modul de l'anterior cicle
				print("\n<--")
			inici_arxiu = False
			cicle = line["cicle"].upper()
			titol_cicle = line["titol_cicle"]
			print("\n--> {} {}#\n".format( cicle, titol_cicle ))
			print("[[{cicle} {desc}|Tots els mòduls del cicle]]".format(
				cicle=cicle,
				desc=titol_cicle))
		if line["modul"]:
			inici_modul = True
			if not inici_cicle:
				# tanquem anterior modul
				print("\n<--\n")
			# nou modul
			modul = line["modul"].replace(".","").replace("  "," ")
			print("\n--> {}#".format(modul))
			print("[[{cicle} {modul}|Totes les UFs del modul]]\n".format(
				cicle=cicle,modul=modul))
		if line["uf"]:
			# nova UF
			uf = line["uf"].replace(".","").replace("  "," ").replace(":","")
			mod = modul.split(" ")[0]
			print("\n  * [[{} {} {}|{}]]".format(cicle,mod,uf,uf))

# tanquem darrer modul del darrer cicle
print("\n<--")
# tanquem darrer cicle
print("\n<--\n")


"""ufs = {}
with open("MPs.csv") as file:
	mps = csv.DictReader( file, delimiter=";" )
	for mp in mps:
		# creem cicle
		if mp["cicle"] not in ufs.keys():
			ufs[ mp["cicle"] ] = {}
			ufs[ mp["cicle"] ]["titol"] = mp["titol_cicle"]
		# creem modul
		if mp["modul"] not in ufs[ mp["cicle"] ].keys():
			ufs[ mp["cicle"] ][ mp["modul"] ] = {}
			ufs[ mp["cicle"] ][ mp["modul"]] ["titol"] = mp["titol_modul"]
		# creem UF
		if mp["uf"] not in ufs[mp["cicle"]][mp["modul"]].keys():
			ufs[mp["cicle"]][mp["modul"]][mp["uf"]] = mp["titol_uf"]
	print(json.dumps(ufs,indent=4))
"""

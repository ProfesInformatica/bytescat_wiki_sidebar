# -*- coding: utf-8 -*-

# genera cercadors de cicle, modul i UF per dokuwiki BYTES.CAT

import csv, json, unidecode

carpeta = "pages/"
plantilla = """
====== {titol} ======

{tags}

===== Pàgines en aquesta wiki =====

{{{{topic> {topics} }}}}

"""
vocals = {
	"a": ["à","á","â","ä"],
	"e": ["è","é","ê","ë"],
	"i": ["í","ì","î","ï"],
	"o": ["ò","ó","ô","ö"],
	"u": ["ù","ú","û","ü"],
	"A": ["À","Á","Â","Ä"],
	"E": ["È","É","Ê","Ë"],
	"I": ["Í","Ì","Î","Ï"],
	"O": ["Ò","Ó","Ô","Ö"],
	"U": ["Ù","Ú","Û","Ü"],
}

def treu_accents(s):
	for i in vocals.keys():
		for j in vocals[i]:
			s = s.replace(j,i)
	return s

canvis = ( (" ","_"), ("'","_"), ("’","_"), (".",""),
		("  "," "), (",",""), ("·","_"), (":","") )

def normalitza_nom(nom):
	nom2 = nom
	for canvi in canvis:
		nom2 = nom2.replace( canvi[0], canvi[1] )
	#nom2 = nom.lower().replace(" ","_").replace("'","_").replace("’","_").replace(".","").replace("  "," ")
	return treu_accents( nom2 ).lower()


with open("MPs.csv") as file:
	lines = csv.DictReader( file, delimiter=";" )
	cicle = ""
	modul = ""
	mod = ""
	for line in lines:
		if line["cicle"]:
			# nou cicle
			cicle = line["cicle"]
			titol_cicle = line["titol_cicle"].strip()
			titol = cicle.upper()+" "+titol_cicle
			filename = normalitza_nom(titol)+".txt"
			#print(filename)
			file = open(carpeta+filename,"w")
			file.write( plantilla.format(
					titol=titol,
					tags="#FpInfor #"+cicle.lower().capitalize(),
					topics=" #"+cicle.lower().capitalize(),
					))
			file.close()
		if line["modul"]:
			# nou modul
			modul = line["modul"].strip().replace(".","").replace("  "," ")
			mod = modul.split(" ")[0]
			titol = cicle.upper()+" "+modul
			filename = normalitza_nom(titol)+".txt"
			file = open(carpeta+filename,"w")
			file.write( plantilla.format(
					titol=titol,
					tags="#FpInfor #"+cicle.lower().capitalize()+" #"+cicle.lower().capitalize()+mod.lower().capitalize(),
					topics=" #"+cicle.lower().capitalize()+mod.lower().capitalize(),
					))
			file.close()
		if line["uf"]:
			# nova UF
			uf = line["uf"].strip().replace(".","").replace("  "," ").replace(":","")
			u = uf.split(" ")[0]
			titol = cicle.upper()+" "+mod.upper()+" "+uf
			filename = normalitza_nom(titol)+".txt"
			file = open(carpeta+filename,"w")
			uftag = cicle.lower().capitalize()+mod.lower().capitalize()+u.lower().capitalize()
			uftag2 = uftag[:-1]+"0"+uftag[-1]
			file.write( plantilla.format(
					titol=cicle.upper()+" "+mod.upper()+" "+uf,
					tags="#FpInfor #"+cicle.lower().capitalize()+
							" #"+cicle.lower().capitalize()+mod.lower().capitalize()+
							" #"+uftag+" #"+uftag2,
					topics = " #"+uftag+" #"+uftag2,
					))
			file.close()


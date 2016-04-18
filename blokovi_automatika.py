import re

in_file = open(input("ulazna datoteka? "),"r")

out_file = open("blokovi_"+in_file.name, "w")


rjecnik = {
'ZID' : '30504A-1',
'ZB' : '30504A-1',
'POTPORNI' : '30505A-1',
'ZP' : '30505A-1',
'PZID' : '30505A-1',
'ZIDP' : '30505A-1',
'SUHOZID' : '30506A-1',
'ZIDS' : '30506A-1',
'SUHZID' : '30506A-1',
'OD' : '30507A-1',
'OGRDRV' :'30507A-1',
'OGDR' : '30507A-1',
'POLIGON' : '10401-1',
'POL' : '10401-1',
'OZ' : '30508A-1',
'OZIC' : '30508A-1',
'ZICOGR' :'30508A-1',
'OGRZ' :'30508A-1',
'OZELJ' : '30509A-1',
'ZELJO' : '30509A-1',
'OGZELJ' : '30509A-1',
'STDST' : '40202-1',
'SDST' : '40202-1',
'STDS' : '40202-1',
'DSST' : '40202-1',
'BSTST' : '40203-1',
'BSTS' : '40203-1',
'SDS' : '40202-1',
'DSS' : '40202-1',
'SBS' : '40203-1',
'SBST' : '40203-1',
'BSS' : '40203-1',
'STBET' : '40203-1',
'SMS' : '40204A-1',
'SRASDRV' : '40205A-1',
'SRD' : '40205A-1',
'SRB' : '40205B-1',
'SBR' : '40205B-1',
'SEMAFOR' : '40208-1',
'RAZVODNI_ORMAR' : '40215-1',
'SHSTRUJA' : '402165-1',
'SHSTR' : '402165-1',
'SHS' : '402165-1',
'SAHT_STRUJA' : '402165-1',
'ZATVARAC_NA_POVRSINI' : '40901-1',
'SHV' : '40902B-1',
'SAHT_VODA' : '40902B-1',
'ZATVARAC_OKNO' : '40903-1',
'HIDRANT_POVRSINA' : '40904B-1',
'HIDRANT_OKNO' : '40905-1',
'STTDR' : '41113-1',
'STTELDR' : '41113-1',
'STTD' : '41113-1',
'SHT' : '41119B-1',
'OKNO_TEL' : '41119B-1',
'TEL_OKNO' : '41119B-1',
'SLV' : '41301-1',
'SLIVNIK' : '41301-1',
'SLIV' : '41301-1',
'SLVNIK' : '41301-1',
'REVIZIONO_OKNO' : '41302B-1',
'TALOZNICA' : '41303B-1',
'DB' : '60118-1',
'DC' : '60119-1',
'OZIV' : '60124A-1',
'ZIV' : '60124A-1',
'ZIVICA' : '60124A-1',
'MEDA' : '90501-1',
'MEDJA' :'90501-1'
}


while True:

	linija = in_file.readline()

	if not linija:
		break

	kod = re.split('\s+',linija)
	
	if kod[4] in rjecnik:
		out_file.write('-insert'+" "+rjecnik[kod[4]])
		out_file.write("\n")
		out_file.write(kod[1]+","+kod[2])
		out_file.write("\n")
		out_file.write("1")
		out_file.write("\n")
		out_file.write("0")
		out_file.write("\n")

	else:
		out_file.write('Fali kod za '+kod[4])
		out_file.write("\n")

in_file.close()
out_file.close()
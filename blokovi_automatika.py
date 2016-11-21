import re

in_file = open(input("ulazna datoteka? "),"r")

out_file = open("blokovi_"+in_file.name, "w")

rjecnik2 = {
	'C' : '', #cesta
	'RUB' : '', #rubnjak
	'RUBNJAK' : '', #rubnjak
	'RUBKOB' : '', #rubnjak, spojiti na kraj objekta
	'GRAG' : '', #graba gore
	'GRAD' : '', #graba dolje
	'CIJEVD' : '', #dno cijevi
	'V' : '', #visina
	'CM' : '', #cesta makadam
	'SEPT' : '', #septicka jama
	'RUBK' : '', #kraj rubnjaka
	'KANALICA' : '', #kanalica
	'SLB' : '' ,#vidjeti sto je to
	'CM' : '', #cesta makadam
	'V' : '', #visina
	'ULAZ' : '', #ulaz
	'OTOK' : '', #otok na cesti
	'TRAFO' : '', #trafostanica
	'GRABA' : '', #graba
	'CA_CM' : '',#cesta asfalt-makadam
	'CA_NOVI' : '', #cesta nova
	'OBJ' : '', #objekt
	'PROPUST' :'', #propust
	'VIS' : '', #visina
	'CA' : '', #cesta asfalt
	'PUT' : '', #put
	'CM_CA' :'', #cesta makadam/asfalt
	'PARKING' : '', #parking
	'PSOPUST' : '', #propust
	'CA_ULAZ' : '', #asfaltirana cesta, ulaz
	'CA_' : '', #cesta asfalt
	'MOST' : '', #most
	'STERNJA' : '', #sternja
	'CM_ULAZ' : '', #cesta makadam, ulaz
	'TEMELJ' : '', #temelj
	'GRA' : '', #graba
	'SAHT_L' :'', #lomna tocka sahta, ubaciti ako treba na sredinu spoja blok
	'PRUGA' : '',#pruga
	'TRACNICE' : '', #tracnice
	'OBJEKT' : '',#objekt
	'PK' : '', #pruzni kamen
	'RAMPA' : '', #rampa
	'OBRADA-MOST' : '', #most-ograda
	'CA-OBRADA-MOST' : '', #cesta asfalt, obrada most
	'VODE' : '', #pojas voda
	'KORIDOR' : '', #koridor ceste
	'STEPENICE' : '', #stepenice
	'BUNAR' : '', #bunar
	'CA-MOST' : '', #most
	'NOGOSTUP' : '', #nogostup
	'GRABA_' : '',  #graba
	'OBROV' : '', #obrov, mozda je meda
	'POTHOD' : '', #pothodnik
	'POTHODNIK' : '', #pothodnik
	'PT' : '', #poligonska tocka
	'STUPICbeton' : '' #betonski stupic, staviti u kodove, ako bude trebalo


	
}

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
'ODRV' :'30507A-1',
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
'HIDRANT' : '40904B-1', #hidrant na povrsini
'HIDRANT_OKNO' : '40905-1',
'HID' : '40904B-1', #hidrant na povrsini
'STTDR' : '41113-1',
'STTELDR' : '41113-1',
'STTD' : '41113-1',
'SHT' : '41119B-1',
'SAHT' : '41302B-1', #saht-nije definirana vrsta, reviziono okno-simobl
'OKNO_TEL' : '41119B-1',
'TEL_OKNO' : '41119B-1',
'SLV' : '41301-1',
'SLIVNIK' : '41301-1',
'SLIV' : '41301-1',
'SLVNIK' : '41301-1',
'REVIZIONO_OKNO' : '41302B-1',
'TALOZNICA' : '41303B-1',
'DB' : '60118-1', #drvo bjelogorica
'DC' : '60119-1', #drvo crnogorica
'OZIV' : '60124A-1', #zivica
'ZIV' : '60124A-1',
'ZIVICA' : '60124A-1',
'MEDA' : '90501-1',
'MEDJA' : '90501-1',
'ZHDO' : '40901-1', #zatvarac voda
'OZICKOB' : '30508A-1', #zicana ograda, spojiti na kraj objekta
'VODAZ' : '40901-1', #zatvarac voda
'SDTEL' :'41113-1',#drveni telefonski stup
'ZELJ_STUP' : '40204A-1', #zeljezni telefonski stup
'OB_OZELJ' : '30509A-1', #ograda betonsko-zeljezna, ubacuje se zeljezna
'SBSTL' : '40203-1', #stup betonski, struja lampa, ubacuje se betonski stup struje
'OBODRV' : '30507A-1', #ograda betonsko drvena?, ubacuje se drvena ograda
'SAHT_K' : '41302B-1', #saht kanalizacija, ubacuje se reviziono okno
'OBOZELJ' : '30509A-1', #ograda betonsko zeljezno
'ORMARIC' : '41102-1', #kabelski razdjelnik u samostojecom ormaricu (struja)
'ZID_NASIP' : '30504A-1', # zid-nasip
'ZID_NASIP_ULAZ' : '30504A-1', # zid-nasip-ulaz
'OZELJ_ULAZ' : '30509A-1', #zeljezna ograda
'VODA_Z' : '40901-1', #zatvarac za vodu
'OB' : '30504A-1', #ograda betonska
'OBOZLJ' : '30509A-1', #ograda betonsko-zeljezna, stavljen simbol zeljezne
'SZSTL' : '40204A-1', #stup zeljezni struja lampa, ubacuje se zeljezni stup struje
'OZIV_ULAZ' : '60124A-1', #zivica na ulazu
'SDSTL' : '40202-1', #stup drveni struja lampa, ubacuje se drveni stup struje
'OBOZIC' : '30508A-1', #ograda betonsko zicana, ubacuje se zicana
'V_ZAT' : '40901-1', #zatvarac voda
'OZIC_ULAZ' : '30508A-1', #zicana ograda ulaz
'SEMOFOR' : '40208-1', #semafor
'SZP' : '40204B-1', #stup zeljezni uz prugu
'OBOD' : '30507A-1', #betonska-drvena ograda, ubacuje se drvena ograda
'OR-STRUJA' : '41102-1', #ormaric struja
'OZIVICA' : '60124A-1', #zivica
'SBSTL-OBZELJ' : '40203-1', #stup betonski struja-lampa uz zeljezno betonsku ogradu, #ubacuje se betonski stup struje
'SDRODE' : '40202-1', #stup drveni struja
'ULAZ-OZELJ' : '30509A-1', #zeljezna ograda na ulazu
'0ZIC' : '30508A-1', #zicana ograda
'ULAZ-ZID' : '30504A-1', #zid
'ULAZ-ODRV' : '30507A-1', #drvena ograda
'SAHT-TEL' : '41119B-1', #saht telefon
'OZIC-ULAZ' : '30508A-1', #zicana ograda na ulazu
'ELBET' : '40203-1', #stup betonski struja
'ELDRV' : '40202-1' #stup drveni struja

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

	elif kod[4] in rjecnik2:
		pass

	else:
		out_file.write('Fali kod za '+kod[4])
		out_file.write("\n")

in_file.close()
out_file.close()
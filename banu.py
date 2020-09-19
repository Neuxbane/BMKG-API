import requests

for x in range(100):
	print("")
print("")
print("---< Meminta data pada BMKG >---")
print("")

htmltext = "Error, Tidak Bisa Memukan Url yang di cari"
try:
	url = requests.get("https://data.bmkg.go.id/datamkg/MEWS/DigitalForecast/DigitalForecast-DIYogyakarta.xml")
	htmltext = url.text
	url = requests.get("https://data.bmkg.go.id/autogempa.xml")
	htmltext2 = url.text
except:
	print("/!\	Error Can't find BMKG Data Cuaca")
	print("---< Ada Masalah Ketika Meminta Data Cuaca BMKG di DI Yogyakarta >---")
	print("/!\	Coba:")
	print("/!\		-Pastikan Internet Terhubung")

else:
	print("")
	print("---< Data di terima >---")
	print("")

	print("")
	print("---< Membuka Data dari BMKG di DI Yogyakarta >---")
	print("")

	print("")
	print("---| Info Waktu |---")
	print("")
	print(htmltext[htmltext.find("<timestamp>"):htmltext.find("</timestamp>")].replace("<timestamp>", "Waktu terdeteksi "))
	print(htmltext[htmltext.find("<year>"):htmltext.find("</year>")].replace("<year>", "tahun "))
	print(htmltext[htmltext.find("<day>"):htmltext.find("</day>")].replace("<day>", "hari "))
	print(htmltext[htmltext.find("<minute>"):htmltext.find("</minute>")].replace("<minute>", "menit "))
	print(htmltext[htmltext.find("<second>"):htmltext.find("</second>")].replace("<second>", "detik "))
	print("")
	print("---| BMKG ->X<- Banu - [Menu Kabupaten] |---")
	print("")
	kabdat = htmltext
	listkabupaten = []
	for x in range(len(htmltext)):
		if len(kabdat) == 0:
			break	
		kabdat = kabdat[kabdat.find('<name xml:lang="id_ID">'):len(kabdat)]
		listkabupaten.append(kabdat[kabdat.find('<name xml:lang="id_ID">'):kabdat.find("</name>")].replace('<name xml:lang="id_ID">', ""))
		kabdat = kabdat[kabdat.find("</name>")+7:len(kabdat)]
	del listkabupaten[len(listkabupaten)-1]
	c = 0
	for x in listkabupaten:
		print(x + "	< " + str(c))
		c += 1
	print("")
	print("---| BMKG ->X<- Banu - [Menu Kabupaten] |---")
	print("")

	print("Silahkan dipilih nama Kabupatennya dan ketik nomornya saja")
	print("Antara 0 sampai " + str(len(listkabupaten)-1))
	print("")
	try:
		Kabupaten = listkabupaten[int(input('>nomor>'))]
		for x in range(100):
			print("")
		print("")
		print("---| Info Waktu |---")
		print("")
		print(htmltext[htmltext.find("<timestamp>"):htmltext.find("</timestamp>")].replace("<timestamp>", "Waktu terdeteksi "))
		print(htmltext[htmltext.find("<year>"):htmltext.find("</year>")].replace("<year>", "tahun "))
		print(htmltext[htmltext.find("<day>"):htmltext.find("</day>")].replace("<day>", "hari "))
		print(htmltext[htmltext.find("<minute>"):htmltext.find("</minute>")].replace("<minute>", "menit "))
		print(htmltext[htmltext.find("<second>"):htmltext.find("</second>")].replace("<second>", "detik "))
		htmltext = htmltext[htmltext.find('<name xml:lang="id_ID">' + Kabupaten):htmltext[htmltext.find('<name xml:lang="id_ID">' + Kabupaten):len(htmltext)].find("</area>")+htmltext.find('<name xml:lang="id_ID">' + Kabupaten)]
		while True:
			print("------Info Gempa|>-")
			print("-<|	" + htmltext2[htmltext2.find("<Tanggal>"):htmltext2.find("</Tanggal>")].replace('<Tanggal>', "Tanggal ").replace('-', " "))
			print("-<|	" + htmltext2[htmltext2.find("<Jam>"):htmltext2.find("</Jam>")].replace('<Jam>', "Pukul "))
			print("-<|	" + htmltext2[htmltext2.find("<Magnitude>"):htmltext2.find("</Magnitude>")].replace('<Magnitude>', "Magnitude "))
			print("-<|	" + htmltext2[htmltext2.find("<Kedalaman>"):htmltext2.find("</Kedalaman>")].replace('<Kedalaman>', "Kedalaman "))
			print("-<|	" + htmltext2[htmltext2.find("<Potensi>"):htmltext2.find("</Potensi>")].replace('<Potensi>', ""))
			print("----------------|>-")
			print("")
			print("---<|> BMKG ->X<- Banu - [" + Kabupaten + "] <|>---")
			print("")
			print("-|	Info Suhu            " + Kabupaten + "	<0")
			print("-|	Info Kelembapan      " + Kabupaten + "	<1")
			print("-|	Info Cuaca           " + Kabupaten + "	<2")
			print("-|	Info Arah Angin      " + Kabupaten + "	<3")
			print("-|	Info Kecepatan Angin " + Kabupaten + "	<4")
			print("")
			print("Silahkan dipilih dan ketik nomornya saja")
			print("Antara 0 sampai 4")
			print("")
			Input = int(input('>nomor>'))
			try:
				if Input == 0:
					print("----------------|>-")
					print("---<| Info Suhu |>-")
					print("----------------|>-")
					data = str(htmltext[htmltext.find('parameter id="t" description="Temperature" type="hourly">'):htmltext.find('parameter id="t" description="Temperature" type="hourly">')+htmltext[htmltext.find('parameter id="t" description="Temperature" type="hourly">'):len(htmltext)].find("</parameter>")])
					print("")
					print(data.replace('parameter id="t" description="Temperature" type="hourly">', "			Suhu Dalam Urutan jam mulai dari sekarang sampai +66 jam").replace('<timerange type="hourly" h="', "Dalam +").replace('" datetime=', " Jam , Waktu ").replace('"', "").replace('>', "").replace('</timerange', "").replace('<value unit=C', "*C ").replace('<value unit=F', "*F ").replace('</value', ""))
				if Input == 1:
					print("----------------------|>-")
					print("---<| Info Kelembapan |>-")
					print("----------------------|>-")
					data = str(htmltext[htmltext.find('<parameter id="hu" description="Humidity" type="hourly">'):htmltext.find('<parameter id="hu" description="Humidity" type="hourly">')+htmltext[htmltext.find('<parameter id="hu" description="Humidity" type="hourly">'):len(htmltext)].find("</parameter>")])
					print("")
					print(data.replace('<timerange type="hourly" h="', "Dalam +").replace('" datetime=', " Jam , Waktu ").replace('"', "").replace('>', "").replace('<parameter id=hu description=Humidity type=hourly', "			Kelembapan Dalam Urutan jam mulai dari sekarang sampai +66 jam").replace('<value unit=', "Kelembapan ").replace('</value', "").replace('</timerange', ""))
				if Input == 2:
					print("-----------------|>-")
					print("---<| Info Cuaca |>-")
					print("-----------------|>-")
					data = str(htmltext[htmltext.find('<parameter id="weather" description="Weather" type="hourly">'):htmltext.find('<parameter id="weather" description="Weather" type="hourly">')+htmltext[htmltext.find('<parameter id="weather" description="Weather" type="hourly">'):len(htmltext)].find("</parameter>")])
					print("")
					print(data.replace('<timerange type="hourly" h="', "Dalam +").replace('" datetime=', " Jam , Waktu ").replace('"', "").replace('>', "").replace('<parameter id="weather" description="Weather" type="hourly">', "			Cuaca Dalam Urutan jam mulai dari sekarang sampai +66 jam").replace('<value unit=', "Cuaca ").replace('</value', "").replace('</timerange', ""))
				if Input == 3:
					print("----------------------|>-")
					print("---<| Info Arah Angin |>-")
					print("----------------------|>-")
					data = str(htmltext[htmltext.find('<parameter id="wd" description="Wind direction" type="hourly">'):htmltext.find('<parameter id="wd" description="Wind direction" type="hourly">')+htmltext[htmltext.find('<parameter id="wd" description="Wind direction" type="hourly">'):len(htmltext)].find("</parameter>")])
					print("")
					print(data)
				if Input == 4:
					print("---------------------------|>-")
					print("---<| Info Kecepatan Angin |>-")
					print("---------------------------|>-")
					data = str(htmltext[htmltext.find('<parameter id="ws" description="Wind speed" type="hourly">'):htmltext.find('<parameter id="ws" description="Wind speed" type="hourly">')+htmltext[htmltext.find('<parameter id="ws" description="Wind speed" type="hourly">'):len(htmltext)].find("</parameter>")])
					print("")
					print(data)




			except:
				for x in range(100):
					print("")
				print("Mohon Maaf Nomor Tidak Falid")



	except:
		for x in range(100):
			print("")
		print("Mohon Maaf Nomor Tidak Falid")
	
print("")
print("---| Badan Meteorologi, Klimatologi, dan Geofisika |---")
print("")
print("		-| > python ->X<- Banu < |-")
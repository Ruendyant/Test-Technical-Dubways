def gabung(pertama, kedua):
	list_per = []
	list_ked = []
	kata_gabung = ""
	if len(pertama) != len(kedua):
		print("huruf pada Kata pertama dan kedua tidak berjumlah sama")
		return None
	else:
		for p in pertama:
			list_per.append(p)
		for p in kedua:
			list_ked.append(p)
		for n in range(0,len(list_per)):
			kata_gabung += list_per[n] + list_ked[n]



		print(kata_gabung)

pert = input("Masukan Kata pertama : ")
ked = input("Masukan Kata kedua : ")
gabung(pert,ked)

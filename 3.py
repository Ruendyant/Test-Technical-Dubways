def gambar(num):
	center = (num-1)/2
	if num % 2 == 0:
		return None
	else:

		for i in range(0,num):
			for j in range(0,num):
				if(((i % 2 == 0) and (j == center) or ((i % 2 == 1) and (j % 2 == 1)))):
					print("= ", end="")
					continue
				print("* ", end="")
			print()

gambar(5)
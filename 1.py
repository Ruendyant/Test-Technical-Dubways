def bin_hex():
	b_num = list(input("Input a binary number: "))
	value = 0

	for i in range(len(b_num)):
		digit = b_num.pop()
		if digit == '1':
			value = value + pow(2, i)
	#return value

	result = ['0'] * 1000
	i = 0
	while value != 0:
		temp = value % 16

		if temp < 10:
			result[i] = chr(temp + 48)
			i += 1
		else:
			result[i] = chr(temp + 55)
			i += 1
		value = int(value / 16)
	j = i - 1
	while j >= 0:
		print(result[j])
		j -= 1
	#return result

bin_hex()
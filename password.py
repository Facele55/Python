import random as ran


def gen_pass(n: int):
	str1 = ""
	for i in range(0, n, 2):
		c = ran.choice(list("abcdefghijklmnopqrstuvwx@#$%^&*€£¥1234567890yzABCDEFGHIJKLMNOPQRSTUVWXYZ"))
		str1 += c
		if i != n - 1:
			b = ran.choice(list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@#$&€£*¥1234567890"))
			str1 += b
	return str1


if __name__ == "__main__":
	lent = int(input("Enter the length of password : "))
	print("Your password is: ", gen_pass(n=lent))

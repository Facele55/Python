def get_sign(month: int, day: int):
	if month == 12:
		astro_sign = 'Sagittarius' if (day < 22) else 'Capricorn'
		return astro_sign
	elif month == 1:
		astro_sign = 'Capricorn' if (day < 20) else 'Aquarius'
		return astro_sign
	elif month == 2:
		astro_sign = 'Aquarius' if (day < 19) else 'Pisces'
		return astro_sign
	elif month == 3:
		astro_sign = 'Pisces' if (day < 21) else 'Aries'
		return astro_sign
	elif month == 4:
		astro_sign = 'Aries' if (day < 20) else 'Taurus'
		return astro_sign
	elif month == 5:
		astro_sign = 'Taurus' if (day < 21) else 'Gemini'
		return astro_sign
	elif month == 6:
		astro_sign = 'Gemini' if (day < 21) else 'Cancer'
		return astro_sign
	elif month == 7:
		astro_sign = 'Cancer' if (day < 23) else 'Leo'
		return astro_sign
	elif month == 8:
		astro_sign = 'Leo' if (day < 23) else 'Virgo'
		return astro_sign
	elif month == 9:
		astro_sign = 'Virgo' if (day < 23) else 'Libra'
		return astro_sign
	elif month == 10:
		astro_sign = 'Libra' if (day < 23) else 'Scorpio'
		return astro_sign
	elif month == 11:
		astro_sign = 'Scorpio' if (day < 22) else 'Sagittarius'
		return astro_sign
	else:
		error = "Wrong input data"
		return error


if __name__ == "__main__":
	d = int(input("Input day of birthday: "))
	m = int(input("Input month of birth: "))
	print("Your Astrological sign is :", get_sign(month=m, day=d))

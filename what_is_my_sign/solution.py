def what_is_my_sign(day, month):
	if (day>31 or day<1 or month>12 or month<1):
		return "Date not correct!"
	else:
		if ( (day>20 and month==3) or (day<21 and month==4) ):
			return "Aries"
		elif ( (day>20 and month==4) or (day<22 and month==5) ):
			return "Taurus"
		elif ( (day>21 and month==5) or (day<22 and month==6) ):
			return "Gemini"
		elif ( (day>21 and month==6) or (day<23 and month==7) ):
			return "Cancer"
		elif ( (day>22 and month==7) or (day<23 and month==8) ):
			return "Leo"
		elif ( (day>22 and month==8) or (day<24 and month==9) ):
			return "Virgo"
		elif ( (day>23 and month==9) or (day<24 and month==10) ):
			return "Libra"
		elif ( (day>23 and month==10) or (day<23 and month==11) ):
			return "Scorpio"
		elif ( (day>22 and month==11) or (day<22 and month==12) ):
			return "Sagittarius"
		elif ( (day>21 and month==12) or (day<21 and month==1) ):
			return "Capricorn"
		elif ( (day>20 and month==1) or (day<20 and month==2) ):
			return "Aquarius"
		elif ( (day>19 and month==2) or (day<21 and month==3) ):
			return "Pisces"
		else:
			return "ERROR!"

def main():
	print ( what_is_my_sign(5, 8) )
	print ( what_is_my_sign(29, 1) )
	print ( what_is_my_sign(30, 6) )
	print ( what_is_my_sign(31, 5) )
	print ( what_is_my_sign(2, 2) )
	print ( what_is_my_sign(8, 5) )
	print ( what_is_my_sign(9, 1) )
if __name__ == '__main__':
	main()
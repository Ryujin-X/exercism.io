def sum_of_multiples(number, factors=[3, 5]):
	return sum({(multiple * factor) for multiple in range(number) for factor in factors if (multiple * factor) < number})
	
	
	


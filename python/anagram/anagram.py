from collections import Counter


def detect_anagrams(string, words_list):
    return [word for word in words_list if word.lower() != string.lower() and Counter(word.lower()) == Counter(string.lower())]



		
		
			
		
		
				
				
	

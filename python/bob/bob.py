def hey(what):
	sentence = what.strip()
	if not sentence:
		#nothing
		reply = "Fine. Be that way!"
	elif sentence.isupper():
		#shout
		reply = "Whoa, chill out!"
	elif sentence.endswith('?'):
		#question
		reply = "Sure."
	else:
		#normal
		reply = "Whatever."
	return reply

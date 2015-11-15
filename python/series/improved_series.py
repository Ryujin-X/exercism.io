# Take a sequence of digits from a a string and list every possible sequence up to n length

def slices(string, sequence):

    digit_list = [int(digit) for digit in string]
    output_list = []

    #step = 0
    #while step < sequence - 1:
        #end = 1 + step
    if sequence > len(string):
        raise ValueError("Error: The sequence is larger than the string!")
    
    if sequence == 0:
        raise ValueError("Error: The sequence must be a value larger than zero!")
   		
    end = sequence
    start = 0
    
    while end <= len(digit_list):
            #print(digit_list[start:end])
        output_list.append(digit_list[start:end])
        start += 1
        end += 1
        #else:
            #step += 1
                
    return output_list

#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    
    convertor = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    
    for i in range(len(roman_string)):
        current_value = convertor[roman_string[i]]
        
        if i < len(roman_string) - 1:
            next_value = convertor[roman_string[i + 1]]
            
            if current_value < next_value:
                total -= current_value
            else:
                total += current_value
        else:
            total += current_value
    
    return total

    
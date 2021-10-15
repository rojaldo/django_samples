myString = "Hello World"

def count_character(myString, character):
    count = 0
    if type(myString) == str and type(character) == str and len(character) == 1 and len(myString) > 0:
        for char in myString:
            if char == character:
                count += 1
        return count

print(count_character(True, 'hola'))
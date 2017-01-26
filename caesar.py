def alphabet_position(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter.lower()
    char_pos = alphabet.find(char)
    return char_pos

def rotate_character(car, rot):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if car.lower() == car:
        car_pos = alphabet.find(car)
        new_pos = car_pos + rot
        if new_pos > 26:
            new_pos = new_pos % len(alphabet)
            car = alphabet[new_pos]
        else:
            new_pos = new_pos % len(alphabet)
            car = alphabet[new_pos]
    if car.upper() == car:
        car_pos = ALPHABET.find(car)
        new_pos = car_pos + rot
        if new_pos > 26:
            new_pos = new_pos % len(ALPHABET)
            car = ALPHABET[new_pos]
        else:
            new_pos = new_pos % len(ALPHABET)
            car = ALPHABET[new_pos]
    else:
        car = car
    return car

def encrypt(text, rot):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    newtext = ''

    for car in text:
        if car == ' ':
            newtext = newtext + ' '
        elif car.lower() == car:
            if alphabet.find(car) == -1:
                newtext = newtext + car
            else:
                car = rotate_character(car, rot)
                newtext = newtext + car
        elif car.upper() == car:
            if ALPHABET.find(car) == -1:
                newtext = newtext + car
            else:
                car = rotate_character(car, rot)
                newtext = newtext + car
    return newtext

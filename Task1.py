sound = 10

if __name__ == '__main__':
    if (sound <= 39):
        print("The sound effect is Faint")
    elif (sound <= 69):
        print("The sound effect is Moderate")
    elif (sound <= 99):
        print("The sound effect is Very Loud")
    elif (sound <= 129):
        print("The sound effect is Extremely Loud")
    else:
        print("The sound effect is Painful")

wave = 400

if __name__ == '__main__':
    if 380 <= wave <= 449:
        print("Violet")
    elif 450 <= wave <= 494:
        print("Blue")
    elif 495 <= wave <= 569:
        print("Green")
    elif 570 <= wave <= 589:
        print("Yellow")
    elif 590 <= wave <= 619:
        print("Orange")
    elif 620 <= wave <= 750:
        print("Red")
    else:
        print("Invisible Light")


def crackiterable(start=1, end=100):
    try:
        totalcount = 0
        cracklepopcount = 0
        snapcount = 0
        cracklecount = 0
        for number in range(start, (end+1)):
            totalcount += 1
            if number % 3 == 0 and number % 5 == 0:
                print("{0} - Cracklepop!\n").format(number)
                cracklepopcount += 1
            elif number % 3 == 0 and not number % 5 == 0:
                print("{0} - Snap!\n").format(number)
                snapcount += 1
            elif number % 5 == 0 and not number % 3 == 0:
                print("{0} - Crackle!\n").format(number)
                cracklecount += 1
            else:
                print("{0}\n").format(number)
        print("""
        In the range from {0} to {1}, there were:
        {2} Snaps, {3} Crackles, and {4} Cracklepops""").format(
        start, end, snapcount, cracklecount, cracklepopcount)

    except TypeError:
        print("You've not provided an integer for start and end length")
        raise
    except:
        print("Unexpected error!")
        raise


crackiterable()
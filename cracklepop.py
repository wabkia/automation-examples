
from sys import argv as argv

# attempt to set command line arguments as start and end values
try:
    start = int(argv[1])
    end = int(argv[2])
except:
    print("There is a problem with the supplied arguments")
raise

# determine the direction of the count
def stepdirection(start, end):
    if start > end:
        end -= 1
        step = -1
    else:
        end += 1
        step = 1
    return start, end, step


# generate list using default values or supplied arguments
# then iterate over the list, checking for snap, crackle,
# and cracklepop conditions.
def crackiterable(start=-1, end=-100):
    try:
        totalcount = 0
        cracklepopcount = 0
        snapcount = 0
        cracklecount = 0
        for number in range(*stepdirection(start, end)):
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

# if called from the command line, attempt to use arguments
# and if no arguments exist call function with defaults
if __name__ == "__main__":
    if 'start' in globals() and 'end' in globals():
        crackiterable(start, end)
    else:
        crackiterable()





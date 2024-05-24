# Foo Bar Buzz!

i = 0
while i is not 'bla':
    i += 1
    if (i % 5) == 0:
        print(f"Buzz {i}")
        print(i)
        continue
    match (i % 2):
        case 1:
            print(f"Hey look it works {i}")
            continue
        case 0:
            print(f"The even number works {i}")
            continue
        case _:
            print("The match statement was confused by the input")
            exit()

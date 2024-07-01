# Class practice


class Dummy:
	def __init__(self, name):
		self.name = name
		self.dummyness = 1
	def more_dummy(self):
		self.dummyness += 1
	def less_dummy(self):
		self.dummyness -= 1


names = []
 
 
for x in range(5):
    n = "dummy_" + str(x)
    names.append(n)
    names[x] = Dummy(n)


while True:
    print("")
    print("Who has becometh your target?")
    print(range(5))
    target = str(input())
    if target not in "01234":
        print("Type an integer between 0 and 4 inclusive")
        exit()
    target = int(target)
    print("")
    print(f"Is dummy_{target} more or less dummy?")
    morl = input()
    match morl:
        case "more":
            names[target].more_dummy()
            print(names[target].dummyness)
        case "less":
            names[target].less_dummy()
            print(names[target].dummyness)
    print("")
    print("Wanna do more? Y/N")
    domore = input()
    if domore != "Y":
        print(f"Given you typed {domore}, this program ends now")
        exit()





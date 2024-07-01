# Contact manager
# Planned storage method: .json, current .txt
# Cannot currently handle duplicate names. It is planned to add a unique identifier

# This imports nets a big dict that I use to clean up a lot of inputcleaning
from badinput import badinputfunc

contactfile = open("C:\\Users\\Jouke Rodenhuis\\Github\\itvitae\\contactfile.txt")
stuff = contactfile.readlines()
contactfile.close()

namelist = []


class contactexistensie:
    def __init__(self, name, email, telnum, addr):
        self.name = name
        self.email = [email]
        self.telnum = [telnum]
        self.addr = [addr]
        
    def appender(self, which, stuff):
        match which:
            case 'email':
                self.email.append(stuff)
            case 'telnum':
                self.telnum.append(stuff)
            case 'addr':
                self.addr.append(stuff)

def inputcleaner(uinput, which, namelist):
    inputcleandict = badinputfunc()
    match which:
            case 'email':
                generic = f'Please input the {which} again'
                while True:
                    match uinput:
                        case uinput if '@' not in uinput:
                            print(f'The mail address you provided does not contain an \'@\'. {generic}')
                            uinput = input()
                            continue
                        case uinput if '.' not in uinput:
                            print(f'The mail address you provided does not contain a \'.\'. {generic}')
                            uinput = input()
                            continue
                        case uinput if uinput.count('@') >= 2:
                            print(f'The mail address you provided contains two or more \'@\' characters. {generic}')
                            uinput = input()
                            continue
                        case uinput if uinput.count('.') >= 2:
                            print(f'The mail address you provided contains two or more \'.\'s. {generic}')
                            uinput = input()
                            continue
                        case uinput if uinput[0] in '@.':
                            print(f'The mail address needs characters before the {uinput[0]}. {generic}')
                            uinput = input()
                            continue
                        case uinput if uinput[len(uinput) - 1] in '@.':
                            print(f'The mail address needs characters after the {uinput[len(uinput) - 1]}. {generic}')
                            uinput = input()
                            continue
                        case _:
                            return uinput
            case 'telnum':
                while True:
                    add = 0
                    space = 0
                    invalid = 0
                    for element in uinput:
                        if not element.isnumeric:
                            match element:
                                case element if element == '+' and add == 1:
                                    print(f'The telephone number contains two or more \'{element}\'. {generic}')
                                    uinput = input()
                                    invalid = 1
                                    break
                                case element if element == '+' and add == 0:
                                    add = 1
                                    continue
                                case element if element == ' ' and space == 1:
                                    print(f'The telephone number contains two or more \'{element}\'. {generic}')
                                    uinput = input()
                                    invalid = 1
                                    break
                                case element if element == ' ' and space == 0:
                                    space = 1
                                    continue
                                case _:
                                    print(f'The telnum contains {element}, which is invalid. {generic}')
                                    uinput = input()
                                    invalid = 1
                                    break
                    match invalid:
                        case 0:
                            return uinput
                        case _:
                            continue
            case 'addr':
                return uinput
            
            case 'modname':
                generic = 'please try again until it matches only one entry'
                while True:
                    k = 0
                    foundlist = []
                    for name in namelist:
                        if uinput.lower() in name.lower():
                            k += 1
                            foundlist.append(name)
                    
                    displayfound = ''
                    for element in foundlist:
                        match len(displayfound):
                            case 0:
                                displayfound = element
                            case _:
                                displayfound += f', {element}'
                    if k == 0:
                        print(f'This program could not match your input within the existing database, {generic}')
                        uinput = input()
                    if k == 1:
                        break
                    if k >= 2:
                        print(f'Your input matches the following entries: {displayfound}, {generic}')
                        uinput = input()
                        k = 0
                        continue
                return uinput, displayfound
            
            case 'whatmod':
                badchoicelist = inputcleandict['whatmod']['bad']
                whatprintlist = inputcleandict['whatmod']['string']
                while True:
                    invalid = 0
                    for index,element in enumerate(badchoicelist):
                        if uinput in element:
                            print(whatprintlist[index])
                            invalid = 1
                            uinput = input()
                            break
                    if invalid == 0:
                        break
                match uinput:
                    case uinput if uinput.lower() in 'name':
                        pass
                    case uinput if uinput.lower() in 'email':
                        pass
                    case uinput if uinput.lower() in 'telephone numbertelnumtelephonenumber':
                        pass
                    case uinput if uinput.lower() in 'address':
                        pass
            
            case 'choice':
                choice = uinput
                
                badchoicelist = inputcleandict['choice']['bad']
                whatprintlist = inputcleandict['choice']['string']
                while True:
                    invalid = 0
                    for index,element in enumerate(badchoicelist):
                        if uinput in element:
                            print(whatprintlist[index])
                            invalid = 1
                            uinput = input()
                            break
                    if invalid == 0:
                        break    
                
                match choice:
                    case choice if choice in 'list':
                        print(f'You typed \'{choice}\', which this program interprets as \'list\'')
                        contactlist = lister()
                    case choice if choice in 'update':
                        contactlist = updater()
                    case choice if choice in 'remove':
                        print('This program is too dumb to remove ANY contact for you!')
                return contactlist, choice


def lister():
    contactlist = []
    for line in stuff:
        line = line.strip()
        thing = line.split(', ')
        k = 0
        p1 = contactexistensie(thing[0],thing[1],thing[2],thing[3])
        for index,data in enumerate(thing):
            if index < 4:
                continue
            match data:
                case data if '@' in data:
                    p1.appender('email', data)
                    continue
                case data if data[0] in '+1234567890':
                    p1.appender('telnum', data)
                    continue
                case data if k == 0:
                    p1.appender('addr', data)
                    continue
        contactlist.append(p1)
    return contactlist


def modifier():
    print('Which contact do you want to modify? See the list below to choose. ')
    for contact in contactlist:
        print(contact.name)
        namelist.append(contact.name)
    uinput = input()
    uinput, displayfound = inputcleaner(uinput, 'modname', namelist)
    print(f'What information of {displayfound} do you want to change?')
    uinput = input()
    

def updater():
    
    contactlist = lister()
    print('Do you want to modify a contact, or create a new one?')
    choice = input()
    
    match choice:
        case choice if choice in 'modify':
            pass
        case choice if choice in 'create':
            
            print('What is the name of your new contact?')
            ncname = input()
            
            while True:
                print('Please input 1 or 0 email addresses')
                ncemail = input()
                ncemail = inputcleaner(ncemail, 'email', namelist)
                break
            while True:
                print('Please input 1 or 0 telephone numbers')
                nctelnum = input()
                nctelnum = inputcleaner(nctelnum, 'telnum', namelist)
                break
            
            print('Please input 1 or 0 addresses')
            ncaddress = input()
            p1 = contactexistensie(ncname,ncemail,nctelnum,ncaddress)
        case _:
            print('Your input was unclear and in this edge case the programmer was too lazy at time of writing. BYE!')
            exit()
            
            
            while True:
                print('Does this person have any additional emails, telephone numbers, or addresses?')
                print('This process will end if you type \'No\'')
                choice = input()
                match choice.lower():
                    case 'no':
                        break
                    case choice if choice == 'e' or choice == 's':
                        print(f'Your input is unclear.')
                        continue
                    case choice if choice == 'a':
                        print(f'{choice} could refer to either emails or addresses, please specify')
                        continue
                    case choice if choice == 'r':
                        print(f'{choice} could refer to either telephone numbers or addresses, please specify')
                        continue
                    case choice if choice in 'emails':
                        print('Please input the email you wish to add')
                        mail = input()
                        mail = inputcleaner(mail, 'email', namelist)
                        p1.appender('email', mail)
                    case choice if choice in 'telephone numbers':
                        print('Please input the telephone number you wish to add')
                        tel = input()
                        tel = inputcleaner(tel, 'telnum', namelist)
                        p1.appender('telnum', tel)
                    case choice if choice in 'address':
                        print('Please input the telephone number you wish to add')
                        address = input()
                        p1.appender('addr', address)
    contactlist.append(p1)
    return contactlist

print('What do you want to do? Choose from list, update, and remove')
choice = input()
contactlist, choice = inputcleaner(choice, 'choice', namelist)

while True:
    print('This is the current database after the last modification:')
    for contact in contactlist:
        print(contact.name, contact.email, contact.telnum, contact.addr)
    print('Do you want to do something else (y), or stop the program? (n) [y/n]')
    uinput = input()
    match uinput.lower():
        case 'y':
            print('What would you like to do?')
            uinput = input()
            contactlist, choice = inputcleaner(uinput, 'choice', namelist)
        case 'n':
            print('I will now resume my eternal slumber')
            exit()
        case _:
            print(f'Type either \'y\' or \'n\', you typed {uinput}')
            continue

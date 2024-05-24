#Script dat een lijst kan aannemen van een txt.file of hardcoded. Zet er e-mails in. Check of de emails correct zijn. Correct is tekst@hostname.domain. 

maillist = ["@tommy.dummy.com", "henkie@dummy.bonk", "tommy@dummy.com", "tommy", "tommy@dummy", "tommy@.dummy", "@.com", "@tommy.dummy.com", "?!@#$%^&*(.derp"]
maillist2 = ["@tommy.dummy.com"]




#The function below checks e-mails that have already been extracted from whatever data they were inside of. 

def EmailChecker():
    correctaddresses = []
    CorrectCharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz@.1234567890"
    for address in maillist:
    
        CheckMeter = 0
        FaultyAddress = 0
        IndexofAt = 0
        IndexofDot = 0
        length = len(address)
        
        for index,letter in enumerate(address):
        
            match letter:
            
                case letter if letter not in CorrectCharacters:
                    FaultyAddress = 1
            
                case letter if letter == "@" and index > 0 and CheckMeter == 0:
                    CheckMeter += 1
                    IndexofAt = index
                    
                case letter if letter == "@" and index > IndexofAt and CheckMeter > 0:
                    FaultyAddress = 1
                    
                case letter if letter == "." and index > IndexofAt + 1 and CheckMeter == 1:
                    CheckMeter += 1
                    IndexofDot = index
                    
                case letter if letter == "." and index > IndexofDot and CheckMeter == 2:
                    FaultyAddress = 1
                    
        if length > IndexofDot and FaultyAddress == 0 and CheckMeter == 2:
            correctaddresses.append(address)
            
    return correctaddresses

correctaddresses = EmailChecker()            
print(correctaddresses)
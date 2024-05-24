emails = [
	'larry@abc.nl',
	'barry@abc.de',
	'harry@abc.be',
	'larry@xyz.com',
	'barry@xyz.it',
    'HarHar@NoDotComForYou',
    'AbsoloteCounterCulture',
	]

RemovalString = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!#$%^&*-_=+\\\;\:\'\"?/><,`~\{\[\}\]\|)'
CurrentEmail = 0

for email in emails:
    if emails[CurrentEmail].rfind('.com') != -1:
        print('Wow, ' + emails[CurrentEmail] + ' is already correct!')
        CurrentEmail += 1
        continue
    if emails[CurrentEmail].rfind('@') == len(emails[CurrentEmail]) - 1 or emails[CurrentEmail].find('@') == -1:
        print('The address \'' + emails[CurrentEmail] +'\' either does not contain any characters after @ or has no @ at all and is therefore invalid.')
        CurrentEmail += 1
        continue
    if emails[CurrentEmail].rfind('.com') == -1 and emails[CurrentEmail].rfind('.') != -1:
        emails[CurrentEmail] = emails[CurrentEmail].rstrip(RemovalString)
        emails[CurrentEmail] = emails[CurrentEmail] + 'com'
        print('This is what the email ended up as: '+ emails[CurrentEmail])
        CurrentEmail += 1
        continue
    if emails[CurrentEmail].rfind('.') == -1:
        emails[CurrentEmail] = emails[CurrentEmail] + '.com'
        print('This is what the email ended up as: '+ emails[CurrentEmail])
        CurrentEmail += 1
        continue
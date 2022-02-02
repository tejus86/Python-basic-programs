weekdays = ['sun', 'mon', 'tues', 'wed', 'thurs', 'fri', 'sat']
listAsString = ' '.join(weekdays)
print(listAsString)

listAsTuple = tuple(weekdays)
print(listAsTuple)

listasSet = set(weekdays)
print(listasSet)

print(weekdays.count('mon'))

print([[x,weekdays.count(x)] for x in set(weekdays)])
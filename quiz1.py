def testgen(index):
    weekdays = ['sun', 'mon', 'tues', 'wed', 'thurs', 'fri', 'sat']
    yield weekdays[index]
    yield weekdays[index+1]
    day = testgen(0)

    print(next(day))
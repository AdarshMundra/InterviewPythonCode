def creating_gen(index):
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    yield months[index]
    yield months[index+2]
    yield months[index+5]
next_month = creating_gen(3)
# print(next_month)
print(next(next_month), next(next_month), next(next_month))
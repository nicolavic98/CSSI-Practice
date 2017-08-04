snax = {
    "fruit snacks" : 10,
    "apples" : 7,
    "chips" : 10,
    "soda" : 8,
    "cuties" : 10,
    "raisins" : 3,
}

print snax

#adding to dictionaries
snax["raisins"] = 2

for item in snax:
    print "%s get a %s out of 10" %(item, snax[item])

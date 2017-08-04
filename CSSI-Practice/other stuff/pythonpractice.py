###from random import randint

###def addition(number, number_2):
###    print number * "foobarbaz" * number_2
###addition(5, randint(0, 6))


#from random import randint

#tasks = ["clean my room", "go to the store", "walk the dog", "mow the lawn", "go to school", "study", "apply to college"]
#excuses = ["Lake Shore Drive was closed", "I got lost", "the Cubs won the World Series", "I have a Netflix account", "who does that anyway", "I was listening to Bohemian Rhapsody" ]
#time = ["tomorrow", "in three years", "sometime soon", "in the future", "when I feel like it"]

#print "I did not %s because %s. I will do it %s." % (tasks[randint(0,len(tasks) - 1)], excuses[randint(0, len(excuses) - 1)], time[randint(0,len(time) - 1)])

from random import randint

pizzatype = ["pepperoni", "cheese", "sausage", "hawaiian", "supreme", "three cheeses", "veggie"]

def pizzachoice():
    print "I want %s pizza." %(pizzatype[randint(0, len(pizzatype)-1)])
pizzachoice()

password_elements = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r"]

def choose_random(choices):
    return choices[randint(0, len(choices)-1)]
new_password = ""

for i in range(8):
    new_password = new_password +choose_random(password_elements)

print new_password

#groceries activity
groceries = ["apple", "banana", "eggs", "cheese", "milk", "bread"]

for i in range(len(groceries)):
    print i,
    print groceries[i]

def ShoppingList():
    print "List what you need to buy"
    groceries = []
    num = raw_input("How many groceries?: ")
    for i in range(int(num)):
        groceries.append(raw_input("Enter item: "))
    return groceries

grocery_list = ShoppingList();
for i in range(len(grocery_list)):
    print "%s. %s" % (i + 1, grocery_list[i]) 

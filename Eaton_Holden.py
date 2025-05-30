import random                       
foods = ['double bacon cheesburger','pizza', 'grilled chicken', 'hot dogs', 'pasta', 'beef tacos', 'chicken nuggies']       # list of foods 
costs = [20, 12, 23, 10, 15, 8, 9]                  # prices of food 
flairs = ['with truffle fries', 'with salad', 'with onions', 'with salsa', 'with ketchup', 'with cheese', 'with sour cream'] # condoments side of foods 
flair_costs = [12,8,6,4,2,3,2] 
num_of_items = int(input("how many do you need? ")) # ask the user for a number of items
total = 0

for i in range (num_of_items):                      # use for loops and num_of_items
    food = random.choice(foods)                     # randomly generate an item
    flair = random.choice(flairs)                   # randomly generate a flair 
    index = foods.index(food)                       # get the index of that item in food_items
    cost = costs[index]                             # find the corresponding cost using the index
    flair_index = flairs.index(flair)                    #flair_index
    flair_cost = flair_costs[flair_index]                             #flair_cost
    print (f'{food} {flair}, ${cost} + ${flair_cost} = ${cost + flair_cost}')               # print the food flair and cost
    total += cost + flair_cost                                    # add together to get total
print(total)                                          # print total cost






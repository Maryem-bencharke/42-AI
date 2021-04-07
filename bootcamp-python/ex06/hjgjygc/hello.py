cookbook={
    'sandwich':{'ingredients':{'ham','bread','cheese','tomatoes'},'meal':{'it is a lunch'},'prep_time':{'it takes 10 minutes of preparation'},},
    'cake':{'ingredients':{'flour','sugar','eggs'},'meal':{'it is a dessert'},'prep_time':{'takes 60min of preperation'}},
    'salad':{'ingredients':{'avocado','arugula','tomatoes','spinach'},'meal':{'it is a lunch'},'prep_time':{'takes 15min of preperation'}}
    }
def add_a_recipe(name_of_recipe, ingredients, meal , prep_time,cookbook):
    cookbook[name_of_recipe]={'ingredients':ingredients,'meal':meal,'prep_time':prep_time}    
    return
def del_recipe(name,cookbook):
    cookbook.pop(name)
    return
def print_a_recipe(name,cookbook):
    if name in list(cookbook.keys()):
        print("for {recipe}:\nIts ingredients are :{ingredients}\nIt is eaten as {meal}\nAnd needs {prep_time} min\n".format(recipe=name,ingredients=cookbook[name]['ingredients'],meal=cookbook[name]['meal'],prep_time=cookbook[name]['prep_time']))
        return
    if name not in list(cookbook.keys()):
        print("please enter a valid name.")
while True:
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")
    try:
        a=int(input())
    except ValueError:
        print("\nThis option does not exist, please type the corresponding number.\nTo exit , enter 5.")
    if a==1:
        print("add your recipe:")
        print("the name of your recipe:\n")
        name = str(input())
        print(name)
        print("the ingredients you need:\n")
        ingredients=[]
        i=1
        while i!=0:
            try:
                if str(i).isdigit():
                    ingredients.append(str(input("add what you want:")))
                    break
                if i==0:
                    break
            except ValueError:
                i=""
        print(ingredients)
        meal=str(input("the type of your meal:"))
        print(meal)
        while True:
            i=input("preperation time:")
            if str(i).isdigit():
                prep_time=int(i)
                break
        print(prep_time)
        add_a_recipe(name,ingredients,meal,prep_time,cookbook)
    elif a==2:
        print("you are deleting a recipe.")
        name=str(input("the name of the recipe to delate"))
        del_recipe(name,cookbook)
    elif a==3:
        print("choose a recipe:")
        name=str(input("the name of the recipe you want:"))
        print_a_recipe(name,cookbook)
    elif a==4:
         print("display a recipe:")
         keys=list(cookbook.keys)
         for i in range(len(cookbook)):
             print_a_recipe(keys[i],cookbook)
    elif a==5:
        print("cookbook closed")
        break
    else:
        print("does not exist.")

   

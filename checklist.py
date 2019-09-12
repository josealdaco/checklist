checklist = list()

# Define Functions
def create(item):
    checklist.append(item)

def read(index):
    print(checklist[index])

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)

def list_all_items():
    for x in checklist:
        print(x)

def mark_completed(index):
    checklist[index] = "√" + checklist[index]
    print(checklist[index])

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def select(function_code):
    if function_code == "C" or function_code == "c":
        an = input("Input Item:")
        create(an)
        return True
    # Read item
    elif function_code == "R" or function_code == "r":
        item_index = int(input("Index Number?:"))
        # Remember that item_index must actually exist or our program will crash.
        read(item_index)
        return True
    elif function_code == "M" or function_code == "m":
        an = int(input("INPUT INDEX:"))
        mark_completed(an)
        return True
    # Print all items
    elif function_code == "P" or function_code == "p":
        list_all_items()
        return True
    elif function_code == "D" or function_code == "d":
        destroy_index = int(input("Index to destroy?:"))
        destroy(destroy_index)
        return True
    elif function_code == "Q" or function_code == "q":
        return False
    # Catch all
    else:
        print("Unknown Option")
    # User Selection Code here

def test():
    print("This is a testing function")
    select("C")
    list_all_items()
    print("testing reading function..")
    select("R")
    list_all_items()
    print("testing checkmark function..")
    select("M")
    print("Test function Ended..")
# Run Tests
test()

running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list, P to display list, D to destroy, and Q to quit or M to mark ")
    running = select(selection)

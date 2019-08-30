# Create our Checklist
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
    print("√" + checklist[index])

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def select(function_code):
    if function_code == "C":
        an = input("Input Item")
        create(an)
        return True
    # Read item
    elif function_code == "R":
        item_index = int(input("Index Number?"))

        # Remember that item_index must actually exist or our program will crash.
        read(item_index)
        return True
    # Print all items
    elif function_code == "P":
        list_all_items()
        return True
    elif function_code == "Q":
        return False
    # Catch all
    else:
        print("Unknown Option")
    # User Selection Code here

def test():
    select("C")

    list_all_items()
    select("R")

    list_all_items()

# Run Tests
test()

running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list, P to display list, and Q to quit")
    running = select(selection)

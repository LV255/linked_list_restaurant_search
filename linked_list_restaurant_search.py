import time

# Define the Node class:
class Node:
    def __init__(self, info, next_node=None):
        self.info = info
        self.next_node = next_node

    def get_info(self):
        return self.info

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

# Create the LinkedList class:
class LinkedList:
    def __init__(self, info=None):
        self.head_node = Node(info)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def search(self, request):
        options = ""
        current_node = self.get_head_node()
        while current_node:
            split_to_words = current_node.get_info().split()
            for single_word in split_to_words:
                if single_word.lower() == request.lower():
                    options += str(current_node.info) + "\n\n"
            current_node = current_node.get_next_node()

        # present search results
        if options == "":
            print("Sorry, no matches.")
            time.sleep(1)
            print()
            search_function()
        elif options != "":
            print("Here are some suggestions: ")
            time.sleep(1)
            print()
            print(options)
            again = input("Would you like to search again? (y/n)")
            if again.lower() == "y":
                print()
                search_function()
            elif again.lower() == "n":
                quit()
            else:
                search_function()

# create the linked list and add in restaurants
restaurant_list = LinkedList("""Restaurant Name: Naga Restaurant
Food: Indian
Price: $$
Rating: 4.5/5
Location: 12 Main street, Frodsham""")

restaurant_list.insert_beginning("""Restaurant Name: Asian delight
Food: Chinese
Price: $$
Rating: 4/5
Location: 23 Church street, Frodsham""")

restaurant_list.insert_beginning("""Restaurant Name: EJ's Fry-up
Food: Fish and chips
Price: $
Rating: 4/5
Location: 9 Church street, Frodsham""")

restaurant_list.insert_beginning("""Restaurant Name: India Garden
Food: Indian
Price: $$
Rating: 3.5/5
Location: 15 Red Lane, Frodsham""")

restaurant_list.insert_beginning("""Restaurant Name: The Bear's Paw
Food: British
Price: $$
Rating: 3.5/5
Location: 2 High street, Frodsham""")

restaurant_list.insert_beginning("""Restaurant Name: The Queen's Head
Food: British
Price: $$
Rating: 4/5
Location: 3 Red Lane, Frodsham""")

restaurant_list.insert_beginning("""Restaurant Name: Next Door
Food: European
Price: $$$
Rating: 4.5/5
Location: 17 Church street, Frodsham""")

restaurant_list.insert_beginning("""Restaurant Name: Costa Coffee
Food: Cafe
Price: $
Rating: 4/5
Location: 1 Main street, Frodsham""")

restaurant_list.insert_beginning("""Restaurant Name: Subway
Food: Sandwiches
Price: $
Rating: 4/5
Location: 6 Church street, Frodsham""")

restaurant_list.insert_beginning("""Restaurant Name: The Cottage Tea Shop
Food: Sandwiches, Cafe
Price: $$
Rating: 4.5/5
Location: 8 Main street, Frodsham""")

restaurant_list.insert_beginning("""Restaurant Name: Athens cafe
Food: Greek
Price: $$
Rating: 3/5
Location: 21 High street, Frodsham""")

restaurant_list.insert_beginning("""Restaurant Name: Tokyo town
Food: Sushi, Japanese
Price: $$$
Rating: 5/5
Location: 34 High street, Frodsham""")

restaurant_list.insert_beginning("""Restaurant Name: Paolo's Pizzeria
Food: Pizza, Italian
Price: $
Rating: 3/5
Location: 41 Church street, Frodsham""")

def search_function():
    request = input("What type of food are you interested in? ")
    time.sleep(1)
    print()
    restaurant_list.search(request)

print("   ### Welcome to the Frodsham food guide ###   ")
time.sleep(1)
print("You can search for restaurants in the local area. ")
time.sleep(1)
print("Please type in a search term. For example, British, Indian, Chinese... ")
time.sleep(1)
print()

search_function()
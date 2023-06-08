"""
SPPU Computer Engineering DSA Lab 
Group A - 1

Consider telephone book database of N clients. Make use of a hash table implementation to
quickly look up client's telephone number. Make use of two collision handling
techniques and compare them using number of comparisons required to find a set of 
telephone numbers.
"""


class Record:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self) -> str:
        return f"{self.name}: {self.phone}"


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hashFunction(self, key):
        total = 0
        for i in range(len(key)):
            total += ord(key[i])
        return total % self.size

    def insert(self, name, phone):
        comparisions = 0
        key = self.hashFunction(name)
        if self.table[key] == None:
            self.table[key] = Record(name, phone)
            comparisions += 1
        else:
            comparisions += 1
            index = (key + 1) % self.size
            while index != key:
                if self.table[index]==None:
                    self.table[index] = Record(name,phone)
                    comparisions +=1
                    break
                else:
                    comparisions+=1
                    index = (index+1)%self.size
                print("Hash Table is full!")
        print(f"Comparisions required for {name} insertion are {comparisions}.")

    def search(self,name):
        comparisions = 0
        key = self.hashFunction(name)
        if self.table[key] == name:
            comparisions += 1
            print("Record found!")
        else:
            comparisions += 1
            index = (key + 1) % self.size
            while index != key:
                if self.table[index]==None:
                    comparisions +=1
                    print("Record found!")
                    break
                else:
                    comparisions+=1
                    index = (index+1)%self.size
            if index==key:
                print("Not found!")

        print(f"Comparisions required for {name} searching are {comparisions}")
    
    def delete(self, name):
        comparisions = 0
        key = self.hashFunction(name)
        if self.table[key] is not None and self.table[key].name == name:
            comparisions += 1
            self.table[key] = None
            print("Contact deleted successfully")
        else:
            comparisions += 1
            index = (key + 1) % self.size
            while index != key:
                if self.table[index] is not None and self.table[index].name == name:
                    comparisions += 1
                    self.table[index] = None
                    print("Contact deleted successfully")
                    break
                else:
                    comparisions += 1
                    index = (index + 1) % self.size
            if index == key:
                print("Contact not found!")
        print(f"Comparisons required for {name} deletion are {comparisions}")


    def display(self):
        for i in range(self.size):
            if self.table[i] is not None:
                print(self.table[i])
                # for r in self.table[i]:
                #     print(r)


def main(phone_book):

    # Continuously prompt the user to choose an operation until they choose to quit
    while True:
        print("1. Add contact")
        print("2. Search contact")
        print("3. Delete contact")
        print("4. Display all contacts")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        # Add a new contact to the phone book
        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            phone_book.insert(name, phone)
            print("Contact added successfully!")

        # Search for a contact in the phone book
        elif choice == "2":
            name = input("Enter name to search: ")
            phone_book.search(name)

        # Delete a contact from the phone book
        elif choice == "3":
            name = input("Enter name to delete: ")
            phone_book.delete(name)

        # Display all the contacts in the phone book
        elif choice == "4":
            phone_book.display()

        # Quit the program
        elif choice == "5":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    phone_book = HashTable(10)

    # Created Random Contacts
    phone_book.insert("Rashmi Desai", "5432109876")
    phone_book.insert("Sunita Gupta", "4321098765")
    phone_book.insert("Sachin Singh", "3210987654")
    phone_book.insert("Ankit Jain", "2109876543")
    phone_book.insert("Ankit Mishra", "1098765432")

    main(phone_book)  # Calling the main function

    print("Code by Pranav Mehendale")
    
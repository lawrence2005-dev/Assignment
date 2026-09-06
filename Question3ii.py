class Book:
    # Constructor
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    # Method to display book details
    def display_details(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price: $", self.price)
        print()


# Instantiate two book objects
book1 = Book("Makunun'unu Maodzamoyo", "Charles L Mungoshi", 15.00)
book2 = Book("Tambaoga Mwanangu", "Giles Kuimba", 20.00)

# Display the details of both books
book1.display_details()
book2.display_details()
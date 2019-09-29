class Book:

    def __init__(self,title,author,quant,price):
        self.title = title
        self.author = author
        self.quant = quant
        self.price = price

    def displayBooks(self):                                     #This function prints the characteristics of a book.
        print ("The title is: ", self.title,".")
        print ("The author is: ", self.author,".")
        print ("The quantity of this book is: ", self.quant,".")
        print ("The price is: ", self.price,".")

    
Book1 = Book("Lord of the rings","J.R.R. Tolkien",5,11.4)
Book2 = Book("Crime & Punishment","F.Dostojevskis",2,13.7)      #Library contains already these books.
Book3 = Book("Animal farm","G.Orwell",4,9.7)                    
Book4 = Book("Hobbit","J.R.R. Tolkien",1,8.5)

list_of_books=[Book1,Book2,Book3,Book4]                         #List of the available books.

def displayMenu():                                              #This function prints the menu.
    print ("If you want: to see all the available books press: 1+ENTER")
    print ("             to search a book by the title press: 2+ENTER")
    print ("             to search the books of an certain author press: 3+ENTER")
    print ("             to buy an available book press: 4+ENTER")                     
    print ("             to order a book press: 5+ENTER")
    print ("             to change the price of an available book press: 6+ENTER")
    print ("             to see the money of the cash register press: 7+ENTER")
    print ("             to stop this process press: 0+ENTER")

def display_all():                                              #This function prints only the characteristics of the available books.
    for i in range(len(list_of_books)):       
        list_of_books[i].displayBooks()
        print (" ")


def bytitle(title):                                             #This function prints the characteristics of a certain book only if it is available.
    for i in range(len(list_of_books)):
        if (list_of_books[i].title.upper()==title.upper()):
            list_of_books[i].displayBooks()

def byauthor(author):                                           #This function prints the books(and their characteristics) of a certain author.                                 
    for i in range(len(list_of_books)):
        if (list_of_books[i].author.upper()==author.upper() ):
            list_of_books[i].displayBooks()
            print (" ")



summation=0                                                     #The money of the cash register at the beginning.   
def buybook(title,summation):                                   #This function decreases the amount of a certain book and it returns the increased summation of the cash register.
    for i in range(len(list_of_books)):
        if (list_of_books[i].title.upper()==title.upper()):
            summation=summation+list_of_books[i].price
            list_of_books[i].quant=list_of_books[i].quant-1
            return summation


def orderbook(title):                                           #This function:
    notavailable=True
    for i in range(len(list_of_books)):                         #prints the quantity of an available book and gives the opportunity to increase it
        if (list_of_books[i].title.upper()==title.upper()):
            print("There are",str(list_of_books[i].quant))
            morebooks=int(input("You can order more books: "))
            list_of_books[i].quant=list_of_books[i].quant+morebooks
            notavailable=False
    if (notavailable):                                          #or if it is not available,it adds the new book in the available list(with the characteristics).
        T=input("Enter the title of the book: ")
        A=input("Enter the author of the book: ")
        P=int(input("Enter the price of the book: "))
        Q=int(input("Enter the quantity of the book: "))
        list_of_books.append(Book(T,A,Q,P))


def changeprice(title):                                         #This function changes the price of an available book.
    for i in range(len(list_of_books)):
        if (list_of_books[i].title.upper()==title.upper()):
            price=int(input("Enter the new price: "))
            list_of_books[i].price=price



displayMenu()
i=int(input("Select: "))
while(i!=0):                                                    #This process ends when the user enters 0.          
    if(i==1):
        display_all()
    elif(i==2):
        title=input("Which book are you looking for? -")
        bytitle(title)
    elif(i==3):
        author=input("Which author's book are you looking for? -")
        byauthor(author)
    elif(i==4):
        title=input("Which book do you want to buy? -")
        summation=buybook(title,summation)
    elif(i==5):
        title=input("Which book do you want to order? -")
        orderbook(title)
    elif(i==6):
        title=input("Which book's price do you want to change? -")
        changeprice(title)
    else:
        print("The money in the cash register is: ",summation)      #It prints the money of the cash register.
    j=0
    while(j<=len(list_of_books)-1):                                 #If the quantity of a book is zero ,it will be removed from the list of the available books
        if (list_of_books[j].quant<1):
            del list_of_books[j]
        j=j+1
    displayMenu()
    i=int(input("Select: "))
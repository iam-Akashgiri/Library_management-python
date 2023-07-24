class Library:
    def __init__(self,name,std,roll):
        self.std_name=name
        self.std_std=std
        self.std_roll=roll
        self.books=['Ramayan','Mahabharat','Harry potter','Histroy','Maths']
        self.issued_list=[]

        # self.no_of_books=  len(self.books)  do not store any value which will gonna use in future with some randome chnages beacuse it will not work with new modiefied chanes it will show you the same previos store value in as output
    


    def available_books(self):
        print(f'Total {len(self.books)}  books are available {self.books}')



    def std_info(self):
        print(f'stundent name is {self.std_name}')
        print(f'stundent standard is {self.std_std}')
        print(f'stundent roll is {self.std_roll}')


    def issue_book(self,book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f'Book is successfuly issued on your name kindly return on time')
            self.issued_list.append(book_name)
        else:
            if book_name in self.issued_list:
                print(f'book is not available in the library may be it is issued by {self.std_name}')
            else:
                print(f'These book is not available in our library...!\n The list ofavailable books are in library is {self.books} ')


    def Return_book(self,new_book):
        if new_book in self.issued_list:
            self.books.append(new_book)
            self.issued_list.remove(new_book)
            print('Book safely returned in library..!')
            self.available_books()
        else:
            print('These book does not belongs to Library and its not been issued from library..\n Do you want to donate it..?')
            self.a=input('Kindly confirm(yes/no): ')
            if self.a == 'yes':
                self.books.append(new_book)
                print('Thank you for Danating the book..!!')
            else:
                print('Thanks for Confirmation.. ')


                

print(' '*50, 'Welcome to Library')

student_name = input('Enter your name: ')
student_clas = input('Enter your standard: ')
student_Roll = input('Enter your Roll no. ')
student_name= Library(student_name, student_clas, student_Roll)


while 1:

    print(' '*50,' 1.List of Available books.\n' ,' '*50, '2.Want to issue a book. \n',' '*50, '3.want to return a book. \n',' '*50,'4.exit', ' '*50)
    user=int(input('Plese Enter option(1,2,3,4): ' ))
    if user==1:
        student_name.available_books()
    elif user==2:
        book_name = str(input('Enter a book name: '))
        student_name.issue_book(book_name)
    elif user==3:
        new_book = input('Enter a book name you want to return: ')
        student_name.Return_book(new_book)
    elif user==4:
        print(' '*50 ,'Thanks for using My Library..!!')
        exit()
    else:
        print('Oopss ..!! Enter a valid option..')





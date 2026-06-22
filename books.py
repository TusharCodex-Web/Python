# class book:
#     def __init__(self,title,author):
#         self.title = title
#         self.author = author
    
#     def __str__(self):
#         return '<book: {} by {}>'.format(self.title, self.author)

# class TextBook:
#     def __init__(self, title, author, subject):
#         self.title = title
#         self.author = author
#         self.subject = subject

#     def __str__(self):
#         return '<TextBook: {} by {}({})>'.format(self.title,
#                                                          self.author,
#                                                          self.subject)

# book = book(title="all the light ", author="some person")
# textbook = TextBook(title = "python programming", author="some person", subject="programming")

# print(book)
# print(textbook)









# class book:
#     def __init__(self,title,author):
#         self.title = title
#         self.author = author
    
#     def __str__(self):
#         return '<book: {} by {}>'.format(self.title, self.author)

# class TextBook(book):
#     def __init__(self, title, author, subject):
#         super().__init__(title, author)
#         self.subject = subject


# book = book(title="all the light ", author="some person")
# textbook = TextBook(title = "python programming", author="some person", subject="programming")

# print(book)
# print(textbook)




# class A:
#     def say_my_name(self):
#         print('A')

# class B(A):
#     pass
#     # def say_my_name(self):
#     #     print('B')

# class C(A):
#     def say_my_name(self):
#         print('C')

# class D(B,C):
#     pass

# a = A()
# b = B()
# c = C()
# d = D()

# a.say_my_name()
# b.say_my_name()
# c.say_my_name()



class A:
    def say_my_name(self):
        print('A')

class B(A):
    def say_my_name(self):
        print('B')

class C(A):
    def say_my_name(self):
        print('C')

class D(C ,B):
    pass

a = A()
b = B()
c = C()
d = D()

a.say_my_name()
b.say_my_name()
c.say_my_name()
d.say_my_name()

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








# class A:
#     def say_my_name(self):
#         print('A')

# class B(A):
#     def say_my_name(self):
#         print('B')

# class C(A):
#     def say_my_name(self):
#         print('C')

# class D(C ,B):
#     pass

# a = A()
# b = B()
# c = C()
# d = D()

# a.say_my_name()
# b.say_my_name()
# c.say_my_name()
# d.say_my_name()




# # 2nd 
# class Writeable:
#     def write(self, data):
#         with open(self.filepath, 'w') as f:
#             f.write(data)

# class Readable:
#     def read(self):
#         with open(self.filepath, 'r') as f:
#             print(f.read())

# class book(Writeable, Readable):
#     def __init__(self,title,author,filepath):
#         self.title = title
#         self.author = author
#         self.filepath = filepath
    
# book = book(title="something", author="some person", filepath="./book.txt")
# book.write("this is a book")
# book.read()
# book.write("some more things")
# book.read()








# class Writeable:
#     def write(self, data):
#         with open(self.filepath, 'w') as f:
#             f.write(data)

# class Readable:
#     def read(self):
#         with open(self.filepath, 'r') as f:
#             print(f.read())

# class JSONSerializable:
#     def to_json(self):
#         import json
#         print(json.dumps(self.__dict__))


# class book(Writeable, Readable, JSONSerializable):
#     def __init__(self,title,author,filepath):
#         self.title = title
#         self.author = author
#         self.filepath = filepath
    
# book = book(title="something", author="some person", filepath="./book.txt")
# book.write("this is a book")
# book.read()
# book.write("some more things")
# book.read()
# book.to_json()












import json

class Reader:
    def __init__(self, filepath):
        self.filepath = filepath

    def read(self):
        with open(self.filepath , 'r') as f:
            print(f.read())


class Writer:
    def __init__(self, filepath):
        self.filepath = filepath

    def write(self, data):
        with open(self.filepath, 'w') as f:
            f.write(data)

class JSONSerializer:
    def to_json(self, obj):
        import json
        print(json.dumps(obj))

class Book:
    def __init__(self, title, author, filepath):
        self.title = title
        self.author = author
        self.filepath = filepath
        self.reader = Reader(filepath)
        self.writer = Writer(filepath)
        self.serializer = JSONSerializer()

    def read(self):
        self.reader.read()

    def write(self, data):
        self.writer.write(data)

    def to_json(self):
        self.serializer.to_json   (dict(title=self.title, 
                                     author=self.author, 
                                     filepath=self.filepath))

    
book = Book(title="something", author="some person", filepath="./book.txt")
book.write("this is a book")
book.read()
book.write("some more things")
book.read()
book.to_json()

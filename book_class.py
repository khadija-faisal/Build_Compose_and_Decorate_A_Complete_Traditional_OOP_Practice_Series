#practice question 11
#11. Class Methods
class Book:
    total_books = 5
    @classmethod
    def increment_book_count(cls, count):
        cls.total_books += count


    
Book().increment_book_count(5)
print(f"the count of total books {Book.total_books}")
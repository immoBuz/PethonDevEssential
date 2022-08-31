from Book import Book


book1 = Book(author='Marcus Perrie', name='Fighting back', issue_date='2019-01-01',genre='SciFi')
print(book1.get_info())
book2 = Book(author='Miranda Devis', name='Mystery sight', issue_date='2019-02-01', genre='Novel')
print(book2.get_info())
book3 = Book(author='Marcus Perrie', name='Fighting back', issue_date='2019-01-01',genre='SciFi')
print(book3.get_info())
print(book1 == book2)
print(book1 == book3)

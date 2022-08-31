class Book:
    def __init__(self, author, name, issue_date, genre):
        self.__author = author
        self.__name = name
        self.__issue = issue_date
        self.__genre = genre

    def get_author(self):
        return self.__author

    def get_name(self):
        return self.__name

    def get_issue_date(self):
        return self.__issue

    def get_genre(self):
        return self.__genre

    def get_info(self):
        return self.__author, self.__name, self.__issue, self.__genre

    def __eq__(self, other):
        return (
                self.get_author() == other.get_author()
                and self.get_name() == other.get_name()
                and self.get_issue_date() == other.get_issue_date()
                and self.get_genre() == other.get_genre()
        )

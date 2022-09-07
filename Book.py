class Book:
    def __init__(self, author, name, issue_date, genre):
        self.__author = author
        self.__name = name
        self.__issue = issue_date
        self.__genre = genre

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_issue_date(self):
        return self.__issue

    def set_issue_date(self, issue_date):
        self.__issue = issue_date

    def get_genre(self):
        return self.__genre

    def set_genre(self, genre):
        self.__genre = genre

    def get_info(self):
        return (
            self.get_name(),
            self.get_author(),
            self.get_issue_date(),
            self.get_genre()
        )

    def __eq__(self, other):
        return (
                self.get_author() == other.get_author()
                and self.get_name() == other.get_name()
                and self.get_issue_date() == other.get_issue_date()
                and self.get_genre() == other.get_genre()
        )

    def __hash__(self):
        return hash((self.get_author(), self.get_name(), self.get_issue_date(), self.get_genre()))

    def __str__(self):
        return (
            f"Book:\n\t(name) {self.get_name()}"
            + f"\n\t(author) {self.get_author()}"
            + f"\n\t(issue) {self.get_issue_date()}"
            + f"\n\t(genre) {self.get_genre()}"
        )

    def __repr__(self):
        return (
            f"Book(author='{self.get_author()}', "
            + f"name='{self.get_name()}', "
            + f"issue_date='{self.get_issue_date()}', "
            + f"genre='{self.get_genre()}'"
            + ")"
        )


class BookReview:
    def __init__(self, user_id, body, review_date):
        self.__id = user_id
        self.__body = body
        self.__rev_date = review_date

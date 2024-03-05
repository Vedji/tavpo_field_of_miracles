import random


class FieldOfMiracles:
    def __init__(self):
        self.database_words = ["чай", "кофе", "компьютер"]
        self.word = None
        self.guess_word = None

    def guess_letter(self, letter: str) -> str:
        """
        Return string 'Сначала загадайте слово'
        Return string 'Буква <letter> угадана, ваше слово <self.guess_word>' if letter guess'
        Return string 'В слове <self.guess_word> нет буквы <letter>' if letter not guess'
        Return 'Вы угадали слово <self.word>' if user win'
        Return 'Можно ввести только одну букву на русском' if user input incorrect letter
        """
        pass

    def generate_word(self) -> str:
        """
        Return: 'Слово длинной <len(self.guess_word)> сгенерированно'
        """
        pass


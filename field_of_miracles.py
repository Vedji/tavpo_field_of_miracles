import random
import re


class FieldOfMiracles:
    def __init__(self):
        self.database_words = [
            "дом", "машина", "яблоко", "кофе", "дерево", "компьютер", "человек", "ребенок", "время", "день",
            "ночь", "улица", "город", "дождь", "снег", "ветер", "небо", "земля", "вода", "огонь",
            "цветок", "трава", "птица", "рыба", "кошка", "собака", "мышь", "книга", "телефон", "стол",
            "стул", "окно", "дверь", "стена", "пол", "потолок", "свет", "тень", "звук", "тишина",
            "работа", "игра", "школа", "учебник", "учитель", "ученик", "магазин", "товар", "цена", "качество",
            "жизнь", "здоровье", "счастье", "любовь", "чай"
        ]
        self.word = None
        self.guess_word = None

    def guess_letter(self, letter: str) -> str:
        """
        :return str 'Сначала загадайте слово' \n
        :return str 'Можно ввести только одну букву' \n
        :return str 'Можно ввести только одну букву на русском' if user input incorrect letter \n
        :return str 'Буква <letter> угадана, ваше слово <self.guess_word>' if letter guess' \n
        :return str 'Вы угадали слово <self.word>' if user win' \n
        :return str 'В слове <self.guess_word> нет буквы <letter>' if letter not guess' \n
        """
        if self.word is None or len(self.word) <= 0:
            return 'Сначала загадайте слово'
        if len(letter) != 1:
            return 'Можно ввести только одну букву'
        if not re.search("[а-яА-Я]", letter):
            return'Можно ввести только одну букву на русском'
        letter = letter.lower()
        if letter in self.word:
            self.guess_word = "".join([
                    self.word[i] if self.word[i] == letter or self.guess_word[i] == self.word[i] else '_'
                    for i in range(len(self.word))])
            if self.guess_word != self.word:
                return f'Буква {letter} угадана, ваше слово {self.guess_word}'
            else:
                return f'Вы угадали слово {self.word}'

        return f'В слове {self.guess_word} нет буквы {letter}'

    def generate_word(self) -> str:
        """
        :return str 'Слово длинной <len(self.guess_word)> сгенерированно'
        """
        self.word = self.database_words[random.randrange(0, len(self.database_words))]
        self.guess_word = '_' * len(self.word)
        return f'Слово длинной {len(self.word)} сгенерированно'


if __name__ == "__main__":
    random.seed(2)
    test = FieldOfMiracles()
    print(test.generate_word())
    print(test.generate_word())
    print(test.generate_word())

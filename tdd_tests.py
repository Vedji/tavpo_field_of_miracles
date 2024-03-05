import unittest
import field_of_miracles
import random


class TestFieldOfMiracles(unittest.TestCase):

    def setUp(self):
        self.field_of_miracles = field_of_miracles.FieldOfMiracles()

    def test_generate_word(self):
        random.seed(2)
        self.assertEqual(self.field_of_miracles.generate_word(), f"Слово длинной 3 сгенерированно")   # Слово чай
        self.assertEqual(self.field_of_miracles.generate_word(), f"Слово длинной 4 сгенерированно")   # Слово кофе
        self.assertEqual(self.field_of_miracles.generate_word(), f"Слово длинной 9 сгенерированно")   # Слово компьютер

    def test_guess_letter(self):
        random.seed(2)
        self.field_of_miracles.generate_word()
        self.assertEqual(self.field_of_miracles.guess_letter(""), "Можно ввести только одну букву")
        self.assertEqual(self.field_of_miracles.guess_letter("Ап"), "Можно ввести только одну букву")
        self.assertEqual(self.field_of_miracles.guess_letter("F"), "Можно ввести только одну букву на русском")
        self.assertEqual(self.field_of_miracles.guess_letter("Ч"), "Буква ч угадана, ваше слово ч__")
        self.assertEqual(self.field_of_miracles.guess_letter("ш"), "В слове ч__ нет буквы ш")
        self.assertEqual(self.field_of_miracles.guess_letter("а"), "Буква а угадана, ваше слово ча_")
        self.assertEqual(self.field_of_miracles.guess_letter("й"), "Вы угадали слово чай")



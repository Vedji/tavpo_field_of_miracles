from behave import given, when, then
import random
import field_of_miracles


@given('Generate word by seed {number}')
def step_generate(context, number):
    random.seed(number)


@when('Print guess word')
def step_generate(context):
    context.result = field_of_miracles.FieldOfMiracles().generate_word()


@then('Get printed guess word')
def step_generate(context):
    assert context.result == 'Слово длинной 3 сгенерированно'


@given('Guess letter {letter}')
def step_guess(context, letter):
    context.letter = letter
    random.seed(2)
    context.miracles = field_of_miracles.FieldOfMiracles()
    context.miracles.generate_word()


@when('Check input letter')
def step_guess(context):
    context.result = context.miracles.guess_letter(context.letter)


@then('print letter guess')
def step_guess(context):
    assert context.result == 'Буква ч угадана, ваше слово ч__'


@then('print letter not guess')
def step_guess(context):
    assert context.result == f'В слове ___ нет буквы п'


@given('Guess letter {letter} not generated')
def step_not_generate(context, letter):
    context.letter = letter
    random.seed(2)
    context.miracles = field_of_miracles.FieldOfMiracles()


@when('Check input letter')
def step_guess(context):
    context.result = context.miracles.guess_letter(context.letter)


@when('Check input letter not generated')
def step_guess(context):
    context.result = context.miracles.guess_letter(context.letter)


@then('Print error')
def step_guess(context):
    assert context.result == 'Сначала загадайте слово'

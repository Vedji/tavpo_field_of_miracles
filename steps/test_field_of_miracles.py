from behave import given, when, then
import random
import field_of_miracles


@given('Generate word by seed {number}')
def step_generate_given(context, number):
    context.seed = number


@when('Print guess word')
def step_generate_when(context):
    random.seed(context.seed)
    context.miracles = field_of_miracles.FieldOfMiracles()


@then('Get printed guess word')
def step_generate_then(context):
    context.result = context.miracles.generate_word()
    assert context.result == 'Слово длинной 7 сгенерированно'


@given('Guess letter {letter}')
def step_guess_given(context, letter):
    context.letter = letter
    random.seed(2)
    context.miracles = field_of_miracles.FieldOfMiracles()
    context.miracles.generate_word()


@when('Check input letter')
def step_guess_when(context):
    context.result = context.miracles.guess_letter(context.letter)


@then('Print letter guess')
def step_guess_then(context):
    assert context.result == 'Буква ч угадана, ваше слово ч__'


@given('Not Guess letter {letter}')
def step_not_guess_given(context, letter):
    context.letter = letter
    random.seed(2)
    context.miracles = field_of_miracles.FieldOfMiracles()
    context.miracles.generate_word()


@when('Not Check input letter')
def step_not_guess_when(context):
    context.result = context.miracles.guess_letter(context.letter)


@then('Print letter not guess')
def step_not_guess_then(context):
    assert context.result == f'В слове ___ нет буквы п'


@given('Not generated Guess letter {letter}')
def step_not_generate_given(context, letter):
    context.letter = letter
    random.seed(2)
    context.miracles = field_of_miracles.FieldOfMiracles()


@when('Check input letter not generated')
def step_not_generate_when(context):
    context.result = context.miracles.guess_letter(context.letter)


@then('Print error')
def step_not_generate_then(context):
    assert context.result == 'Сначала загадайте слово'

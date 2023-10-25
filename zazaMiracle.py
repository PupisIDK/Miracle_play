from behave import given, when, then
from zaza import play_game

@given('the game is started')
def step_impl(context):
    context.num_players = 2
    context.word = play_game(context.num_players)


@when('I enter "{num}" players')
def step_impl(context, num):
    context.num_players = int(num)

@then('I should see "{message}"')
def step_impl(context, message):
    assert context.output.splitlines()[-1] == message


@when('I guess "{letters}"')
def step_impl(context, letters):
    for l in letters:
        context.output = play_game(context.num_players, context.word, l)

@given('the game is started')
def start_game(game):
    game.start()


@when('I enter "{num}" players')
def enter_players(game, num):
    game.num_players = int(num)


@then('a random word should be selected')
def verify_word(word, WORDS=None):
    if WORDS is None:
        WORDS = ["python", "programming", "code", "miracle"]
    assert word in WORDS


@when('I guess "{letter}" again')
def guess_again(game, letter, prev_guesses):
    prev_guesses.append(letter)
    game.guess(letter)


@given('the game is started')
def step_impl(game):
    game.start()


@when('I guess "{letter}"')
def guess(game, letter):
    game.guess(letter)


@then('I should see "{message}"')
def check_message(output, message):
    assert message in output

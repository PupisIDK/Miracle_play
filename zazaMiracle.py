from behave import given, when, then
from zaza import play_game


@given('the game is started')
def step_impl(context):
    context.num_players = 2
    context.word = play_game(context.num_players)


@when('I enter "{num}" players')
def step_impl(context, num):
    context.num_players = int(num)



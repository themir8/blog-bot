from aiogram.dispatcher.filters.state import State, StatesGroup


class States(StatesGroup):

    # Main states
    recommendations = State()
    search = State()
    follows = State()
    my_blog = State()

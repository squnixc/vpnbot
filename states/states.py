from aiogram.fsm.state import StatesGroup, State


class MenuState(StatesGroup):
    intro = State()
    main_menu = State()


class DeviceState(StatesGroup):
    choose_device = State()


class SubscriptionState(StatesGroup):
    plans = State()
    payment_method = State()
    confirm = State()


class FAQState(StatesGroup):
    reading = State()


class AdminState(StatesGroup):
    main = State()
    panel = State()
    about = State()
    send = State()
    gift = State()
    config = State()
    manage = State()

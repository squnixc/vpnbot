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

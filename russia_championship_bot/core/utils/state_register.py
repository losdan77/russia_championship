from aiogram.fsm.state import StatesGroup, State

class StepsRegister(StatesGroup):
    GET_EMAIL = State()
    GET_CODE = State()
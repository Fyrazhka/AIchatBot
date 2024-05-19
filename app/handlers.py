from aiogram.types import Message
from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from app.generators import gpt4o

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await message.answer('Добро пожаловать!')
    await state.clear()

class Generate(StatesGroup):
    text = State()

@router.message(F.text)
async def generate(message: Message, state: FSMContext):
    await state.set_state(Generate.text)
    response = await gpt4o(message)  # Pass the entire message object
    await message.answer(response.choices[0].message.content)
    await state.clear()

@router.message(Generate.text)
async def generate_error(message: Message):
    await message.answer("Генерация предыдущего ответа...")

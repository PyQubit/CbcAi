from aiogram.fsm.state import State, StatesGroup


class UserState(StatesGroup):
    """حالت‌های کاربر در بات"""

    choose_language = State()  # انتخاب زبان اولیه برای کاربر جدید
    medical_chat = State()     # مشاوره پزشکی
    lab_analysis = State()     # تحلیل آزمایش
    doctor_guide = State()     # راهنمای انتخاب تخصص پزشک

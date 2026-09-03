from aiogram import Router

from handlers.admin import router as admin_router
from handlers.chat import router as chat_router
from handlers.common import fallback_router, router as common_router
from handlers.doctors import router as doctors_router
from handlers.lab import router as lab_router
from handlers.premium import router as premium_router
from handlers.settings import router as settings_router


def setup_routers() -> Router:
    root = Router()
    root.include_router(admin_router)
    # settings قبل از بقیه تا انتخاب زبان در onboarding درست کار کند
    root.include_router(settings_router)
    root.include_router(common_router)
    root.include_router(chat_router)
    root.include_router(lab_router)
    root.include_router(doctors_router)
    root.include_router(premium_router)
    # fallback باید آخر باشد
    root.include_router(fallback_router)
    return root

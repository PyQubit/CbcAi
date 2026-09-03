from groq import AsyncGroq

from config import GROQ_API_KEY

# کلاینت مشترک Groq — فقط اتصال، بدون منطق کسب‌وکار
groq_client = AsyncGroq(api_key=GROQ_API_KEY)
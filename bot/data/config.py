# Импорт необходимых модулей и классов
import os

from dotenv import load_dotenv

# Определение пути к файлу .env
dotenv_path = os.path.join(os.path.dirname(__file__), '.env.dist')

# Проверка существования файла .env и загрузка переменных окружения
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# Получение значений переменных окружения
BOT_TOKEN = str(os.getenv('BOT_TOKEN'))
PGUSER = str(os.getenv("PGUSER"))
PGPASSWORD = str(os.getenv("PGPASSWORD"))
DATABASE = str(os.getenv("DATABASE"))
admins = [
    713171665
]

ip = os.getenv("ip")

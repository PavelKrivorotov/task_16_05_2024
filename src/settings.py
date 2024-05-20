import os
from pathlib import Path
Base_Dir = Path(__file__).parent.parent

from dotenv import load_dotenv
load_dotenv(Path(Base_Dir, '.env'))


DATABASE = {
    'MIDDLWARE': os.getenv('DB_MIDDLWARE'),
    'USER': os.getenv('DB_USER'),
    'PASSWORD': os.getenv('DB_PASSWORD'),
    'NAME': os.getenv('DB_NAME'),
    'HOST': os.getenv('DB_HOST'),
    'PORT': int(os.getenv('DB_PORT'))
}


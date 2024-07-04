from pathlib import Path
from env import DATABASE

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATABASES = {
    'default': {
        'ENGINE': DATABASE['ENGINE'],
        'NAME': BASE_DIR / DATABASE['NAME'],
    }
}
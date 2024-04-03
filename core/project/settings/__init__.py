import os
from pathlib import Path
from decouple import config,Csv
from dotmap import DotMap

ENV = DotMap({'config': config, 'Csv': Csv})
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

ADMIN_PATH = ENV.config("ADMIN_PATH")
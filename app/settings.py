import os
import distutils.util

DEBUG = bool(distutils.util.strtobool(os.getenv("DEBUG", "True")))
DATA_FOLDER = os.getenv("DATA_FOLDER", default="/data")

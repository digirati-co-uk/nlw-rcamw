import os
import distutils.util

DEBUG = bool(distutils.util.strtobool(os.getenv("DEBUG", "True")))
DATA_FOLDER = os.getenv("DATA_FOLDER", default="/data")
URL_PREFIX = os.getenv("URL_PREFIX")
DESCRIPTION = os.getenv("DESCRIPTION", default="Description")
ATTRIBUTION = os.getenv("ATTRIBUTION", default="Attribution")

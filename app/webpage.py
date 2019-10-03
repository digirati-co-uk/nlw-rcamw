from os import listdir
from os.path import isfile, join
import json

import settings

page = "<html><head></head><body>"


filenames = [f for f in listdir(settings.DATA_FOLDER) if isfile(join(settings.DATA_FOLDER, f))]

for filename in filenames:
    print(filename)
    if ".json" not in filename:
        print("skipping")
        continue

    label = filename.replace(".json", "")

    page = page + f"<a href='https://universalviewer.io/uv.html?manifest={settings.URL_PREFIX}/{filename}'>{label}</a><br/>"

page = page + "</body></html>"

with open(join(settings.DATA_FOLDER, "index.html"), "w") as new_file:
    new_file.write(page)

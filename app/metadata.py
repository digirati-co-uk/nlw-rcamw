from os import listdir
from os.path import isfile, join
import json

import settings

filenames = [f for f in listdir(settings.DATA_FOLDER) if isfile(join(settings.DATA_FOLDER, f))]

for filename in filenames:
    print(filename)
    if ".json" not in filename:
        print("skipping")
        continue

    label = filename.replace(".json", "")

    content = ""
    with open(join(settings.DATA_FOLDER, filename), "r") as content_file:
        content = content_file.read()

    content_as_dict = json.loads(content)

    content_as_dict["label"] = label
    content_as_dict["metadata"][0]["value"] = label

    for canvas in content_as_dict["sequences"][0]["canvases"]:
        image_id = canvas["images"][0]["resource"]["service"]["@id"].split("/").pop()
        if image_id.startswith(f"{label}_"):
            image_id = image_id[len(label)+1:]
        canvas["label"] = image_id

    with open(join(settings.DATA_FOLDER, "metadata", filename), "w") as new_file:
        new_file.write(json.dumps(content_as_dict, indent=4, sort_keys=True))
    # print(json.dumps(content_as_dict))

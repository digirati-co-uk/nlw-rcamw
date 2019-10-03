from os import listdir
from os.path import isfile, join
import json

import settings

collection = {
  "@context": "http://iiif.io/api/presentation/2/context.json",
  "@id": f"{settings.URL_PREFIX}/root.json",
  "@type": "sc:Collection",
  "label": "RCAMW",
  "viewingHint": "top",
  "description": settings.DESCRIPTION,
  "attribution": settings.ATTRIBUTION,
  "manifests": []
}

filenames = [f for f in listdir(settings.DATA_FOLDER) if isfile(join(settings.DATA_FOLDER, f))]

for filename in filenames:
    print(filename)
    if ".json" not in filename:
        print("skipping")
        continue

    label = filename.replace(".json", "")

    collection["manifests"].append({
      "@id": f"{settings.URL_PREFIX}/{filename}",
      "@type": "sc:Manifest",
      "label": label
    })


with open(join(settings.DATA_FOLDER, "root.json"), "w") as new_file:
    new_file.write(json.dumps(collection, indent=4, sort_keys=True))

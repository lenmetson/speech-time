# Version history
## Created 3 Nov
# 4 Nov - added code from this tutorial https://pydataverse.readthedocs.io/en/latest/user/basic-usage.html#download-and-save-a-dataset-to-disk

# Script to call Harvard Dataverse API to read in dataset

pip install pyDataverse

from pyDataverse.api import NativeApi, DataAccessApi
from pyDataverse.models import Dataverse

base_url = 'https://dataverse.harvard.edu/'

api = NativeApi(base_url)
data_api = DataAccessApi(base_url)

DOI = "https://doi.org/10.7910/DVN/EQ9WBE" # add DOI of our dataset

dataset = api.get_dataset(DOI)

files_list = dataset.json()['data']['latestVersion']['files']

for file in files_list:
    filename = file["dataFile"]["filename"]
    file_id = file["dataFile"]["id"]
    print("File name {}, id {}".format(filename, file_id))

    response = data_api.get_datafile(file_id)
    with open(filename, "wb") as f:
        f.write(response.content)

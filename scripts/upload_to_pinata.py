import os
from pathlib import Path
import requests, json
from brownie import network

PINATA_BASE_URL = "https://api.pinata.cloud"
endpoint = "/pinning/pinFileToIPFS"
filepath = {
    "PUG": "./img/pug.png",
    "SHIBA_INU": "./img/shiba-inu.png",
    "ST_BERNARD": "./img/st-bernard.png",
}
breedToIpfs = {}


def main():
    upload_to_pinata


def upload_to_pinata():
    for x in filepath:

        filename = filepath[x].split("/")[-1:][0]
        headers = {
            "pinata_api_key": os.getenv("PINATA_API_KEY"),
            "pinata_secret_api_key": os.getenv("PINATA_API_SECRET"),
        }

        with Path(filepath[x]).open("rb") as fp:
            image_binary = fp.read()
            response = requests.post(
                PINATA_BASE_URL + endpoint,
                files={"file": (filename, image_binary)},
                headers=headers,
            )
            # print(response.json())
            final_uri = (
                "https://gateway.pinata.cloud/ipfs/" + response.json()["IpfsHash"]
            )
            breedToIpfs.update({f"{x}": f"{final_uri}"})

    # print("\nFINAL DICT:\n")
    # print(breedToIpfs)


# for z in breedToIpfs:
# print(f"{z}:")
# print(f"{breedToIpfs[z]}")

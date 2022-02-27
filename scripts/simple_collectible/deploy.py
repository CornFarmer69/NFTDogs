from random import sample
from scripts.helpful_scripts import get_account, OPENSEA_URL
from brownie import SimpleCollectible, config, network

sample_token_uri = (
    "ipfs://Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"
)


def main():
    deploy_and_create()


def deploy_and_create():
    account = get_account()
    simple_collectible = SimpleCollectible.deploy({"from": account})
    tx = simple_collectible.createCollectible(sample_token_uri, {"from": account})
    tx.wait(1)
    print(
        f"Awesome, you can now view your NFT at {OPENSEA_URL.format(simple_collectible.address, (simple_collectible.tokenCounter() - 1))}"
    )
    return simple_collectible

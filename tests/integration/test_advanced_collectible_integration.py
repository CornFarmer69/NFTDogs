from brownie import network, AdvancedCollectible
import pytest
import time
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_account,
    get_contract,
)
from scripts.advanced_collectible.deploy import deploy_and_create


def test_can_create_advanced_collectible_integration():
    # deploy the contract
    # create an NFT
    # get a random breed back
    # --- Arrange
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for integration testing.")
    # --- Act
    advanced_collectible, creation_transaction = deploy_and_create()
    time.sleep(60)
    # --- Assert
    assert advanced_collectible.tokenCounter() == 1

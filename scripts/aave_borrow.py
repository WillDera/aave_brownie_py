from brownie import config, network
from scripts.get_weth import get_weth
from scripts.helpful_scripts import get_account


def main():
    account = get_account()
    erc20_address = config["networks"][network.show_active()]["weth_token"]
    # get_weth()
    if network.show_active() in ["mainnet-fork"]:
        get_weth()

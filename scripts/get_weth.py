from brownie import network, interface, config
from scripts.helpful_scripts import get_account


def main():
    get_weth()


def get_weth():
    """
    Mints WETH from deposited ETH
    """
    # ABI
    # Address
    account = get_account()
    weth = interface.IWeth(config["networks"][network.show_active()])

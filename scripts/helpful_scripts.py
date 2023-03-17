from brownie import network, accounts, config

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

# this makes out get_account function more flexible 
def get_account(index=None, id=None):
    # ways to get accounts; accounts[0], accounts.add(), accounts.load()
    if index:
        return accounts[index]
    elif network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in FORKED_LOCAL_ENVIRONMENTS:
        return accounts[0]
    elif id:
        return accounts.load(id)
    else:
        return accounts.add(config["wallets"]["from_key"])
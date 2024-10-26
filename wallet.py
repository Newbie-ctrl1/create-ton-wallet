from tonsdk.contract.wallet import Wallets, WalletVersionEnum
from tonsdk.utils import to_nano

def create_wallet():
    mnemonics, public_key, private_key, wallet = Wallets.create(
        version=WalletVersionEnum.v3r2,
        workchain=0,
    )
    return mnemonics, wallet.address.to_string(True, True, True)

def create_multiple_wallets(num_wallets):
    wallets = []
    for _ in range(num_wallets):
        mnemonics, address = create_wallet()
        wallets.append((mnemonics, address))
    return wallets

def main():
    num_wallets = int(input("Berapa banyak wallet yang ingin Anda buat? "))
    wallets = create_multiple_wallets(num_wallets)
    
    with open('key.txt', 'w') as f:
        for idx, (mnemonics, address) in enumerate(wallets, 1):
            f.write(f"Wallet {idx}:\n")
            f.write(f"Address: {address}\n")
            f.write(f"Mnemonics: {' '.join(mnemonics)}\n\n")
    
    print(f"{num_wallets} wallet telah dibuat dan disimpan di key.txt")

if __name__ == "__main__":
    main()
import asyncio
import pandas as pd
from aiofile import async_open
from tonsdk.contract.wallet import WalletVersionEnum, Wallets
from tonsdk.crypto import mnemonic_new
from tonsdk.utils import bytes_to_b64str

class AsyncTonWalletGenerator:
    def __init__(self, wallet_amounts):
        self.wallet_amounts = wallet_amounts

    async def generate_wallet(self):
        wallet_workchain = 0
        wallet_version = WalletVersionEnum.v4r2  # Menggunakan versi wallet v4R2
        wallet_mnemonics = mnemonic_new()

        _mnemonics, _pub_k, _priv_k, wallet = Wallets.from_mnemonics(
            wallet_mnemonics, wallet_version, wallet_workchain)

        query = wallet.create_init_external_message()
        bytes_to_b64str(query["message"].to_boc(False))

        user_friendly_address = wallet.address.to_string(is_user_friendly=True)

        # Memodifikasi alamat untuk mengganti karakter sesuai permintaan
        formatted_address = user_friendly_address.replace('+', '_').replace('/', '-')

        return formatted_address, wallet_mnemonics

    async def write_wallets_to_files(self):
        addresses = []
        mnemonics = []

        tasks = [self.generate_wallet() for _ in range(self.wallet_amounts)]
        wallets = await asyncio.gather(*tasks)

        for index, (address, mnemonic) in enumerate(wallets):
            addresses.append(address)
            mnemonics.append((f"Wallet {index + 1}: {address}\nMnemonic: {' '.join(mnemonic)}"))

        # Write addresses to address.txt
        async with async_open("address.txt", 'w') as address_file:
            await address_file.write('\n'.join(addresses))

        # Write mnemonics and addresses to key.txt
        async with async_open("key.txt", 'w') as key_file:
            await key_file.write('\n\n'.join(mnemonics))

    async def run(self):
        await self.write_wallets_to_files()

if __name__ == "__main__":
    try:
        # Meminta input dari pengguna untuk jumlah dompet yang ingin dibuat
        jumlah_dompet = int(input("Masukkan jumlah dompet yang ingin dibuat: "))
        
        generator = AsyncTonWalletGenerator(wallet_amounts=jumlah_dompet)
        
        print(f"Generating {jumlah_dompet} wallets...")
        
        asyncio.run(generator.run())
        
        print("Wallets generated successfully!")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka yang benar.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Async TON Wallet Generator
This Python script generates multiple TON (The Open Network) wallets asynchronously. It uses the tonsdk library for wallet creation and outputs wallet addresses and mnemonic phrases into two separate files: `address.txt` and `key.txt`.

## Features

- **Asynchronous Wallet Generation**: Utilizes asynchronous programming for efficient wallet generation.
- **TON Wallet Version v4R2**: Creates wallets using the v4r2 wallet version.
- **Address Formatting**: Wallet addresses are formatted by replacing `+` with `_` and `/` with `-`.
- **Output to Files**: The generated wallet addresses are stored in `address.txt` and the corresponding mnemonics and addresses are saved in `key.txt`.

## Requirements

Before running the script, ensure you have the necessary dependencies installed:

## Prerequisites
- **Python 3.7+**
- **Install the required libraries by running**:
 ```bash
 pip install tonsdk aiofile pandas
 ```
## Usage

1. Clone this repository or copy the script to your local environment.
2. Run the script using Python.
 ### Example:
 ``` bash
  python wallet.py
 ```
3. Input the number of wallets you want to generate when prompted.
4. The script will generate the wallets and save the results in `address.txt` and `key.txt`.

## Output Files

`address.txt`: Contains the generated wallet addresses.
`key.txt`: Contains the wallet addresses and their corresponding mnemonic phrases.

## Sample Output
- **address.txt**:
 ```
 kQDBwl4YkUzZjHSpP1k5KUpRvw2jj1PQtfHPu08eCvnqopMl
 kQBQF4xGnWZmKnUdr9ESkY_StUVvjCE63a4H3VFsioquOsPi
 ```
- **key.txt**:

 ```yaml
 Wallet 1: kQDBwl4YkUzZjHSpP1k5KUpRvw2jj1PQtfHPu08eCvnqopMl
 Mnemonic: word1 word2 word3 ... word24

 Wallet 2: kQBQF4xGnWZmKnUdr9ESkY_StUVvjCE63a4H3VFsioquOsPi
 Mnemonic: word1 word2 word3 ... word24
 ```

## Example Usage

When you run the script, you'll be asked to input the number of wallets you'd like to generate. After providing the number, the script will generate the specified number of wallets asynchronously and save the addresses and mnemonics to the respective files.

 ```yaml
 Masukkan jumlah dompet yang ingin dibuat: 2
 Generating 2 wallets...
 Wallets generated successfully!
 ```
## Error Handling
Invalid Input: If you input something other than a number, the script will prompt an error message:

 ```
Input tidak valid. Harap masukkan angka yang benar.
 ```
General Exceptions: Any other errors will be captured and displayed with the corresponding error message.
 
## Contribution
Feel free to fork the repository and submit pull requests for any improvements or additional features.

## License
This project is licensed under the MIT License.

 

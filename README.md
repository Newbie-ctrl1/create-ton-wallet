# Wallet Generator - TON SDK

A Python script to generate multiple wallets for the TON blockchain using the `tonsdk` library.

## Features
- Create wallets for the TON blockchain using the v3r2 wallet version.
- Save wallet addresses and mnemonics to a `key.txt` file.
- Option to send wallet data to a server endpoint via HTTP POST request (using `requests`).

## Requirements

- Python 3.x
- `tonsdk` library
- `requests` library

## Installation

 1. Clone the repository or download the script.
  ```bash
  git clone https://github.com/your-repo/wallet-generator.git
  cd wallet-generator
  ```
 2. Install the required dependencies.
  ```bash
  pip install tonsdk requests
  ```
## Usage
 1. Run the script:

  ```bash
  python wallet_generator.py
  ```
 2. Input the number of wallets you want to create.
 3. The generated wallets' mnemonics and addresses will be saved in a file called key.txt.
 4. If you have a server or API endpoint that accepts wallet data, you can modify the script to send the wallet information using requests by updating the send_to_server function with your endpoint.

## Example of Output

The key.txt file will contain the wallet data in the following format:

  ```yaml
  Wallet 1:
  Address: EQC...
  Mnemonics: word1 word2 word3 ... word24
  
  Wallet 2:
  Address: EQC...
  Mnemonics: word1 word2 word3 ... word24
  ```

## Sending Wallet Data to a Server

If you want to send the generated wallet data to a remote server, make sure to include your server's endpoint in the send_to_server function inside the script.

 ## Example:

```python
  def send_to_server(wallet_data):
      url = "https://your-api-endpoint.com/wallets"
      response = requests.post(url, json=wallet_data)
      if response.status_code == 200:
          print("Data sent successfully!")
      else:
          print("Failed to send data. Status code:", response.status_code)
  ```
## License
This project is licensed under the MIT License.

## Explanation
-**Requirements**: Explains the necessary libraries and how to install them.

-**Usage**: Describes how to run the script and what the expected output is.

-**Example Usage**: Provides a demonstration of how the script interacts.

-**Contribution and License**: Standard sections for an open-source project.

You can modify the server URL section in the script and explain how it works according to the API or server you intend to use.

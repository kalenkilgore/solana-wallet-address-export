# 🪙 solana-wallet-address-export

**Easily Export Your Phantom Solana Wallet Addresses with One Simple Script**

Tired of manually copying your Solana wallet addresses one by one from your Phantom wallet? This script does it all for you, automagically. Just enter your seed phrase (securely!), tell it how many addresses you want, and boom—they're neatly saved into a file.

---

## 💻 Installation

### Step 1: Install Python

Make sure Python 3.8 or later is installed:

- **Mac**: 
  - Install Homebrew if you haven't already:
  ```bash
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  ```
  - Then install Python:
  ```bash
  brew install python
  ```

- **Linux (Ubuntu)**:
  ```bash
  sudo apt update
  sudo apt install python3 python3-pip
  ```

### Step 2: Install Solana CLI

- **Mac and Linux:**
  ```bash
  sh -c "$(curl -sSfL https://release.solana.com/v1.18.12/install)"
  ```
  After installation, restart your terminal and confirm installation:
  ```bash
  solana --version
  ```

### Step 3: Install Python Dependencies

Run:
```bash
pip3 install pexpect
```

---

## 🚀 How to Run the Script

### Step-by-Step Instructions

1. **Download the script**:
   ```bash
   git clone https://github.com/kalenkilgore/solana-wallet-address-export.git
   cd solana-wallet-address-export
   ```

2. **Run the script**:
   ```bash
   python3 solana-address-export.py
   ```

3. **When prompted**:
   - Securely enter your Phantom wallet seed phrase (it won't show on the screen—this is intentional!).
   - Enter the number of wallet addresses you want to export.

4. **Done!**
   - The script prints addresses to the screen and saves them to `addresses.txt` in the current directory.

---

## 🔒 Security Tips

- **Never share your seed phrase** with anyone.
- **Store `addresses.txt` securely.**

---

## 🤝 Contribute

Feel free to improve this script. Pull requests welcome!

---

## 📄 License

MIT License—Use, modify, and enjoy!


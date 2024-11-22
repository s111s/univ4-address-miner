# Uniswap V4 Address Challenge Miner

This repository contains tools to participate in the **Uniswap V4 Address Challenge** by mining salts to achieve a higher score. The tools include Python scripts for generating and verifying salts, and a Solidity contract for on-chain verification.

---

## Repository Contents

- **`univ4-addr-miner.py`**  
  A Python script used to mine salts by iterating through different values to achieve higher scores.  
  **Usage**:  
  ```bash
  $ python3 univ4-addr-miner.py
  ```

  You can optimize the mining process by modifying the salt_int parameter within the script.

- **`univ4-verify-salt.py`**
  A Python script to verify if a generated salt is valid and its associated score.
  
  Usage:
  ```bash
  $ python3 univ4-verify-salt.py [SALT]
  ```

  Example:
  ```bash
  $ python3 univ4-verify-salt.py 0x72bed203c9a5eff37e1f55be91f742def6e0e5c7ebf3d141f7d8a81436e3f4f0
  ```

- **`CheckScore.sol`**
  A Solidity smart contract to verify the salt's score directly on the blockchain. This ensures that the on-chain verification matches the Python scripts.

## Prerequisites

- Python 3: Ensure Python 3.x is installed on your system.

## Installation

- Clone the repository:
```bash
$ git clone https://github.com/your-username/univ4-address-challenge-miner.git
$ cd univ4-address-challenge-miner
```

- Install Python dependencies if required:
```bash
$ pip install -r requirements.txt
```
from web3 import Web3

# Constants
deployer = "0x48E516B34A1274f49457b9C6182097796D0498Cb"
initcode_hash = "0x94d114296a5af85c1fd2dc039cdaa32f1ed4b0fe0868f02d888bfc91feb645d9"

def compute_address(deployer, salt, initcode_hash):
    deployer_bytes = bytes.fromhex(deployer[2:])
    salt_bytes = Web3.to_bytes(salt)
    initcode_hash_bytes = bytes.fromhex(initcode_hash[2:])
    data = b'\xff' + deployer_bytes + salt_bytes + initcode_hash_bytes
    return "0x" + Web3.keccak(data).hex()[-40:]

def score_address(address):
    score = 0
    if address.startswith("0x"):
        address = address[2:]
    
    leading_zeros = len(address) - len(address.lstrip("0"))
    score += leading_zeros * 10
    
    if address[leading_zeros:leading_zeros + 4] == "4444":
        score += 40
        if len(address) > leading_zeros + 4 and address[leading_zeros + 4] != "4":
            score += 20
    
    if address.endswith("4444"):
        score += 20
    
    score += address.count("4")
    
    return score

def generate_next_salt(current_salt):
    # Convert bytes to integer
    salt_int = int.from_bytes(current_salt, 'big')
    # Increment (can be changed to your wanted number)
    salt_int += 13187*218762640769843579162539339882768668739731745229660067529421
    # Convert back to bytes
    return salt_int.to_bytes(32, 'big')

# Mining process
best_score = 0
best_address = ""
best_salt = b'\x00' * 32

# Start with all zeros
salt = b'\x00' * 32

while int.from_bytes(salt, 'big')<=115792089237316195423570985008687907853269984665640564039457584007913129639935:
    try:
        address = compute_address(deployer, salt, initcode_hash)
        current_score = score_address(address)
        
        if current_score > best_score:
            best_score = current_score
            best_address = address
            best_salt = salt
            print(f"New best score: {best_score}")
            print(f"Address: {best_address}")
            print(f"Salt: 0x{best_salt.hex()}")
            print("-" * 50)
        
        # Generate next salt in sequence
        salt = generate_next_salt(salt)
        
    except KeyboardInterrupt:
        print("\nMining stopped by user")
        print(f"Final best score: {best_score}")
        print(f"Final best address: {best_address}")
        print(f"Final best salt: 0x{best_salt.hex()}")
        break
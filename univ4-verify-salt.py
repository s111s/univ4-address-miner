from web3 import Web3
import sys

arg=sys.argv[1]

if(arg[:2]=="0x"):
    arg = arg[2:]

# Constants
deployer = "0x48E516B34A1274f49457b9C6182097796D0498Cb"
initcode_hash = "0x94d114296a5af85c1fd2dc039cdaa32f1ed4b0fe0868f02d888bfc91feb645d9"

# Helper function to compute CREATE2 address
def compute_address(deployer, salt, initcode_hash):
    deployer_bytes = bytes.fromhex(deployer[2:])
    salt_bytes = Web3.to_bytes(salt)
    initcode_hash_bytes = bytes.fromhex(initcode_hash[2:])
    data = b'\xff' + deployer_bytes + salt_bytes + initcode_hash_bytes
    return "0x" + Web3.keccak(data).hex()[-40:]

# Verification function
def verify_salt(salt):
    # Check salt length
    if len(salt) != 32:
        return False, "Salt must be 32 bytes long"
    
    # Check for constant salt
    if all(c == salt[0] for c in salt):
        return False, "Salt cannot be a constant value"
    
    # Compute the CREATE2 address
    address = compute_address(deployer, salt, initcode_hash)
    return True, f"Valid salt, CREATE2 address: {address} \nAddress Score: {score_address(address)} "

def score_address(address):
    score = 0
    if address.startswith("0x"):
        address = address[2:]
    
    # Leading zeros
    leading_zeros = len(address) - len(address.lstrip("0"))
    score += leading_zeros * 10
    
    # Check for "4444" pattern
    if address[leading_zeros:leading_zeros + 4] == "4444":
        score += 40
        # First nibble after "4444" is not "4"
        if len(address) > leading_zeros + 4 and address[leading_zeros + 4] != "4":
            score += 20
    
    # Last four nibbles are "4"
    if address.endswith("4444"):
        score += 20
    
    # Count extra "4"s
    score += address.count("4")
    
    return score

# Example usage
salt = bytes.fromhex(arg)
is_valid, message = verify_salt(salt)
print(message)
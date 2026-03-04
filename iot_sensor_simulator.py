import time
from web3 import Web3
import requests

# 1. Connect to the Live Sepolia Network
infura_url = "https://sepolia.drpc.org"
web3 = Web3(Web3.HTTPProvider(infura_url))

print(f"Connected to Sepolia Testnet: {web3.is_connected()}")

# 2. Your Credentials
wallet_address = "0xa07275Dc71cB26Ecc6CD701d56410A63956D1E25"
# PASTE YOUR PRIVATE KEY BACK IN HERE (I removed it for your security!):
private_key = "YOUR PRIVATE KEY" 

# 3. Contract Keys
contract_address = "0xfF35aFE64bd4434c73528E2be989E0860C87c52D"

abi = [
    {
        "inputs": [
            {"internalType": "address", "name": "_receiver", "type": "address"},
            {"internalType": "string", "name": "_cargoName", "type": "string"},
            {"internalType": "int256", "name": "_maxTemperature", "type": "int256"}
        ],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "inputs": [{"internalType": "int256", "name": "_newTemp", "type": "int256"}],
        "name": "updateTemperature",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [], "name": "cargoName", "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view", "type": "function"
    },
    {
        "inputs": [], "name": "currentTemperature", "outputs": [{"internalType": "int256", "name": "", "type": "int256"}],
        "stateMutability": "view", "type": "function"
    },
    {
        "inputs": [], "name": "maxTemperature", "outputs": [{"internalType": "int256", "name": "", "type": "int256"}],
        "stateMutability": "view", "type": "function"
    },
    {
        "inputs": [], "name": "shipmentStatus", "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view", "type": "function"
    }
]

# Build the connection to the contract
contract = web3.eth.contract(address=contract_address, abi=abi)

# 4. The Digital Twin Logic (Simulating a Global Cold Chain)
def update_temperature_on_chain(new_temp):
    print(f"\n📡 Beaming new temperature ({new_temp}°C) to blockchain...")
    
    # Get the pending transaction number (FIXED)
    nonce = web3.eth.get_transaction_count(wallet_address, 'pending')
    
    # Build the transaction payload
    tx = contract.functions.updateTemperature(new_temp).build_transaction({
        'chainId': 11155111, # Sepolia Chain ID
        'gas': 3000000,
        'maxFeePerGas': web3.to_wei('10', 'gwei'),
        'maxPriorityFeePerGas': web3.to_wei('2', 'gwei'),
        'nonce': nonce,
    })

    # Sign the transaction with your Private Key
    signed_tx = web3.eth.account.sign_transaction(tx, private_key=private_key)
    
    # Send it to the global network!
    tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
    
    print(f"🚀 Transaction sent! Hash: {web3.to_hex(tx_hash)}")
    print("⏳ Waiting for global network confirmation (takes ~15 seconds)...")
    
    # Wait for the network to officially log it
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"✅ Transaction successful! Logged in Block: {receipt.blockNumber}")
    
    # Ask the contract what the official status is now
    status = contract.functions.shipmentStatus().call()
    print(f"📦 Official Contract Status: {status}")
    
    # --- NEW: The AKies Global n8n Alert System ---
    if "SPOILED" in status:
        print("🚨 BREACH DETECTED! Alerting AKies Control Tower...")
        
        webhook_url = "https://n8n.vedsan8n52002.xyz/webhook/cargo-alert"
        
        payload = {
            "contract": contract_address,
            "recorded_temp": new_temp,
            "status": status,
            "cargo": "Pharmaceuticals"
        }
        
        try:
            requests.post(webhook_url, json=payload)
            print("📨 Alert successfully delivered to n8n!")
        except Exception as e:
            print(f"⚠️ Failed to reach n8n: {e}")
    # ---------------------------------
    print("-" * 40)

# 5. Run the Simulation
print("Starting AKies Pharma Cold Chain Digital Twin...")
current_temp = -22 

for i in range(3):
    update_temperature_on_chain(current_temp)
    current_temp += 3 
    time.sleep(5)

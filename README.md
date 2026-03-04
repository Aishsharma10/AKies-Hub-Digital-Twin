# 🌐 AKies Hub: Web3 Digital Twin & Cold Chain Optimizer

An automated, blockchain-integrated supply chain management system that bridges a client-facing frontend with decentralized smart contracts and simulated IoT telemetry. 

Built as a proof-of-concept for enterprise logistics, this system ensures zero-trust visibility and automated penalty enforcement for global cold chain operations (e.g., Pharmaceuticals, Perishable Foods).

## 🏗️ System Architecture
This project utilizes a microservices architecture to fully automate the dispatch, monitoring, and tracking of sensitive global cargo.

1. **Client Interface:** A custom web dashboard capturing cargo specifications (Name, Max Temperature threshold, Receiver Wallet Address).
2. **Integration Middleware (n8n):** - Captures REST API payloads from the frontend.
   - Stages order data into a centralized cloud database (Google Sheets) with a `Pending` status.
   - Orchestrates automated email alerts to stakeholders upon contract breaches.
3. **Web3 Engine (Python):**
   - Autonomously polls the database for pending logistics orders.
   - Forges and deploys a customized Ethereum Smart Contract to the Sepolia Testnet for each unique shipment.
   - Pushes the immutable blockchain contract address back to the cloud database.
4. **IoT Digital Twin:** Simulates real-time truck telemetry, beaming live temperature readings directly to the blockchain to verify contract compliance.

## 📂 Core Components

* 📄 **`index.html`** - The Client Dispatch Dashboard. A sleek, asynchronous frontend that posts cargo requirements to the n8n ingestion gateway.
* 🧠 **`TransitLogger.sol`** - The immutable logic. A Solidity smart contract that permanently stores the cargo's parameters and automatically calculates breaches if temperature thresholds are exceeded.
* ⚙️ **`deploy_contract.py`** - The Background Worker. A Python script that bridges Web2 (Google Sheets via n8n) and Web3 (Ethereum via Web3.py), deploying contracts dynamically.
* 📡 **`iot_sensor_simulator.py`** - The Physical-to-Digital Bridge. Simulates an IoT thermometer inside a transit vehicle, sending live data to the blockchain and triggering emergency n8n email webhooks if cargo spoils.

## 🛠️ Tech Stack
* **Frontend:** HTML5, CSS3, JavaScript (Fetch API)
* **Middleware/Automation:** n8n (Webhook ingestion, JSON mapping, Google Sheets API, Gmail API)
* **Backend:** Python 3, `requests` library
* **Blockchain:** Web3.py, Infura RPC, Ethereum Sepolia Testnet, Solidity

## ⚙️ Key Features
* **Zero-Touch Deployment:** Once a client submits an order, the entire pipeline (database entry, blockchain deployment, and database update) runs autonomously.
* **Immutable State Tracking:** Shipment parameters are hardcoded into the blockchain, preventing tampering during global transit.
* **Automated SLA Enforcement:** If the IoT sensor logs a temperature above the maximum threshold, the smart contract state changes to `SPOILED` and the system autonomously fires emergency email alerts to the supply chain managers.

## 🚀 How to Run the Simulation
1. Serve `index.html` to capture order inputs.
2. Ensure the n8n webhook workflows are active to catch the payload.
3. Run `python deploy_contract.py` to trigger the Web3 deployment sequence.
4. Run `python iot_sensor_simulator.py` and input temperature readings to test the smart contract's breach logic and trigger the automated email alerts.
2. Ensure the n8n webhook workflows are active to catch the payload.
3. Run `python deploy_contract.py` to trigger the Web3 deployment sequence.

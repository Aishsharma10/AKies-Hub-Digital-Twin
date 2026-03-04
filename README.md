# AKies Hub: Digital Twin & Web3 Logistics Optimizer 🌐📦

An automated, blockchain-integrated supply chain management system that bridges client-facing frontends with decentralized smart contracts. 

## 🏗️ System Architecture
This project utilizes a microservices architecture to fully automate the dispatch and tracking of sensitive global cargo. 

1. **Client Interface:** A custom web form capturing cargo specifications (Name, Max Temperature threshold, Receiver Wallet Address).
2. **Integration Middleware (n8n):** - Captures POST requests from the web frontend via CORS-enabled webhooks.
   - Automatically stages order data into a centralized cloud database (Google Sheets) with a `Pending` status.
3. **Web3 Engine (Python):**
   - Autonomously polls the database for pending logistics orders.
   - Forges and deploys a customized Ethereum Smart Contract to the Sepolia Testnet for each unique shipment.
   - Pushes the immutable blockchain contract address back through an n8n webhook to instantly update the cloud database to `Deployed`.

## 🛠️ Tech Stack
* **Frontend:** HTML/CSS/JavaScript (Asynchronous Fetch API)
* **Middleware/Automation:** n8n (Webhook ingestion, JSON mapping, Google Sheets API)
* **Backend:** Python 3, `requests` library
* **Blockchain:** Web3.py, Infura RPC, Ethereum Sepolia Testnet, Solidity (Smart Contract)

## ⚙️ Core Features
* **Zero-Touch Deployment:** Once a client submits an order, the entire pipeline (database entry, blockchain deployment, and database update) runs autonomously.
* **Immutable State Tracking:** Shipment parameters (temperature thresholds, receiver identity) are hardcoded into the blockchain, preventing tampering during global transit.
* **Asynchronous Webhooks:** Utilizes dedicated testing and production API endpoints to handle data streams without pipeline bottlenecks.

## 🚀 How to Run
1. Serve the `index.html` file to capture order inputs.
2. Ensure the n8n webhook workflows are active to catch the payload.
3. Run `python deploy_contract.py` to trigger the Web3 deployment sequence.

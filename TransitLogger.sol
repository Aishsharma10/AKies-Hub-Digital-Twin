// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract TransitLogger {
    
    // 1. The Parties
    address public sender;
    address public receiver;
    
    // 2. The Dynamic Cargo Variables
    string public cargoName;
    int public maxTemperature; // Changed to 'int' so it can handle negative numbers!
    int public currentTemperature;  
    
    string public shipmentStatus;
    
    // 3. The Setup (The customer sets the rules when they deploy!)
    constructor(address _receiver, string memory _cargoName, int _maxTemperature) {
        sender = msg.sender; 
        receiver = _receiver;  
        cargoName = _cargoName;
        maxTemperature = _maxTemperature;
        shipmentStatus = "In Transit";
    }

    // 4. The Automated Logic
    function updateTemperature(int _newTemp) public {
        currentTemperature = _newTemp; 
        
        if (currentTemperature > maxTemperature) {
            shipmentStatus = "SPOILED: Contract Breached";
        } else {
            shipmentStatus = "In Transit: Temperature Optimal";
        }
    }
}

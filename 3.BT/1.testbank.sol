// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Bank{

    mapping(address => uint256) balances;

    function DepositMoney(uint256 amount)public {
        require(amount>=0 , "Amount should greater than 0");
        balances[msg.sender]=balances[msg.sender]+amount;
    }

    
    function WithdrawlMoney(uint256 amount)public {
        require(amount<=balances[msg.sender] , "Insuffient balance");
        balances[msg.sender]=balances[msg.sender]-amount;
    }

    function Showbalance() public view returns (uint256){
        return balances[msg.sender];
    }
}


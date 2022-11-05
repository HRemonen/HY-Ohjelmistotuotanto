*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Register Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kolle  kalle123
    Output Should Contain   New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  k  kalle123
    Output Should Contain   Username must be atleast 3 characters long

Register With Valid Username And Too Short Password
    Input Credentials  kallela  k
    Output Should Contain   Password must be atleast 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kallela  kallelansalasana
    Output Should Contain   Password must contain numbers and letters

*** Keywords ***
Create User And Input Register Command
    Create User  kalle  kalle123
    Input Register Command
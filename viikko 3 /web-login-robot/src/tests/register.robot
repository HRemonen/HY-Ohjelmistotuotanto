*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  Hene
    Set Password  Henelius123
    Set Confirmation  Henelius123
    Submit Register
    Register Should Succeed


Register With Too Short Username And Valid Password
    Set Username  h
    Set Password  Henelius
    Set Confirmation  Henelius
    Submit Register
    Register Should Fail With Message  Username must be atleast 3 characters long

Register With Valid Username And Too Short Password
    Set Username  heneliisa
    Set Password  asdf
    Set Confirmation  asdf
    Submit Register
    Register Should Fail With Message  Password must be atleast 8 characters long

Register With Nonmatching Password And Password Confirmation
    Set Username  heneliisa
    Set Password  heneliisan123
    Set Confirmation  eneliisan123
    Submit Register
    Register Should Fail With Message  Passwords must match

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Login

Submit Register
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Confirmation
    [Arguments]  ${confirmation}
    Input Password  password_confirmation  ${confirmation}

*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
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

Login After Successful Registration
    Set Username  testiHene
    Set Password  Henelius123
    Set Confirmation  Henelius123
    Submit Register
    Register Should Succeed

    Go To Login Page
    Set Username  testiHene
    Set Password  Henelius123
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  testiHeneliisa
    Set Password  Henelius123123
    Set Confirmation  Henelius123
    Submit Register
    Register Should Fail With Message  Passwords must match

    Go To Login Page
    Set Username  testiHeneliisa
    Set Password  Henelius123123
    Submit Credentials
    Login Should Fail With Message  Invalid username or password
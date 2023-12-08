*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py

*** Variables ***
${BROWSER}        Chrome
${SERVER}  localhost:5000

${DELAY}  0.2 seconds
${HOME_URL}  http://${SERVER}
${REFERENCE_URL}  http://${SERVER}/reference


*** Keywords ***
# Open Application
#     Open Browser    ${HOME_URL}    ${BROWSER}
#     Maximize Browser Window

# Close Application
Close Application
    Close Browser

Open And Configure Browser
    ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    Call Method    ${options}    add_argument    --no-sandbox
    # Call Method  ${options}  add_argument  --headless
    Open Browser  browser=chrome  options=${options}
    Set Selenium Speed  ${DELAY}


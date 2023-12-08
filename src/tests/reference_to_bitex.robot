*** Settings ***
Resource          resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Application



*** Test Cases ***

Reference to Bibtex-file
    Go To          ${HOME_URL}
    Click Button    name:bibtex
    Download Succeeds With Message  Downloaded Bibtex-file


*** Keywords ***

Download Succeeds With Message
    [Arguments]  ${message}
    Page Should Contain  ${message}
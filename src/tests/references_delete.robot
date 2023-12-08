*** Settings ***
Resource          resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Application



*** Test Cases ***

Delete Book
    Go To          ${HOME_URL}
    Click Button  Delete
    Click Button  Confirm delete
    Delete Reference Succeeds With Message  Deleted book from database


*** Keywords ***

Delete Reference Succeeds With Message
    [Arguments]  ${message}
    Page Should Contain  ${message}
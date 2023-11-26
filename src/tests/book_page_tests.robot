*** Settings ***
Resource          resource.robot

*** Test Cases ***
Test Book Page GET
    Open Application
    Go To          ${URL}/book
    Page Should Contain    Book Page
    Close Application

Test Book Page POST
    Open Application
    Go To          ${URL}/book
    Input Text    name=title     Robot Framework
    Input Text    name=author    Test Author
    Input Text    name=year      2023
    Input Text    name=publisher Test Publisher
    Input Text    name=url        https://example.com
    Click Element name=submit
    Location Should Be    ${URL}/
    Close Application
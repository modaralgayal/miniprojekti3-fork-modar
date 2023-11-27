*** Settings ***
Resource          resource.robot
Suite Setup  Open And Configure Browser
# Suite Teardown  Close Application
# Test Template  Add Book

*** Test Cases ***
Test Book Page GET
    # Open Application
    Go To          ${BOOK_URL}
    Page Should Contain    Books
    # Close Application

Test Book Page POST
    # Open Application
    Go To          ${HOME_URL}
    # Select the "book" option from the dropdown
    Click Element  id=ref_type
    Click Element  xpath=//option[@value='book']
    Set Title  Robot Framework
    Set Author  Test Author
    Set Year  2023
    Set Publisher  Test Publisher
    Set URl  https://example.com
    Submit
    Location Should Be    ${HOME_URL}/
    # Close Application


*** Keywords ***
Submit 
    Click Button  Add Book

Set Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Set Author
    [Arguments]  ${author}
    Input Text  author  ${author}

Set Year
    [Arguments]  ${year}
    Input Text  year  ${year}

Set Publisher
    [Arguments]  ${publisher}
    Input Text  publisher  ${publisher}


Set Url
    [Arguments]  ${url}
    Input Text  url  ${url}

Add book  
    Go To  ${BOOK_URL}
    Set Title  Robot Framework
    Set Author Test Author
    Set Year  2023
    Set Publisher  Test Publisher
    Set URl  https://example.com
    Submit
    Location Should Be    ${BOOK_URL}/


    
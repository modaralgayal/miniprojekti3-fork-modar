*** Settings ***
Resource          resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Application



*** Test Cases ***


Add A Book
    Go To          ${HOME_URL}
    Select From List By Value  id=ref_type  book
    Input Text  id=b_title  Robot Book
    Input Text  id=b_author  Book Author
    Input Text  id=b_year  2022
    Input Text  id=b_publisher  Book Publisher
    Input Text  id=b_url  invalid input
    Click Button  Add Book
    Add Reference Should Fail With Message  Please enter a URL.

*** Keywords ***

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

Add Reference Should Fail With Message
    [Arguments]  ${message}
    Page Should Contain  ${message}
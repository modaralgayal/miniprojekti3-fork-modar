*** Settings ***
Resource          resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Application
# Test Template  Add Book


*** Test Cases ***

Go To Front Page
    Go To          ${HOME_URL}
    Page Should Contain    Books
    Page Should Contain    Articles
    Page Should Contain    Inproceedings


Add A Book
    Go To          ${HOME_URL}
    # Select the "book" option from the dropdown
    Select From List By Value  id=ref_type  book
    Input Text  id=b_title  Robot Book
    Input Text  id=b_author  Book Author
    Input Text  id=b_year  2022
    Input Text  id=b_publisher  Book Publisher
    Input Text  id=b_url  Book Url
    Click Button  Add Book
    Add Reference Succeeds With Message  Robot Book


Add An Article
    Go To          ${HOME_URL}
    # Select the "article" option from the dropdown
    Select From List By Value  id=ref_type  article
    Input Text  id=a_title  Robot Article
    Input Text  id=a_author  Article Author
    Input Text  id=a_year  2022
    Input Text  id=a_journal  Article Journal
    Input Text  id=a_url  Article Url
    Click Button  Add Article
    Add Reference Succeeds With Message  Robot Article

Add A Inproceeding
    Go To          ${HOME_URL}
    # Select the "inproceeding" option from the dropdown
    Select From List By Value  id=ref_type  inproceeding
    Input Text  id=i_title  Robot Inproceeding
    Input Text  id=i_author  Inproceeding Author
    Input Text  id=i_year  2021
    Input Text  id=i_url  Inproceeding Url
    Click Button  Add Inproceeding
    Add Reference Succeeds With Message  Robot Inproceeding

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


Set Journal
    [Arguments]  ${journal}
    Input Text  journal  ${journal}


Add Reference Succeeds With Message
    [Arguments]  ${message}
    Page Should Contain  ${message}
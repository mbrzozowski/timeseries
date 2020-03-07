*** Settings ***
Documentation    End to end timeseries tests
Resource         e2e/e2e_keywords.robot
Suite Setup      Setup All Tests
Suite Teardown   Disconnect Database

*** Test Cases ***
Timeseries Service Doc Endpoint Should Be Available    
    Doc Endpoint Should Be Available

Timeseries Service Health Endpoint Should Be Available
    Health Endpoint Should Be Available

Timeseries Service Should Handle Incorrect Data
    Post Incorrect Data To Timeseries Service
    Status Should Be 400

Timeseries Service Should Handle Correct Data
    Post Correct Data To Timeseries Service
    Status Should Be 201

Timeseries Service Should Get Statistics
    Get Timeseries Service Statistics
    Status Should Be 200
    Field sum Should Be Equal 7.0
    Field avg Should Be Equal 2.33333337306976

Stats Service Should Get Statistics
    Get Stats Service Statistics
    Status Should Be 200
    Field sum Should Be Equal 7.0
    Field avg Should Be Equal 2.33333337306976

Database Should Have Data
    Table timeseries Should Exist
    Table timeseries Column name Should Be character varying
    Table timeseries Column t Should Be integer
    Table timeseries Column v Should Be real
    Table timeseries Count Should Be 5
    For Timestamp 13515552 Value Should Be Equal 2.4




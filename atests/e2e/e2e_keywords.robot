*** Settings ***
Documentation    End to end timeseries keywords
Library          RequestsLibrary
Library          PostgresLibrary.py
Library          OperatingSystem
Resource         e2e_variables.robot

*** Keywords ***
Connect To Database
    Connect Postgres    ${POSTGRES_CON_STR}

Disconnect Database
    Disconnect Postgres

Setup Timeseries Service Session
    Create Session    timeseries    ${TIMESERIES_SERVICE_API_URL}

Setup status_code Service Session
    Create Session    stats    ${STATS_SERVICE_API_URL}

Setup All Tests
    Connect To Database
    Setup Timeseries Service Session
    Setup status_code Service Session

Doc Endpoint Should Be Available
    ${response}    Get Request    timeseries    /doc
    Should Be Equal As Integers    ${response.status_code}    200
    Should Contain    ${response.text}    swagger

Health Endpoint Should Be Available
    ${response}    Get Request    timeseries    /health/
    Should Be Equal As Integers    ${response.status_code}    200
    ${response_json}    Set Variable    ${response.json()}
    Should Be Equal As Strings    ${response_json['status']}    OK

Post Correct Data To Timeseries Service
    Post Data To Timeseries Service    ${CORRECT_DATA_FILE}

Post Incorrect Data To Timeseries Service
    Post Data To Timeseries Service    ${INCORRECT_DATA_FILE}

Post Data To Timeseries Service
    [Arguments]    ${file}
    ${data}   Get File    ${file}
    ${headers}    Create Dictionary    Content-Type=application/json
    ${response}    Post Request    timeseries    /timeseries/    data=${data}    headers=${headers}
    Set Test Variable    ${response}

Status Should Be ${code}
    Should Be Equal As Integers    ${response.status_code}    ${code}

Get Timeseries Service Statistics
    ${response}    Get Request    timeseries    /timeseries/?from=13515551&to=13515553
    Set Test Variable    ${response}

Field ${field} Should Be Equal ${value}
    ${response_json}    Set Variable    ${response.json()}
    Should Be Equal As Numbers    ${response_json['${field}']}    ${value}

Get Stats Service Statistics
    ${response}    Get Request    stats    /stats/?from=13515551&to=13515553
    Set Test Variable    ${response}

Table ${table} Should Exist
    ${result}    Query Postgres    select tablename from pg_tables where schemaname='public'
    ${expected}     Create Dictionary    tablename=${table}
    Should Contain    ${result}    ${expected}

Table ${table} Column ${column} Should Be ${data_type}
    ${result}    Query Postgres    select column_name, data_type from information_schema.columns where table_name='${table}'
    ${expected}     Create Dictionary    column_name=${column}    data_type=${data_type}
    Should Contain    ${result}    ${expected}

Table ${table} Count Should Be ${num}
    ${result}    Query Postgres    select count(*) as cnt from timeseries
    Should Be Equal As Integers    ${result['cnt']}    ${num}

For Timestamp ${t} Value Should Be Equal ${v}
    ${result}    Query Postgres    select v from timeseries where t='${t}'
    Should Be Equal As Numbers    ${result[0]['v']}    ${v}
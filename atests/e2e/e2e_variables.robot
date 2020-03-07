*** Variables ***
${POSTGRES_CON_STR}                postgresql://time:series@localhost:5432/stats_db
${TIMESERIES_SERVICE_API_URL}      http://localhost:8585/api/v1
${STATS_SERVICE_API_URL}           http://localhost:8686/api/v1
${INCORRECT_DATA_FILE}             ${CURDIR}/fixtures/incorrect_data.json
${CORRECT_DATA_FILE}               ${CURDIR}/fixtures/correct_data.json

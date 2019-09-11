# eedomus_gethistory

Currently the code is split and some manual steps should be done.

Changing keep_history value in database to True is needed to Watch a new device.

Currently in order to have this running you should:
- Install SQL Server
- Install Python
- Install Grafana
- Create DB in SQL

- Execute CreateDATABASE.sql in SQL Server
- Modify Parameters in Retireve_History and Retrieve_PeripthID python code
	- SQLSERVER = 'XXXXXXXX'
	- DatabaseName = 'XXXXXXXXXXXX'
	- api_user='XXXXXXXXXXXXXX'
	- api_secret='XXXXXXXXXXXX'
- Run Retrieve_PeripthID.py
- Run Retireve_History.py
- Add Datasource to Grafana 
- Add Dashboard with query: SELECT * FROM v_Grafana
- Schedule the Retireve_History.py execution every X hours (6 hours to 24 hours could be the best)
- Schedule every X days or run manually Retrieve_PeripthID.py if you add a new Device.

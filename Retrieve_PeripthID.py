import json
import requests
import pyodbc 


#######################################
# Parameters to be set before running 
#
SQLSERVER = 'XXXXXXXX'
DatabaseName = 'XXXXXXXXXXXX'
api_user='XXXXXXXXXXXXXX'
api_secret='XXXXXXXXXXXX'
########################################

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server='+SQLSERVER+';'
                      'Database='+DatabaseName+';'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()


api_devices_list = 'https://api.eedomus.com/get?api_user='+api_user+'&api_secret='+api_secret+'&action=periph.list'

responselist = requests.get(api_devices_list)
#print(responselist.content)
#data_list_body=json.loads(responselist.content)
#print(data_list_body)
jsonresponse_list = responselist.content.decode('utf-8', 'ignore')
data_list_body=json.loads(jsonresponse_list)
data_list=data_list_body['body']
#print(type(data_list))
for device in data_list:
    #print(device['periph_id'],device['name'])
    cursor.execute("IF NOT EXISTS(SELECT * FROM [dbo].[devices] WHERE periph_id = '"+device['periph_id']+"') INSERT INTO [dbo].[devices] ([periph_id],[name],[keep_history]) VALUES ('"+device['periph_id']+"','"+device['name']+"',0)")
    cursor.commit()

cursor.close()
conn.close()
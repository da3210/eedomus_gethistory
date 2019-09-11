import json
import requests
import pyodbc
import time


#######################################
# Parameters to be set before running 
#
SQLSERVER = 'XXXXXXXX'
DatabaseName = 'XXXXXXXX'
api_user='XXXXXXXX'
api_secret='XXXXXXXX'
########################################

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server='+SQLSERVER+';'
                      'Database='+DatabaseName+';'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

api_device_hist = 	'https://api.eedomus.com/get?api_user='+api_user+'&api_secret='+api_secret+'&action=periph.history&periph_id='

#Obtener lista de periféricos con un 1 a vigilar
q = cursor.execute("SELECT periph_id FROM [dbo].[devices] WHERE keep_history = 1")
#Recorrer Lista
rows = q.fetchall()


if rows is not None:
    for row in rows:
        response = requests.get(api_device_hist+row.periph_id)
        jsonresponse = response.content.decode('utf-8','ignore')
        data=json.loads(jsonresponse)
        datahistory=data['body']
        #print(type(datahistory))
        #print(datahistory)
        data2=datahistory['history']
        #print(type(data2))
        #print(data2)
        
        for action in data2:
            value=action[0] 
            date=action[1]
            #print('Device: '+row.periph_id+' New Status: '+value+' Date: '+date)
            cursor.execute("IF NOT EXISTS(SELECT * FROM [dbo].[History] WHERE periph_id = '"+row.periph_id+"' AND date = '"+date+"') INSERT INTO [dbo].[History] ([periph_id],[date],[value]) VALUES ('"+row.periph_id+"',CONVERT(datetime, '"+date+"', 120),'"+value+"')")
            cursor.commit()
        time.sleep(.600)
else:
    print("No hay datos en la tabla.")


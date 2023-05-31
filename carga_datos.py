from psycopg2 import connect

# Metodo de conexion
def conexion():
    conn = connect(
        database="da0j6o39saf0j7", 
        user='qlvcxmqudpopzq', 
        password='272ae351ac482d76f3db209d14ceea81cd02f73a1a2144e03f727755fa73be19', 
        host='ec2-44-214-132-149.compute-1.amazonaws.com', 
        port= '5432'
    )
    return conn

# Cargamos los archivos adjuntos
def cargaArchivosAdjuntos():
    #Creating a cursor object using the cursor() method
    conn = conexion()
    cursor = conn.cursor()

    #Executing an MYSQL function using the execute() method
    cursor.execute("SELECT parentid, name, convert_from(body, 'utf-8'), sfid, ownerid FROM salesforce.attachment LIMIT 5")

    # Fetch a single row using fetchone() method.
    data = cursor.fetchall()

    #Closing the connection
    conn.close()
    return data

# Cargamos los casos de servicio
def cargaCasosServicios(cuentas):
    #Creating a cursor object using the cursor() method
    conn = conexion()
    cursor = conn.cursor()

    #Executing an MYSQL function using the execute() method
    cursor.execute(f"SELECT id, sfid, accountid, contactid, equipo__c, priority, reason, origin, subject, status, casenumber, type, closeddate, description, contactmobile, contactphone, contactemail, ownerid " +
	        f"FROM salesforce.case WHERE accountid IN ({cuentas})")

    # Fetch a single row using fetchone() method.
    data = cursor.fetchall()

    #Closing the connection
    conn.close()
    return data

# Cargamos los chats de cuentas
def cargaChatCuentas(cuentas):
    #Creating a cursor object using the cursor() method
    conn = conexion()
    cursor = conn.cursor()

    #Executing an MYSQL function using the execute() method
    cursor.execute(f"SELECT id, sfid, parentid, body, type, insertedbyid, createdbyid " +
	    f"FROM salesforce.accountfeed WHERE parentid IN ({cuentas});")

    # Fetch a single row using fetchone() method.
    data = cursor.fetchall()

    #Closing the connection
    conn.close()
    return data

# Cargamos los chats de contactos
def cargaChatContactos(contactos):
    #Creating a cursor object using the cursor() method
    conn = conexion()
    cursor = conn.cursor()

    #Executing an MYSQL function using the execute() method
    cursor.execute(f"SELECT id, sfid, parentid, body, type, insertedbyid, createdbyid " +
	        f"FROM salesforce.contactfeed WHERE parentid IN ({contactos});")

    # Fetch a single row using fetchone() method.
    data = cursor.fetchall()

    #Closing the connection
    conn.close()
    return data

# Cargamos los chats de casos de servicio
def cargaChatCasosServicio():
    #Creating a cursor object using the cursor() method
    conn = conexion()
    cursor = conn.cursor()

    #Executing an MYSQL function using the execute() method
    cursor.execute(f"SELECT id, sfid, parentid, body, type, insertedbyid, createdbyid " +
	        "FROM salesforce.casefeed LIMIT 100;")

    # Fetch a single row using fetchone() method.
    data = cursor.fetchall()

    #Closing the connection
    conn.close()
    return data


if (__name__ == '__main__'):
    # Probamos los archivos adjuntos
    cuentas = "'0013100001rLG1MAAW','0013100001rLOZzAAO','0010Z00002CWqzKQAT','0013100001rLOeuAAG','0010Z00002AAWM8QAP','0010Z00002AB4INQA1','0013100001rLONPAA4','0013100001rLN8xAAG','0013100001gLK3WAAW','0013100001klAZNAA2','0013100001rLMe7AAG','0013100001l0GFQAA2','0013100001rLn3WAAS','0013100001jm69lAAA','0010Z00002CYV4KQAX','0010Z00002E1dXgQAJ','0013100001litDVAAY','0010Z000029wd7cQAA','0013100001rLhqlAAC','0013r00002YvnVyAAJ','0013r00002ZqCx3AAF','0010Z000028mt3IQAQ','0013100001rLiZ5AAK','0013100001rM5SoAAK','0013100001rLkc7AAC','0010Z0000273hUEQAY','0013100001rM79sAAC','0010Z00002CXFLwQAP','0013r00002Dca9WAAR','0013100001qEKAkAAO','0013100001cidIvAAI','0013100001ciKGTAA2','0013r00002YxybvAAB','0010Z0000232q7wQAA','0010Z000024FhsiQAC','0010Z00002Dqlh3QAB','0013r00002YQ1W2AAL','0013r00002ZRy0XAAT','0013100001r4XBHAA2','0013100001oJSuRAAW','001i000001PEEbvAAH','0013100001r5JzyAAE','0010Z0000232r6vQAA','0010Z0000232r9fQAA','0013100001r5AbsAAE','0013100001nyNBAAA2','0010Z00001xU69qQAC','0010Z0000233kDbQAI','0010Z000024FCDKQA4','0013r00002De5DgAAJ','0013100001r5A0hAAE','0013100001r5A45AAE','0010Z00002CWbrjQAD','0010Z0000273JMJQA2','0010Z00002743JjQAI'"
    contactos = "'0030Z00003N8ey0QAB','0030Z00003NiBAhQAN','0030Z00003NiClzQAF','0030Z00003NiCphQAF','0030Z00003NjXPBQA3','0030Z00003PuAnHQAV','0030Z00003QbVbxQAF','0030Z00003XlyonQAB','0030Z00003Zy4HZQAZ','0030Z00003a0bT1QAI','0030Z00003Vvv9zQAB','0030Z00003WIhYwQAL','0030Z00003XXxWlQAL','0030Z00003XhPfHQAV','0030Z00003ZbJVUQA3','0030Z00003ZgY5IQAV','0030Z00003ZpBuIQAV','0030Z00003bQmyAQAS','0030Z00003bd9r4QAA','0033r00003a8gpIAAQ','0030Z00003c9LzSQAU','0033100002pYoFqAAK','0033100002pZEfZAAW','0033100002wwIUcAAM','0033100003CKbQvAAL','00331000030TkZIAA0','003310000329UAIAA2','00331000038VfpfAAC','00331000032bA4aAAE','00331000033OSwPAAW','003310000364WrBAAU','00331000036T9jnAAC','00331000039Ly2cAAC','00331000039qq0QAAQ','00331000039rce7AAA','00331000039rcmMAAQ','00331000039rcxjAAA','00331000039rk1dAAA','0033100003AUDUGAA5','0033100003AUOQiAAP','0033100003AUPBMAA5','0033100003AUS84AAH','0033100003AUSW6AAP','0030Z00003SOdFdQAL','0033100003AUSePAAX','0033100003AUgshAAD','0033100003AUhtmAAD','0033100003AhMolAAF','0033r00003fy5lFAAQ','0033r00003yXh3jAAC','0033r000040ud84AAA','0033r00003wzsXLAAY','0033100003AhTuDAAV','0033r00003vk0MNAAY','0033r00003vnOCmAAM','0033r00003wjLLlAAM','0033r00003wjMVeAAM','0033100003AhjqXAAR','0033100003AhnMZAAZ','0033r00003a8QhLAAU','0033r00003cwNjTAAU','0033r00003m4rCAAAY','0033r00003mdwRuAAI','0033r00003nHnQ7AAK','0033r00003nKwmcAAC','003i000002BHtD5AAL'"
    data = cargaArchivosAdjuntos()
    # print(data)
    # Probamos los casos de servicio
    data = cargaCasosServicios(cuentas)
    # print(data)
    # Probamos los chats de cuentas
    data = cargaChatCuentas(cuentas)
    #print(data)
    # Probamos los chats de cuentas
    data = cargaChatContactos(contactos)
    # print(data)
    # Probamos los chats de cuentas
    data = cargaChatCasosServicio()
    print(data)
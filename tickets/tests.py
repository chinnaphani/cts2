from django.test import TestCase


import win32com.client
from datetime import datetime


strComputer = ["test","DESKTOP-BA9JKGE","testkind"]
services = ['BthAvctpSvc','BFE','bits']
objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")

for srv in strComputer:
    try:
        squery = 0
        objSWbemServices = objWMIService.ConnectServer(srv, "root\cimv2")
        ucolitem = objSWbemServices.ExecQuery("Select * from Win32_OperatingSystem")
        dcolitem = objSWbemServices.ExecQuery("Select * from Win32_LogicalDisk WHERE DriveType=3")
        for uitem in ucolitem:
            stime = uitem.LastBootUpTime
            tests = stime.split('.')
            datetimeformat = '%Y%m%d%H%M%S'
            sftime = datetime.strptime(tests[0], datetimeformat)
            timenow = datetime.now()
            diff = timenow-sftime
            diffs = diff.days
            print(srv + ' is up for days ' + str(diffs))

        for ditem in dcolitem:
            size = ditem.Freespace
            formatsize = int(size)/1024/1024/1024
            print(srv + ditem.Name, int(round(formatsize)))

        while squery<len(services):
            test = services[squery]
            testquery = "Select * from Win32_Service Where Name = '{}'".format(test)
            colItems = objSWbemServices.ExecQuery(testquery)
            for objitem in colItems:
                try:
                    print(srv +' '+ objitem.DisplayName, objitem.State, objitem.Name)
                except:
                    print("service not found")
            squery = squery + 1
    except:
        print (srv + " not reachable")

# Create your tests here.

# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 11:18:24 2014

@author: amne51ac

All content licensed under GPL unless otherwise noted or required.
"""


{"MID" : '', #AUTOINT MESSAGE IDENTIFIER
 "SID" : '', #INT SYSTEM IDENTIFIER
 "PRIV_KEY" : '', #PRIVATE KEY FOR AUTH
 "TIMESTAMP" : '', #FLOAT ABSOLUTE TIME TRANSMITTED
 "TO_CLIENT" : {
     "TASK_COUNT" : '', #INT NUMBER OF TASKS SENT,
     "TASKS" : [
         {"TID" : '', #AUTOINT TASK IDENTIFIER,
          "COMMANDS" : '', #STR COMMAND SET,
          "PRIORITY" :  ''#FLOAT [0(HIGHEST)-10(LOWEST)]
          }, '...']
      },
 "TO_SERVER" : {
     "STATUS" : {
         "" : ''
         },
     "RETURN_COUNT" : '', #INT NUMBER OF RETURNS SENT,
     "TASKS" : [
         {"TID" : '', #AUTOINT TASK IDENTIFIER,
          "RUNNING_TIME" : '', #FLOAT ABSOLUTE TIME TO CURRENT,
          "TSTATUS" : '', #INT (0:STOPPED, 1:RUNNING, 2:PAUSED, 3:ERROR),
          "TSTATUS_MSG" : '', #STR ERRORMSG OR WHATEVER,
          "RETURN_DATA" : '', #VAR RESULTS FROM TASK,
          "RETURN_TYPE" : '' #STR DESCRIBES DATATYPE FOR RETURN_DATA
         }, '...'],
     "PULL_REQUEST" : '' #INT NUMBER OF TASKS TO PULL OR 0 FOR AUTO,
     },
 "CLIENT_REQUEST" : {
     "REQUEST_ID" : '', #INT ID FROM FRONTEND,
     "PREVIOUS_CID" : '', #INT ID FROM PREVIOUS USE,
     "API_ID" : '', #INT APP ID,
     "USERNAME" : '', #STR USERNAME,
     "PASSWORD" : '', #STR PASSWORD,
     "OS" : '', #INT (0:OTHER, 1:WIN7PRO, ETC...),
     "OS_OTHER" : '', #STR OS DESCRIPTION,
     "OS_VERSION" : '', #STR OS VERSION NUMBER,
     "OS_WIDTH" : '', #INT OS WIDTH (64/32/16 BIT),
     "PROC_ARCH" : '', #STR PROCESSOR ARCHITECTURE,
     "CPU_CORES" : '', #INT NUMBER OF CORES,
     "CPU_CLOCK" : '', #FLOAT CLOCK SPEED,
     "CPU_BRAND" : '', #STR CPU MANUFACTURER,
     "CPU_MODELNO" : '', #INT CPU MODEL NO,
     "CPU_MODELNAME" : '', #STR CPU MODEL NAME,
     "CPU_STR" : '', #STR CPU DESCRIPTION,
     "MEM_SIZE" : '', #INT MEMORY SIZE (MB),
     "MEM_TYPE" : '', #STR MEMORY DESCRIPTION,
     "FLOPS" : '', #INT FLOPS BENCHMARK RETURN
     },
 "CLIENT_ASSIGNMENT" : {
     "CLIENT_ID" : '', #INT CLIENT UNIQUE IDENTIFIER,
     "PRIV_KEY" :  ''#PRIVATE KEY FOR AUTHENTICATION
     }
 }
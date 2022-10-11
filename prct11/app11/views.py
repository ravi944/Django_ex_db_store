from django.shortcuts import render,HttpResponse
import mysql.connector as mysql
import xlrd
import os
import pyexcel as p
import pathlib

def index(request):
    ##### FIRST METHOD
    
    db = mysql.connect(host="localhost",user="root",password="1234",database="db_of_sample")
    cur = db.cursor()
    
    ## WE have to comment this when appending data to already exsting table
    ## if we are creating table keep let it be(18,19,20 lines)
 
    # cur.execute("DROP TABLE IF EXISTS EMPLOYEE")
    # sql1 = "CREATE TABLE EXCEL_DATA20 ( id int not null, first char(20) not null, last char(20), loc char(20) )"
    
    #### To create table for MOCK_DATA excel  sheet in DB
#     sql1 = "CREATE TABLE EXCEL_DATA20 ( id int not null, first_name char(20) not null, last_name char(20), email char(100),gender char(20),ip_address char(100) )"

    # cur.execute(sql1)
    
    
    
    
    if request.method == 'POST':
        loc = request.FILES['myfile']
        if loc.name.endswith('.xlsx'):
            p.save_book_as(file_name=str(loc),dest_file_name = 'your-new-file-out.xls')
            a = xlrd.open_workbook("your-new-file-out.xls")
        else:
            a = xlrd.open_workbook(str(loc))
        

        
        sheet = a.sheet_by_index(0)
        sheet.cell_value(0,0)
    
        l=list()
        for i in range(1,sheet.nrows):
            l.append(tuple(sheet.row_values(i)))
        
        q="insert into excel_data19(id,first,last,loc)values(%s,%s,%s,%s)"
        
        #### To take values from excel sheet and merge with columns in table in DB
#         q="insert into excel_data19(id,first_name,last_name,email,gender,ip_address)values(%s,%s,%s,%s,%s,%s)"


        cur.executemany(q,l)
        db.commit()
        db.close()
        
        
     ###SECOND METHOD
    
#     import pandas as pd
#     from sqlalchemy import create_engine
    
#     engin = create_engine('mysql://root:1234@localhost/ravi')
#     if request.method == 'POST':
#         loc = request.FILES['myfile']
     
#         df = pd.read_excel(str(loc))
#         df.to_sql('people12',con=engin,if_exists='append')


    
    
    return render(request, 'input.html')




import mysql.connector
ppl_list=[]
cnx= mysql.connector.connect(user='root',password='',
                             host='127.0.0.1',
                             database='practice')

cursor=cnx.cursor()
query='SELECT * FROM people'
cursor.execute(query)
for (Name,Weight,Height) in cursor:
    ppl_list.append([Name,Weight,Height])
cnx.close()
ppl_list=sorted(ppl_list,key=lambda weight: weight[1])
ppl_list=sorted(ppl_list,key=lambda height: height[2],reverse=True)
for i in range(len(ppl_list)):
    print (ppl_list[i][0],ppl_list[i][2],ppl_list[i][1])

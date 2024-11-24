#建立新表
import sqlite3

def insert(cur,tablename,date):
    cur.execute('INSERT INTO {}VALUES({})'.format(tablename,data))


conn = sqlite3.connect('carPark.db') #连接数据库（数据库不存在，则建立新数据库)
cur = conn.cursor() #打开游标

#需要建立新表1
sql = "CREATE TABLE IF NOT EXISTS parkTotalInfo(total INTEGER,parks INTEGER,emptys INTEGER,rows INTEGER,cols INTEGER )"
#初始化表1数据
data = '32,0,32,8,4'
cur.execute('INSERT INTO parkTotalInfo VALUES({})'.format(data))

#需要建立新表2
sql = "CREATE TABLE IF NOT EXISTS parkDetailInfo(row INTEGER,col INTEGER,parked  INTEGER)"
for i in range(1,9):
    for j in range(1,5):
        cur.execute('INSERT INTO parkDetailInfo VALUES({},{},0)'.format(i,j))

detailData =[(2,3,1),(7,1,1),(1,4,1),(7,1,0),(2,1,1),(6,2,1),(6,2,0)]
for d in detailData:
    cur.execute('update parkDetailInfo set parked={} where row ={} and col={}'.format(d[2],d[0],d[1]))
conn.commit()

cur.execute('select * from parkTotalInfo')
parkdate = cur.fetchall()
print('fetch:',parkdate)
conn.commit()
total,parks,emptys,rows,cols= parkdate[0]
for r,c,s in detailData:
    if s ==1:
        parks+=1
        emptys-=1
    elif s==0:
        parks-=1
        emptys+=1
print('parks={},emptys={}'.format(parks,emptys))
cur.execute('update parkTotalInfo set parks={},emptys={}'.format(parks,emptys))
conn.commit()



cur.close()#结束则需要关闭游标和数据库的连接
conn.close()
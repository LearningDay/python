* cmd中安装pymysql包

  * pip install pymysql

  * pip3 install pymysql（同时安装python2和3）

```python
import pymysql

conn = pymysql.connect(
	host = '127.0.0.1',
    user = 'root',
    password = 'admin888',
    db = 'learn',
    port = 3306,
    charset = 'gbk'
)

cur = conn.cursor()
cur.execute("select * from dataanalyst where workYear = '1-3年'")

data = cur.fetchall()

for d in data:
    print(d[0],d[-1])
    
cur.close()
conn.close()
```

# 自定义函数reader()灵活读取MySQL数据库
```python
def reader(query,db='learn',char='gbk'):  # 灵活自定义query:sql查询语句','db:数据库名称'，'char：文件编码，如utf8，gbk等'
    sql = query #灵活使用字符串
    engine = create_engine('mysql+pymysql://root:admin888@127.0.0.1:3306/{0}?charset={1}'.format(db,char))# 自动传入，0对应‘db’，1对应‘char’
    df = pd.read_sql(sql,engine)
    return df
```
```python
* reader('show tables')
  * 显示数据库中表的名称
```
# pandas读取mysql数据库
```python
import pymysql
import pandas as pd
from sqlalchemy import create_engine

sql = "select * from dataanalyst where workYear = '应届毕业生'"
engine = create_engine('mysql+pymysql://root:admin888@127.0.0.1:3306/learn?charset=gbk')
pd.read_sql(sql,engine)
```

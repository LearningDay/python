```python
import numpy as np
import pandas as pd
from sqlalchemy import create_engine

def reader(query,db,encoding='utf8'):
	sql = query
	engine = create_engine(
	'mysql+pumysql://root:123456@127.0.0.1:3306/{0}?charset={1}',format(db,encoding)
	)
	df = pd.read_sql(sql,engine)
	return df
	
df_1 = reader('select * from','learn')
```
1. 填入SQL查询语句和数据库名称
2. 即可读取，加载数据库文件
3. 实现半自动化处理 之前同类型数据

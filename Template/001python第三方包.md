```python
import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
import seaborn as sns

# jupyter notebook 的内置命令，让制作好的图片显示在单元格
%matplotlib inline

# 更改设计风格
plt.style.use('ggplot')


plt.rcParams['font.sans-serif']=['SimHei']  
1. 解决中文显示问题
2. 设置默认字体


plt.rcParams['axes.unicode_minus']=False
1. 坐标轴允许显示负值
2. 解决保存图像时负号'-'显示为方块的问题
```

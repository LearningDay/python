[TOC]



1. 数据获取
2. 数据清洗
   * 预处理
   * 缺失值
   * 格式
   * 逻辑错误
   * 选取行列
   * 关联性验证
3. 数据整理
   * 数据规范化
     * 离散化
     * 表转化
   * 指标计算
     * 统计计算，生成各种指标
   * 格式转换
     - 将数据转换为制图制表所需格式
4. 分析框架
   1. 描述分析
      - 利用处理好的数据，制图，进行描述分析
      - 根据描述分析结论，形成洞察结果（洞察结论）
        - 变化
        - 分布
        - 对比
        - 预测
   2. 数据建模
      - 初学者考虑使用线性回归和聚类模型
      - 模型测试
      - 迭代优化
        - 模型加载
5. 可视化
6. 业务理解

***

# 案例背景

1. 希望对2018-19年NBA各支球队得分能力进行总体了解
2. 希望能发觉领先的球队
3. 目标确定：通过第三方平台公开数据，对NBA球队2018-19年进行基本的刻画，进行排名和分类

# 逻辑框架

1. 主要观点
   1. 球队得分能力
      * 球队规模
      * 
   2. 球队排名
      * 得分排名
      * 胜负排名
      * TOP发掘
   3. 球员分类
      * 聚类模型
2. 总结
   * 下一步
     * 球员交易

***

# PPT

## 目录

1. 研究背景
   * 勒布朗詹姆斯，转会湖人，分析2018-19赛季，湖人队表现
2. 研究目标
   * 各球队赛季同比
   * 各球队球员得分能力分布
3. 分析思路
4. 分析结论
5. 指标解释

* Team Per Game Stats：每支队伍平均每场比赛的表现统计
* Miscellaneous Stats：综合统计数据

| 数据名                             | 含义                       |
| ---------------------------------- | -------------------------- |
| Rk -- Rank                         | 排名                       |
| G -- Games                         | 参与的比赛场数（都为82场） |
| MP -- Minutes Played               | 平均每场比赛进行的时间     |
| FG--Field Goals                    | 投球命中次数               |
| FGA--Field Goal Attempts           | 投射次数                   |
| FG%--Field Goal Percentage         | 投球命中次数               |
| 3P--3-Point Field Goals            | 三分球命中次数             |
| 3PA--3-Point Field Goal Attempts   | 三分球投射次数             |
| 3P%--3-Point Field Goal Percentage | 三分球命中率               |
| 2P--2-Point Field Goals            | 二分球命中次数             |
| 2PA--2-point Field Goal Attempts   | 二分球投射次数             |
| 2P%--2-Point Field Goal Percentage | 二分球命中率               |
| FT--Free Throws                    | 罚球命中次数               |
| FTA--Free Throw Attempts           | 罚球投射次数               |
| FT%--Free Throw Percentage         | 罚球命中率                 |
| ORB--Offensive Rebounds            | 进攻篮板球                 |
| DRB--Defensive Rebounds            | 防守篮板球                 |
| TRB--Total Rebounds                | 篮板球总数                 |
| AST--Assists                       | 辅助                       |
| STL--Steals                        | 偷球                       |
| BLK -- Blocks                      | 盖帽                       |
| TOV -- Turnovers                   | 失误                       |
| PF -- Personal Fouls               | 个犯                       |
| PTS -- Points                      | 得分                       |

1. 描述性统计
2. 建模构建
3. 








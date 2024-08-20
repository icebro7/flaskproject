

import sqlite3
from config import employ


class DatabaseEmployHandler(object):
    def __init__(self):
        self.database_path = employ.DATABASE_PATH
        self.conn = sqlite3.connect(self.database_path)
        self.cursor = self.conn.cursor()
        self.conn.commit()
        self.conn = sqlite3.connect(self.database_path)
        self.cursor = self.conn.cursor()

    def query(self, query: str):
        self.cursor.execute(
            query
        )
        return self.cursor.fetchall()

    # 计算不同workCity的salaryMax的平均值,数据用于图表1

    def getSalaryMax(self):
        query = "select workCity,avg(salaryMax) as sm from employ where workCity != '江西' and workCity != '奉贤区' and workCity != '银川' and workCity != '全国' group by workCity order by sm"
        # 将数据以[{"name": "xxx", "value": 1234}]的形式存储
        data = []

        for row in self.query(query):
            data.append(
                {
                    "name": row[0],
                    "value": row[1]
                }
            )
        return data

    # 计算不同workCity的salaryMax的平均值,数据用于图表2

    def getSalarymean(self):
        query = "select empcode,avg(salaryMax) as sm from employ group by empcode order by sm"
        result = self.query(query)
        with open('salarymean.json', 'w') as f:
            f.write(str(result))
        return result

    # 计算不同学历的salaryMax的平均值,数据用于图表5

    def getSalaryMeanByEducation(self):
        # 查询各线城市
        query_1 = "select education,avg(salaryMax) as sm from employ WHERE education != '其他' AND education != 'MBA/EMBA' AND education != 'EMBA' AND education != '中技'  AND education != '学历不限' AND workCity = '北京' OR workCity = '上海' OR workCity = '广州' OR workCity = '台湾' OR workCity = '香港' OR workCity = '澳门' group by education order by sm"
        query_2 = "select education,avg(salaryMax) as sm from employ WHERE education != '其他' AND education != 'MBA/EMBA' AND education != 'EMBA' AND education != '中技'  AND education != '学历不限' AND workCity = '成都' OR workCity = '重庆' OR workCity = '杭州' OR workCity = '武汉' OR workCity = '西安' OR workCity = '郑州' OR workCity = '长沙' OR workCity = '天津' OR workCity = '南京' OR workCity = '沈阳' OR workCity = '合肥' group by education order by sm"
        query_3 = "select education,avg(salaryMax) as sm from employ WHERE education != '其他' AND education != 'MBA/EMBA' AND education != 'EMBA' AND education != '中技'  AND education != '学历不限' AND workCity = '昆明' OR workCity = '福州' OR workCity = '哈尔滨' OR workCity = '长春' OR workCity = '南宁' OR workCity = '石家庄' OR workCity = '济南' OR workCity = '太原' OR workCity = '贵阳' OR workCity = '南昌' group by education order by sm"
        query_4 = "select education,avg(salaryMax) as sm from employ WHERE education != '其他' AND education != 'MBA/EMBA' AND education != 'EMBA' AND education != '中技'  AND education != '学历不限' AND workCity = '呼和浩特' OR workCity = '乌鲁木齐' OR workCity = '兰州' OR workCity = '银川' OR workCity = '南宁' OR workCity = '海口'  group by education order by sm"
        query_5 = "select education,avg(salaryMax) as sm from employ WHERE education != '其他' AND education != 'MBA/EMBA' AND education != 'EMBA' AND education != '中技'  AND education != '学历不限' AND workCity = '西宁' OR workCity = '拉萨'  group by education order by sm"
        with open('salarymeanbyeducation.json', 'w') as f:
            f.write(str(self.query(query_1)))
            f.write(str(self.query(query_2)))
            f.write(str(self.query(query_3)))
            f.write(str(self.query(query_4)))
            f.write(str(self.query(query_5)))
        return self.query(query_1), self.query(query_2), self.query(query_3), self.query(query_4), self.query(query_5)

    # 计算所有岗位中的出现次数top30,数据用于图表8

    def getnameByTop(self):
        # 查询字段：name中出现次数最多的前30个
        query = "select name,count(name) as num from employ group by name order by num desc limit 30"
        result = self.query(query)
        with open('empNameByTop.json', 'w') as f:
            f.write(str(result))
        return result

    def save(self):
        self.conn.commit()
        self.conn.close()


if __name__ == '__main__':
    pass

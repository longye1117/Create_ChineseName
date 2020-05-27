# 作者：刘馨
# 日期：2020/5/27

import random
import numpy as np


name_list=[]
for i in range(0,1000):
    first_name_list = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯',
                      '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦',
                      '尤', '许', '姚', '邵', '堪', '汪', '祁', '毛', '禹',
                      '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴',
                      '谈', '宋', '茅', '庞', '熊', '纪', '舒', '屈', '项',
                      '祝', '董', '梁',"东方","欧阳","司马"]
    name_length=np.random.randint(1,3)
    name=random.choice(first_name_list)
    for i in range(0,name_length):
            head = random.randint(0xb0, 0xf7)
            body = random.randint(0xa1, 0xfe)
            val = f'{head:x}{body:x}'
            name = name+str(bytes.fromhex(val).decode('gb2312',errors="ignore"))
            # name.append(str)
    name_list.append(name)

print(name_list)
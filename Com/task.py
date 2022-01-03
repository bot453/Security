# coding=utf-8
"""
计划任务测试文件
"""
import datetime

# 显示当前具体时间
today = datetime.datetime.now()
# 输入时间str转化
Now_Today = str(today)
# print("today is:"+str(today))

# a文件追加写入,并创建文件
f = open("Testing.txt","a")
# 文件写入
f.write("This is Test File write!"+Now_Today+"\n\r")
# 关闭文件
f.close()
print("测试完成")


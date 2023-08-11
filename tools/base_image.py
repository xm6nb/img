import base64
import matplotlib.pyplot as plt
import numpy

# 对base64文件进行解码
with open('subject','r') as j:
    str = base64.b64decode(j.read().encode())
    # 解码后的文件保存一下
    with open('file','w') as f:
        f.write(str.decode())
# 对坐标数据进行处理       
with open('file','r') as f:
    list = f.read().split('),')
with open('out','w') as x:
    for i in list:
        str = i.replace('(','').replace(')','').replace('[','').replace(']','')
        x.write(str + '\n')
# 开始绘图
x,y=numpy.loadtxt('out',delimiter=',',unpack=True)
plt.plot(x,y,'.')
plt.show()


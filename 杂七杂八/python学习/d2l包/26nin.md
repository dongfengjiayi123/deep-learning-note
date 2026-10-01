NiN网络中的网络
全连接层占空间,且容易过拟合
输入的像素乘以高和宽
![alt text](杂七杂八/python学习/d2l包/image-36.png)

vgg的占用空间很占用且全连接层会占用带宽,容易过拟合
nin不用全连接层
nin块
![alt text](杂七杂八/python学习/d2l包/image-37.png)
nin架构
![alt text](杂七杂八/python学习/d2l包/image-38.png)
![alt text](杂七杂八/python学习/d2l包/image-39.png)
 

参数少为了解决全连接的维度问题




```
import torch
from torch import nn
from d2l import torch as d2l

#nin架构
def nin_block(in_channels, out_channels, kernel_size, strides, padding):
    return nn.Sequential(
        nn.Conv2d(in_channels, out_channels, kernel_size, strides, padding),
        nn.ReLU(),
        nn.Conv2d(out_channels, out_channels, kernel_size=1), nn.ReLU(),
        nn.Conv2d(out_channels, out_channels, kernel_size=1), nn.ReLU())

#nin模型很像alexnet
net = nn.Sequential(
    nin_block(1, 96, kernel_size=11, strides=4, padding=0),
    nn.MaxPool2d(3, stride=2),
    nin_block(96, 256, kernel_size=5, strides=1, padding=2),
    nn.MaxPool2d(3, stride=2),
    nin_block(256, 384, kernel_size=3, strides=1, padding=1),
    nn.MaxPool2d(3, stride=2),
    nn.Dropout(0.5),
    # 标签类别数是10
    nin_block(384, 10, kernel_size=3, strides=1, padding=1),
    nn.AdaptiveAvgPool2d((1, 1)),#全局平均池化
    # 将四维的输出转成二维的输出，其形状为(批量大小,10)
    nn.Flatten())

```

```



```















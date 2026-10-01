vgg![alt text](杂七杂八/python学习/d2l包/image-33.png)
使用块的想法首先出现在牛津大学的[视觉几何组（visual geometry group）](http://www.robots.ox.ac.uk/~vgg/)的*VGG网络*中。通过使用循环和子程序，可以很容易地在任何现代深度学习框架的代码中实现这些重复的架构。

更深更大,数据更多
![alt text](杂七杂八/python学习/d2l包/image-32.png)

块中的概念,3*3的重复使用比5*5更快更好
![alt text](杂七杂八/python学习/d2l包/image-34.png)

VGG-16,VGG-19
![从AlexNet到VGG，它们本质上都是块设计。](../img/vgg.svg)
重复的VGG块

其中关系的图
![alt text](杂七杂八/python学习/d2l包/image-35.png)


```vgg块
import torch
from torch import nn
from d2l import torch as d2l


def vgg_block(num_convs, in_channels, out_channels):
    layers = []
    for _ in range(num_convs):
        layers.append(nn.Conv2d(in_channels, out_channels,
                                kernel_size=3, padding=1))
        layers.append(nn.ReLU())
        in_channels = out_channels
    layers.append(nn.MaxPool2d(kernel_size=2,stride=2))
    return nn.Sequential(*layers)
```
```为什么是五块是因为224/2^5=7
conv_arch = ((1, 64), (1, 128), (2, 256), (2, 512), (2, 512))
```

```实现vgg网络结构
def vgg(conv_arch):
    conv_blks = []
    in_channels = 1
    # 卷积层部分
    for (num_convs, out_channels) in conv_arch:
        conv_blks.append(vgg_block(num_convs, in_channels, out_channels))
        in_channels = out_channels

    return nn.Sequential(
        *conv_blks, nn.Flatten(),
        # 全连接层部分
        nn.Linear(out_channels * 7 * 7, 4096), nn.ReLU(), nn.Dropout(0.5),
        nn.Linear(4096, 4096), nn.ReLU(), nn.Dropout(0.5),
        nn.Linear(4096, 10))

net = vgg(conv_arch)
```

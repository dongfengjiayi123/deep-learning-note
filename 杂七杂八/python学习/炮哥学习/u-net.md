![alt text](杂七杂八/python学习/炮哥学习/image.png)
u-net主要是通过保留原来的一部分信息,然后通过切割合并的方式使得信息分为两部分,即原来的信息和通过卷积池化和专职卷积等方法提取的图像信息融合,不断通过上采样进行放大,最终得到结果

![alt text](杂七杂八/python学习/炮哥学习/image-1.png)

先将原始图像扩大再进行识别

每一小块都是unet的多个进行识别

语义分割的unet
代码中的网络模型结构

![alt text](杂七杂八/python学习/炮哥学习/image-2.png)

512*512*3
512*512*num
RestNet50骨干
编码器部分是个Restnet50
deencoder 部分是线性插值进行上采样
concat融合
上采样的大小与融合一样

代码中不用切割
输入多少
输出多少
![alt text](杂七杂八/python学习/炮哥学习/image-3.png)

环境创建与安装
在数据处理细节不同

代码的分析和环境测试
![alt text](杂七杂八/python学习/炮哥学习/image-4.png)
bottleneck
存在卷积操作相加和把x拿过来进行融合
![alt text](杂七杂八/python学习/炮哥学习/image-5.png)










2020.10.15

1.在网上学习Python编程，今天了解了Python的包和模块的调用，了解了Python的各种数据类型，字典，列表，元组，集合的定义格式和使用方法。


2020.10.17

树莓派开箱配置：

1.树莓派与笔记本的远程连接

我使用网线通过ssh和笔记本电脑相连。

（1）ssh连接配置

先在sd卡内烧录系统镜像，在boot目录下新建一个ssh文件，不要有文件后缀。

（2）获取树莓派ip

我通过网线和笔记本相连，在笔记本上进入控制面板\网络和 Internet\网络连接中找到wlan右键点击属性，点击共享，把选项框都打勾。运行cmd输入arp -a查找树莓派ip即可。

（3）使用putty通过ssh连接

将树莓派ip输入putty即可连接树莓派。连接过程的选项框点击是即可，然后输入用户名和密码，用户名：pi，密码raspberry即可登录树莓派。

2.第一次登录树莓派的配置

（1）给Raspbian的包管理器apt-get换源

（2）给Python的第三方模块安装工具pip换源
详细配置参考链接：

https://github.com/TommyZihao/ZihaoTutorialOfRaspberryPi/blob/master/%E7%AC%AC3%E8%AE%B2%EF%BC%9A%E4%B8%80%E5%8A%B3%E6%B0%B8%E9%80%B8%E9%85%8D%E7%BD%AE%E6%A0%91%E8%8E%93%E6%B4%BE.md





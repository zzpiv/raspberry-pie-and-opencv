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

2020.10.18

树莓派4搭建opencv3.4.0环境

1.安装opencv依赖库

sudo apt-get install build-essential git cmake pkg-config -y

sudo apt-get install libjpeg8-dev -y

sudo apt-get install libtiff5-dev -y

sudo apt-get install libjasper-dev -y

sudo apt-get install libpng12-dev -y

sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev -y

sudo apt-get install libgtk2.0-dev -y

sudo apt-get install libatlas-base-dev gfortran -y

2.在网上寻找opencv版本的源码文件，因为很多人说用命令行下载速度很慢而且不稳定，最好的方法是在百度网盘下载后通过vnc传送给树莓派的Download目录下。

（1）解压opencv下载文件，执行以下命令

cd /home/pi/Downloads

unzip opencv-3.4.0.zip

unzip opencv_contrib-3.4.0.zip

（2）新建一个用于编译的文件build 执行以下命令

cd /home/pi/Downloads/opencv-3.4.0

mkdir build

cd build

（3）设置cmake参数  执行以下代码（文件路径需根据实际情况修改）

cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON -D OPENCV_EXTRA_MODULES_PATH=/home/pi/Downloads/opencv_contrib-3.4.0/modules -D BUILD_EXAMPLES=ON -D WITH_LIBV4L=ON PYTHON3_EXECUTABLE=/usr/bin/python3.7 PYTHON_INCLUDE_DIR=/usr/include/python3.7 PYTHON3_NUMPY_INCLUDE_DIRS=/home/pi/usr/lib/python3/dist-packages/numpy/core/include ..

（4）配置成功后 执行以下命令

sudo make

等待两个小时的编译，，，，

（5）出现100%表示编译成功 install 执行命令

sudo make install 大约1分钟

（6）测试 执行以下命令

python3

import cv2

cv2.__version__

出现opencv版本号说明安装成功。

注意：编译前的避坑操作 参考链接：https://blog.csdn.net/qq_43762614/article/details/102760414

（1）可以在一个大佬的百度云盘里下载然后将所有带i结尾的文件全部都拷贝到 opencv_contrib/modules/xfeatures2d/src/ 路径下即可树莓派安装opencv时丢失的文件

链接：https://pan.baidu.com/s/1xi6_5NuTFiP4SD649FgIJw
提取码：mbsj

（2）错误的原因是缺少cuda.hpp文件，这些文件在opencv_contrib-3.4.1/modules/xfeatures2d/include/opencv2目录下，所以直接将这个目录下的文件拷贝到opencv-3.4.1/modules/stitching/include/opencv2/即可

（3）执行命令 vim ~/opencv/opencv-3.2.0/modules/videoio/src/cap_ffmpeg_impl.hpp

在文件最顶端添加如下内容即可

#define AV_CODEC_FLAG_GLOBAL_HEADER (1 << 22)
#define CODEC_FLAG_GLOBAL_HEADER AV_CODEC_FLAG_GLOBAL_HEADER
#define AVFMT_RAWPICTURE 0x0020

（4）首先找到/home/pi/Downloads/opencv-3.4.0/modules/python/src2 中的cv2.cpp文件，然后在第885行把char* 改成 const char* 即可

执行完以上4步操作，编译一般就没什么问题了。

因为我编译前把坑都填完了，所以编译了一次就成功了，开心。

附一个简单的oython测试代码










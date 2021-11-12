# MicroserviceDK（Docker + k8s）
2021-07-23 Docker&amp;k8s微服务容器化实践
![01-topo.png](images/01-topo.png)

## 从依赖最少的 信息服务 入手
[thrift官网](https://thrift.apache.org/)
* 下载 thrift-0.14.2.exe 改成thrift.exe 放在path可及的地方(System32)
> thrift -version
```
<dependency>
  <groupId>org.apache.thrift</groupId>
  <artifactId>libthrift</artifactId>
  <version>0.14.2</version>
</dependency>
```

### thrift/demo.thrift  尝试生成对应代码文件 （安装 thrift support 插件）
```
thrift --gen java demo.thrift
thrift --gen py demo.thrift
```
### 新建模块 message-thrift-python-service （安装 python 插件）
>要么新建python项目的时候，framework就添加thrift
>要么选择对应module右键添加framework支持
> 
>注意 SDKs - python3.9 - package - 要安装pip+six+thrift 
> （电脑若开了代理，就报各种pip版本不正确，详细日志报 check_hostname requires server_hostname
> 操他妈）

新建thrift文件夹/message.thrift文件
sh脚本（右键执行）：输出py到根目录下面
```shell
thrift --gen py -out ../ message.thrift
```
### 简单实现一下 api/MessageService.py 
message_service.py   并与thrift 关联起来
### 与


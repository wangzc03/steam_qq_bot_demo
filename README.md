# steam_qq_bot_demo
这是一个使用python库a2s（查询steam服务器游戏人数） 和onebot（qq机器人）写的一个能查询steam游戏服务器人数的简单demo

这两个库都能在github找到
qq新版支持很多接口 很方便

1.安装python环境 ，配置pip镜像 使用pip安装依赖
2.安装qq，安装onebot，运行
3.运行本脚本，在群聊里输入关键字 触发查询并发送

先获取你要搜索的服务器ip，然后使用浏览器steam接口访问（记得修改ip）获取json 得到你要查询的服务器端口
http://api.steampowered.com/ISteamApps/GetServersAtAddress/v0001?addr=123.456.78.90
然后加到查询列表数据结构中


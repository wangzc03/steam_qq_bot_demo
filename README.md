# steam_qq_bot_demo
这是一个使用python库a2s（查询steam服务器游戏人数） 和nonebot（qq机器人）写的一个能查询steam游戏服务器人数的简单demo示例
你在qq群中发一句特定的话（如越南1），就会有一个人输出每一行服务器X 地图Y 和游戏人数Z的列表<br>
https://github.com/Yepoleb/python-a2s <br>
https://github.com/nonebot/nonebot2  <br>
这两个库都能在github找到<br>
qq新版支持很多接口 很方便<br>

你可能需要购买云服务器和一个qq小号来后台运行这个bot<br>
在你购买服务器后，你进入了windows server 20xx版<br>
你需要：<br>
1.安装python环境 ，配置pip镜像 使用pip安装依赖<br>
2.安装qq，安装nonebot2，并运行<br>
3.运行本脚本，在群聊里输入关键字 触发查询并发送<br>

先获取你要搜索的服务器ip，然后使用浏览器steam接口访问（记得修改ip）获取json 得到你要查询的服务器端口<br>
http://api.steampowered.com/ISteamApps/GetServersAtAddress/v0001?addr=123.456.78.90<br>
然后加到查询列表数据结构中<br>


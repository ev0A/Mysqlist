# Mysql Server端伪造-任意文件读取-CTF快速利用脚本

嫌网上脚本太麻烦？想换个文件读还要vim进去手动改？

想读取的文件太多，一次一次输入太麻烦？

用了一次以后端口就被系统占用，必须等释放以后才能继续用？

---
这两个mysql任意文件读取脚本 一定能满足你的需求！

项目提供了两个文件，dicc和input，
一个采用字典的方式进行任意文件读取
一个采用交互式界面进行任意文件读取
不需要进入vim！ 用字典直接读！命令行直接输！
结合burp intruder，直接fuzz出flag！

采用了socket的端口复用技术，防止端口被系统占用，想绑定就绑定，为所欲为！
PS: 端口复用只能防止套接字关闭后被系统保留，如果端口上已经有mysql应用，则还是不能绑定
​    **会爆socket.error: [Errno 10013]错误**

## dicc
用法
dicc.txt是字典文件

```python
python2 exp_dicc.py port
例
python2 exp_dicc.py 3306
```
此时会进入监听，结合具体场景，用burp重复发包即可，读取成功的文件会被计入到log文件夹

## input
用法
```python
python2 exp_input.py port
例
python2 exp_input.py 3306
```
此时会进入监听，可以在命令行输入你想读的文件，然后发包即可，每次发完包需重新输入文件名
直接回车即可退出，读取成功的文件也会被计入到log文件夹


## 安利一下
安利一下我的任意文件读取的fuzz字典项目

[https://github.com/ev0A/ArbitraryFileReadList](https://github.com/ev0A/ArbitraryFileReadList)


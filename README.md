# speech-to-text-microphone
google api speech-to-text  麦克风  Python示例 


最重要的代码
```
import os
os.environ['http_proxy'] = 'http://127.0.0.1:7890'
os.environ['https_proxy'] = 'http://127.0.0.1:7890'

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'shell.json'
```
因国内访问谷歌的服务会被墙，需要本地开VPN服务，并且在代码里设置使用的代理，否则不能使用。

示例文档：
https://cloud.google.com/speech-to-text/docs/samples

示例代码Github:
https://github.com/googleapis/python-speech/tree/main/samples

密钥文件位置：
先进入谷歌云控制台 https://console.cloud.google.com/
进入API和服务管理界面
选择凭据
选择服务账号
进入后选择密钥，即可添加

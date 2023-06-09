# v2free机场自动签到
Fork vpnqd/v2free项目，学习并使用v2free机场自动签到
删除了TGBOT自动通知，增加了飞书机器人通知
## 功能

废话，肯定就是机场自动签到啊。
## 部署
1. Fork此仓库
2. 到`Settings`→`Secrets`→`Actions` 添加以下参数：

| 参数  | 是否必须  | 内容  | 示例  |
| ------------ | ------------ | ------------ | ------------ |
| EMAIL  | 是  | 注册机场所用邮箱  | a@example.com  |
| PASSWORD  | 是  | 注册机场所用密码  | password1  |
| BASE_URL  | 是  | 机场地址  | https://examplea.com  |
| SCKEY  | 是  | Sever酱秘钥  | SCTxxxxxxxxxxxxxx  |
| FS_BOT  | 否  | 飞书机器人webhook地址  | https://open.feishu.cn/open-apis/bot/v2/hook/xxxx  |

> https://xcao.top/post-278.html 水了个博文，操作更详细

3. 转到`Actions`创建一个workflow，运行一次，以后每天项目都会自动运行。最后，可以到Run sign查看签到情况，同时也会通过Sever酱发送出去。
## Fork
1. https://github.com/vpnqd/v2free

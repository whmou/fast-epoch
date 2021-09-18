# fast-epoch
convert copied epoch time to UTC+0 human readable with mac notification
![image](https://github.com/whmou/fast-epoch/blob/main/demo.jpg)<br><br>

## Prerequisite
---
1. Python3 Mac env
2. Mac Alfred (optional) [Download link](https://www.alfredapp.com/)
3. If you don't use Alfred to trigger the app, then put your epoch time as 1st argumment to the ep.py 

## Install steps
---
1. Change the ep.py path in the epoch.app by mac automator.app
```bash
$ open /System/Applications/Automator.app
## b=`python /Users/wmou/test/ep.py $time` change the ep.py path to wherever the code is located
```
2. Put epoch.app folder under the /Applications folder
3. Call Alfred, type "reload" to renew the index to make Alfred recognize epoch.app
<br><br>

## Usage
---
1. Copy epoch time string to the Mac clipboard. <br>ex: 1631937786 or 1631937786000 (In milliseconds)
2. Call Alfred and type "epoch" to trigger the app.
3. The reslut will show as the mac notification
![image](https://github.com/whmou/fast-epoch/blob/main/fast-epoch-example.png)
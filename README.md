# communication-invoice-screenshot
自动生成通讯发票截图的小程序 
http://www.tax.sh.gov.cn/xbwz/wzcx/WSBSptFpCx_loginsNewl.jsp 

我这个临时写得很随意很烂，求修改

## 使用方法：
```
git clone https://github.com/Adamyuanyuan/communication-invoice-screenshot.git
cd communication-invoice-screenshot
# python image.py 发票代码 发票号码首 发票号码尾 2（发票号码前面0的数量）
python image.py 131001728062 00828881 00828895 2

```
图片会保存到 outs 文件夹下

### 注意
目前我有两个模板：分别是 2017.4.17日（002.png）和2017年09.29日（003.png）的模板，各位看看自己的发票是属于哪个模拟

## 原理很简单
1. PS一个发票模板
2. 指定首尾发票号码
3. 根据图片修改库修改模板中的发票号码
4. 循环生成并保存到文件夹下

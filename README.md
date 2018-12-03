# communication-invoice-screenshot
自动生成通讯发票截图的小程序 http://www.tax.sh.gov.cn/xbwz/wzcx/WSBSptFpCx_loginsNewl.jsp 
我这个临时写得很随意很烂，求修改

## 使用方法：
```
# python image.py 发票代码 发票号码首 发票号码尾 2（发票号码前面0的数量）
python image.py 131001728062 00828881 00828895 2

```
图片会保存到 outs 文件夹下

## 原理很简单
1. PS一个发票模板
2. 根据图片修改库修改模板中的发票号码
3. 循环保存图片到指定文件夹

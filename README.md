# communication-invoice-screenshot
自动生成通讯发票截图的小程序

## 原理
发票一张张截图太浪费程序员的时间，30张发票的截图要浪费1个多小时；
本程序自动将发票号码和发票代码填充到发票截图中；
需要提前通过PS准备底图，每批的发票底图我会定时更新；

## 使用方式

```
git clone https://github.com/Adamyuanyuan/communication-invoice-screenshot.git
cd communication-invoice-screenshot
// 131001862515 指的是 发票代码 258305 指的是起始与末尾的发票号码，2 指的是发票号码前面0的个数
python image.py 131001862515 258305 258327 2
```
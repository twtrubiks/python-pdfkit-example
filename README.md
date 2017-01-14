# python-pdfkit-example
python-pdfkit HTML TO PDF Example

使用 python-pdfkit 將 HTML 轉成 PDF
 
* [Youtube Demo](https://youtu.be/ceIJRWriTig)  
 
常常需要將一些東西轉換成 PDF，今天教你使用 [python-pdfkit](https://github.com/JazzCore/python-pdfkit) 快速完成這個功能。

使用 Python [Flask](http://flask.pocoo.org/) 搭配 [python-pdfkit](https://github.com/JazzCore/python-pdfkit)  實現轉換成 PDF 功能。

## 特色
* 搭配 [python-pdfkit](https://github.com/JazzCore/python-pdfkit) 實現轉換成 PDF 功能 ( HTML 轉成 PDF)。


## 安裝套件 
請先確定電腦有安裝 [Python](https://www.python.org/)

因為轉出 PDF 是用到 [python-pdfkit](https://github.com/JazzCore/python-pdfkit)  以及 [wkhtmltopdf](http://wkhtmltopdf.org/)

所以必須安裝這兩個套件，以下用 Windows 環境介紹

### python-pdfkit
``` 
pip install pdfkit
```
更多 python-pdfkit ，可參考  [python-pdfkit](https://github.com/JazzCore/python-pdfkit) 

### wkhtmltopdf
最後 python 還是會去使用 wkhtmltopdf.exe ，所以請務必安裝 [wkhtmltopdf](http://wkhtmltopdf.org/)

安裝方法很簡單，基本上就是無腦安裝 exe 檔(請選擇符合自己電腦的版本)，請記好自己安裝的路徑

![alt tag](http://i.imgur.com/t13xYR5.png)

![alt tag](http://i.imgur.com/v7N4vIN.png)

安裝好 wkhtmltopdf 之後，建議大家可以先做測試，測試方法如下

先使用 cmd (命令提示字元) 切換到 wkhtmltopdf 路徑下 

接著請在  cmd (命令提示字元) 輸入以下指令

``` 
wkhtmltopdf "https://www.google.com.tw/" out.pdf
```
![alt tag](http://i.imgur.com/IbsxiDn.png)

順利的話，路徑下會多出 out.pdf 的檔案，打開它可以看到我們將 google 的首頁轉成 pdf 文件了

![alt tag](http://i.imgur.com/Mku3y4X.png)

更多 wkhtmltopdf ，可參考  [wkhtmltopdf](http://wkhtmltopdf.org/)


## 開始使用 python-pdfkit

### 設定路徑

前面有提到  python-pdfkit 還是會去使用 wkhtmltopdf.exe，所以我們必須告訴系統自己的 wkhtmltopdf.exe 路徑

``` 
config = pdfkit.configuration(wkhtmltopdf='wkhtmltopdf.exe 存在路徑')
pdfkit.from_url("目標網址", "輸出檔案", configuration=config)
```
``` 
config = pdfkit.configuration(wkhtmltopdf='C:/Program Files (x86)/wkhtmltopdf/bin/wkhtmltopdf.exe')
pdfkit.from_url("https://www.google.com.tw/", "out.pdf", configuration=config)
```
當然，你也可以直接設定電腦的環境變數。

### 一些 python-pdfkit 基本的使用

``` 
import pdfkit

# 指定目標網址 轉成 pdf 
pdfkit.from_url('https://www.google.com.tw/', 'out.pdf')

# 指定目標檔案(html) 轉成 pdf 
pdfkit.from_file('test.html', 'out.pdf')

# 指定目標字串 轉成 pdf 
pdfkit.from_string('Hello!', 'out.pdf')
```

指定目標字串也可以寫 html

``` 
body = """
    <html>
      <head>
        <meta name="pdfkit-page-size" content="Legal"/>
        <meta name="pdfkit-orientation" content="Landscape"/>
      </head>
      Hello World!
      </html>
    """

pdfkit.from_string(body, 'out.pdf')
``` 

合併多的網址、檔案(html) 轉成 pdf 

``` 
pdfkit.from_url(['https://www.google.com.tw/', 'https://tw.yahoo.com/', 'https://shopping.pchome.com.tw/'], 'out.pdf')
pdfkit.from_file(['file1.html', 'file2.html'], 'out.pdf')
``` 

額外多的設定，像是邊距、邊碼、大小
``` 
options = {
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'custom-header' : [
        ('Accept-Encoding', 'gzip')
    ]
    'cookie': [
        ('cookie-name1', 'cookie-value1'),
        ('cookie-name2', 'cookie-value2'),
    ],
    'no-outline': None
}

pdfkit.from_url('https://www.google.com.tw/', 'out.pdf', options=options)
``` 
更多的額外設定的參數，可參考這份說明 [wkhtmltopdf.txt](http://wkhtmltopdf.org/usage/wkhtmltopdf.txt)

P.S <br>
如果出現如下圖(很多黑色框框)，代表你的電腦可能沒安裝字型檔
![alt tag](http://i.imgur.com/RY6QT6y.png)

如果出現亂碼(如下圖)，代表是編碼問題

![alt tag](http://i.imgur.com/QIxMIw9.png)


指定編碼即可解決這個問題
``` 
options = {
        'encoding': 'UTF-8'
    }
pdfkit.from_string(body, filename, configuration=config, options=options)
```
![alt tag](http://i.imgur.com/q0OGpv9.png)

如果出現下方的錯誤
``` 
IOError: 'No wkhtmltopdf executable found'
```
通常是你沒安裝 wkhtmltopdf 或是 你忘記指定  wkhtmltopdf.exe 的路徑



## 執行畫面 (簡單範例)

執行程式，請用 <b>系統管理員</b> 執行 (不然有時候會無法存取)

請將記得安裝套件
``` 
pip install -r requirements.txt
``` 


首頁
![alt tag](http://i.imgur.com/kF3723e.jpg)
可以輸入網址  (將目標網址轉成 PDF )

PDF template (範例)
![alt tag](http://i.imgur.com/4wLFq1x.jpg)
 
## 執行環境
* Python 3.4.3

## Reference 
* [python-pdfkit](https://github.com/JazzCore/python-pdfkit/) 
* [wkhtmltopdf](http://wkhtmltopdf.org/)

## License
MIT license

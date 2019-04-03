# What this package will crawl

1. 保險業資訊公開觀測站

http://ins-info.ib.gov.tw/customer/announceinfo.aspx

保險商品
承保範圍, 不保事項, 保單紅利,拒保職業,理賠申請文件


2. 保險經紀人公會

http://www.piba.org.tw/
首頁  >>  會員名冊

經紀人 的

執業型態	執業單位	服務單位地址

3. 保險代理人同業公會

http://www.ciaa.org.tw/pages/CIAA_NameList_01.aspx

會員名錄 >> 	

壽險會員|產險會員|個人會員

的

會員名稱	負責人	ZIP	聯絡地址	聯絡電話


# Installation
1

```
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```


2
Use Headless Browser PhantomJS, you can download it here:
http://phantomjs.org/download.html

Name the directory phantomjs/

```
├── README.md
├── crawler.py
├── easy_intro.py
├── phantomjs
│   ├── ChangeLog
│   ├── LICENSE.BSD
│   ├── README.md
│   ├── bin
│   ├── examples
│   └── third-party.txt
├── requirements.txt
└── venv
```


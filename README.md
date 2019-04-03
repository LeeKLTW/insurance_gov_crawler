# What this package will crawl

1. 保險業資訊公開觀測站

http://ins-info.ib.gov.tw/customer/announceinfo.aspx

公司 保險商品

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


4. 財團法人保險事業發展中心

http://insprod.tii.org.tw/database/insurance/query.asp
並不是很穩定


# Installation
1

```
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```


2
Use chromedriver, you can download it here:
http://chromedriver.chromium.org/

Name it chromedriver

```
├── README.md
├── crawler.py
├── easy_intro.py
├── chromedriver
├── requirements.txt
└── venv
```

---

#免責事由: 除外責任與不保事項

http://www.insop.org.tw/resources/forum/20170815.pdf

除外責任與不保事項，都是保險單條款約定保險人的免責事由，但在保險人免責的意義上，仍有些許的不同。

## 除外責任
除外責任，為英美法學者所謂的「除外條款（Exceptions clause）」，即將原包括在契約內之危險（法律上必須負責之危險）排除在契約承保範圍之外。
除外條款釐定的目的，在將除外責任危險明示於契約條款內，保險人依約定不
予理賠，以明確保險的範圍。現行保險法所列示的除外責任危險，主要有：

（一）損害係出於要保人或被保險人的故意（保險法第二十九條第二項但書）。

（二）被保險人故意自殺（保險法第一百零九條第一項）或墮胎所致疾病、殘
廢、流產或死亡（保險法第一百二十八條）或因犯罪行為，所致傷害、殘
廢或死亡（保險法第一百三十三條）。

（三）被保險人因犯罪處死或拒捕或越獄致死（保險法第一百零九條第三項）。

（四）要保人故意致被保險人於死（保險法第一百二十一條第三項）。

## 不保事項
不保事項，為英美法學者所謂的「不包括條款（Exclusionary clause）」，即保險契約的當事人，於保險契約中特別約定，在某種指定情況發生時，保險人
得以免除保險金額給付之條款。不保事項釐定的目的，在將會讓保費上升到沒人能接受的過高危險，特地拉出來不做承保，以降低這部份的危險讓保險費與保險人承受的危險下降，以明確排除被保險人在特定情況發生時的危險，以維
持費率的公平性。
（一）不保之危險事故（Excel Perils）。如戰爭（不論宣戰與否）、類似戰爭行為、叛亂等。

（二）不保之損失（Excel Losses）。如車體損失保險承保車輛碰撞成的損失，但對於被保險汽車之毀損滅失所致之附帶損失，包括貶值及不能使用的損失皆不保之列。

（三）不保之財產（Excel Property）。如住宅火災保險單中對於貨幣、證件、文稿、有價證券、珠寶、藝術品等財務損失，若未特別約定載明在承保範圍內（須加繳保險費），皆不予承保。

（四）不保之所在地（Excel Locations）。如住宅火災保險通常僅限於一定所在地的財產（建築物及建築物內動產）。

（五）不保之期間（Excel Period）。如傷害保險被保險人從事特定超乎尋常危險活動（從事角力、摔跤、柔道、空手道、跆拳道、馬術、拳擊、特技表演、汽車、機車及自由車等的競賽或表演）的期間。
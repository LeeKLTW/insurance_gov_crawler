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

一份保單中有幾個重要部分，拒保職業、產品名稱、承保範圍、除外責任與不保事項(後說明)、申請理賠文件。
主要有兩個問題：1.「可以保嗎？」、2.「有賠嗎？」

1.「可以保嗎？」=> 拒保職業

2.「有賠嗎？」=> 承保範圍、除外責任與不保事項

但是「承保範圍」變動太大，比較乾淨的方式是用「申請理賠文件」頗析，以下文為例：

```
1、申請身故保險金：(1)保險金申請書(2)死亡診斷書或相驗屍體證明書(3)病理組織檢查報告及診斷證明書(防癌險因癌症身故時需要)(4)監護人身分證明(受益人未滿七歲或受禁治產宣告者須附監護人身分證明)(5)除戶戶籍謄本(6)受益人身分證明(戶籍謄本或身分證影本)(7)保險單(8)意外事故證明文件(因意外身故時需要)
2、申請全殘廢或殘廢保險金：(1)保險金申請書(2)殘廢診斷書(由本公司提供表格由醫院出具證明或使用勞保殘廢診斷書)(3)監護人身分證明(受益人未滿七歲或受禁治產宣告者須附監護人身分證明)(4)X光片(截肢時需用)(5)保險單(全殘廢時需用)(6)意外事故證明文件(申請意外殘廢或全殘保險金時需要)
3、申請住院醫療及日額保險金：(1)保險金申請書(2)醫療費用收據(含明細表)(3)診斷書(4)戶口名簿影本(要保書未登載被保險人與事故人親屬關係時需要)(5)病理組織檢查報告(首次申請防癌保險金時需要)(6)X光片(申請意外日額償金骨折未住院時需要)
4、申請傷害醫療保險金：(1)保險金申請書(2)醫療費用收據(含明細表)(3)診斷書(4)X光片(骨折於國術館就診者，此部份不包括一年期團體定期綜合保險)(5)戶口名簿影本(要保書未記載被保險人與事故人親屬關係時需要)
5、申請喪葬津貼：(1)保險金申請書(2)死亡診斷書(3)除戶戶籍謄本(4)親屬關係證明文件(戶口名簿或身分證影本)
6、申請生育津貼(1)保險金申請書(事故人應填新生兒並由監護人蓋章)(2)出生證明(3)戶籍謄本或戶口名簿影本
7、申請重大疾病豁免保險：(1)保險金申請書(2)診斷書(3)病理組織檢查報告(罹患癌症時需要)(4)保險單
```

身故、殘廢、住院、傷害醫療有賠，
另外喪葬津貼、生育津貼，再加上重大疾病豁免。

2.「有賠嗎？」=> 直接回答有沒有賠，並說要帶哪些文件，這也是比較符合客服的口吻。

小bug：有些保單會把「通知義務」放到承保範圍裡。

說明：除外責任與不保事項，以下說明為什麼法律上區分兩者，但因為不賠所以實際上爬蟲也是將資料也是存在一起。

除外責任：法律上必須負責之危險排除在契約承保範圍之外（自殺、殺人、墮胎、拒捕、越獄）

不保事項：沒人能接受的過高危險（
事故：戰爭;
損失：車體維修後的貶值;
財產：藝術品;
所在地：不動產所在地;
期間：競技或特技）

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
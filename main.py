from datetime import date
from scapper import mainScapper
from pdf_creator import create_pdf
#yyyy-mm-dd
dates=[["2010-01-01","2010-12-30"],
["2011-01-01","2011-12-30"],
['2012-01-01','2012-12-30'],
['2013-01-01','2013-12-30'],
['2014-01-01','2014-12-30'],
['2015-01-01','2015-12-30'],
['2016-01-01','2016-12-30'],
['2017-01-01','2017-12-30'],
['2018-01-01','2018-12-30'],
['2019-01-01','2019-12-30'],
['2020-01-01','2020-12-30'],
['2021-01-01','2021-12-30']]
tagnames=["Oklahoma AND Agriculture"]
tagnames=[i.split() for i in tagnames]
for tag in tagnames:
    for date in dates[-2:]:
        main_url=f"""https://tulsaworld.com/search/?nsa=eedition&app=editorial&d1={date[0]}&d2={date[1]}&s=start_time&sd=desc&l=100&t=article&q={"+".join(tag)}&d1={date[0]}&d2={date[1]}"""
        mainScrapperList=mainScapper(main_url)
        for content in mainScrapperList:
            print(content[0])
            create_pdf(content, "tulsa/"+date[0][:4]+"/")
# import os 
# for i in dates:
#     os.mkdir("tulsa/"+i[0][:4])
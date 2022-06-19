def scrapper(url):
    import requests
    from bs4 import BeautifulSoup
    tulsa_link="https://tulsaworld.com/"
    r=requests.get(url).text
    results=BeautifulSoup(r, 'html.parser')
    aritcle=results.find_all("article") 
    links=[]
    for i in aritcle:
        link=i.find("a")['href']
        if ".html" in link:
            links.append(tulsa_link+link)
    print("links scrapped")
    return links
def article_object(url):
    from newspaper import Article
    article=Article(url)
    try:
        article.download()
        article.parse()
        article.nlp()
        return article
    except:
        pass
    
def mainScapper(url):
    scrappedLinks=scrapper(url)
    scrappedContent=[]
    for i in scrappedLinks:
        article=article_object(i)
        try:
            temp_list=[article.title, article.text]
            scrappedContent.append(temp_list)
        except:
            pass
    print("articles done")
    return scrappedContent


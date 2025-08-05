from newspaper import Article

def fetch_articles(urls):
    articles = []
    for url in urls:
        try:
            article = Article(url)
            article.download()
            article.parse()
            articles.append({"title": article.title, "text": article.text, "url": url})
        except:
            continue
    return articles

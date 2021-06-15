
from newspaper import Article
# import newspaper

url = "https://piaui.folha.uol.com.br/lupa/2021/06/"

# article = Article(url)

# lupa = newspaper.build(url,memoize_articles=False)
#
# with open('links.txt','w') as f_out:
#     for article in lupa.articles:
#         f_out.write("%s\n" % article.url)

# print(article.download())
#
# print(article.html)
#
# print(type(article.html))


url = "https://piaui.folha.uol.com.br/lupa/2021/06/14/verificamos-washington-post-motociata-bolsonaro/"

article = Article(url)

article.download()

with open('pagina.html','w') as f_out:
    f_out.write(article.html)


article.parse()

print(article.authors)

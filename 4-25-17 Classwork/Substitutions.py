import json

def betterNews(filename):
    news = open(filename, 'r').read()
    jfile = open('substitutions.json','r').read()
    subs = json.loads(jfile)
    for key in subs:
        news = news.replace(key, subs[key])
    newfile = open('betternews.txt','w')
    newfile.write(news)
    newfile.close()

def main():
    myfile = 'article.txt'
    betterNews(myfile)

main()

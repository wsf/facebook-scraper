from facebook_scraper import get_posts

r  =  get_posts('asartorio', pages=30)

for post in get_posts('PythonParaTodos', pages=3):
    print(post['text'][:50])


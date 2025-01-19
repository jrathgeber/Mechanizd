
import BlogArticle as Article
import BlogPost as Post

article_number = "028"
key_words = "What is the biggest thing ever sold on ebay"

slug = key_words.replace(" ", "_")

Article.new_article(article_number, slug)
Post.new_post(article_number, slug)

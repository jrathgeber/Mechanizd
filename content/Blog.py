
import BlogArticle as Article
import BlogPost as Post

article_number = "024"
key_words = "increase your impact"

slug = key_words.replace(" ", "_")

Article.new_article(article_number, slug)
Post.new_post(article_number, slug)

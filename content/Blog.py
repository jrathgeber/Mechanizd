
import BlogArticle as Article
import BlogPost as Post

article_number = "028"
key_words = "What is the biggest thing ever sold on ebay"

slug = key_words.replace(" ", "_")

file_path_dev = "zappy\\"
file_path_prod = "C:\\dev\\godaddy\\vcard\\blogpost\Articles\\"
file_path_laptop = "G:\\gd93\\vcard\\blogpost\Articles\\"

Article.new_article(file_path_dev, article_number, slug)
Post.new_post(file_path_dev, article_number, slug)

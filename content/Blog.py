
import BlogArticle as Article
import BlogPost as Post
import BlogIndex as IndexPage

article_number = "028"
key_words = "how to sell your stuff on ebay"

slug = key_words.replace(" ", "_")

file_path_dev = "zappy\\"
file_path_prod = "C:\\dev\\godaddy\\vcard\\blogpost\\Articles\\"

file_path_laptop = "D:\\gd23\\vcard\\blogpost\\Articles\\"
file_path_laptop_bp = "D:\\gd23\\vcard\\blogpost\\"

#Article.new_article(file_path_laptop, article_number, slug)
#Post.new_post(file_path_laptop_bp, article_number, slug, key_words)

IndexPage.add_blog(file_path_laptop_bp, article_number, slug, key_words, "Jan22")


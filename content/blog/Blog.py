
import BlogArticle as Article
import BlogPost as Post
import BlogIndex as IndexPage
import BlogImage as Image
import BlogArticleStyle as ArticleStyle
import content.prompts.Jacky1 as j1
import configparser
from datetime import date


# Get Reference to Properties
config = configparser.ConfigParser()
config.read('C:\\etc\\properties.ini')

blog_path = str(config['blog']['blog_path'])

article_number = "034"
key_words = "how to get a post from notion via python api"

further_info = j1.get_prompt(key_words)

slug = key_words.replace(" ", "_")

file_path_dev = "../temp\\"
file_path_prod = blog_path + "\\blogpost\\Articles\\"

file_path_laptop = blog_path + "\\blogpost\\Articles\\"
file_path_laptop_bp = blog_path + "\\blogpost\\"

file_path_laptop_image = blog_path + "\\assets\\custom\\images\\blog\\"
file_path_laptop_thumb = blog_path + "\\assets\\custom\\images\\blog\\thumbs\\"

#Article.new_article(file_path_laptop, article_number, slug, key_words, further_info)
#Post.new_post(file_path_laptop_bp, article_number, slug, key_words)
#Image.new_image(file_path_laptop_image, file_path_laptop_thumb, article_number, slug, key_words, "Feb 02, 2025")
#IndexPage.add_blog(file_path_laptop_bp, article_number, slug, key_words, "Feb 16, 2025")

#ArticleStyle.replace_stype(file_path_laptop_bp, article_number, slug, key_words, "Feb 16, 2025")
from content.blog import BlogArticle as Article, BlogPost as Post, BlogIndex as IndexPage, BlogImage as Image
import content.prompts.Jacky2 as j2
import configparser

# Get Reference to Properties
config = configparser.ConfigParser()
config.read('C:\\etc\\properties.ini')

blog_path = str(config['blog']['blog_path'])

# Get Reference to Properties
config = configparser.ConfigParser()
config.read('C:\\etc\\properties.ini')

article_number = "029"
key_words = "How to start a cracking youtube channel"

further_info = j2.get_prompt(key_words)

slug = key_words.replace(" ", "_")

file_path_dev = "../temp\\"
file_path_prod = blog_path + "\\blogpost\\Articles\\"

file_path_laptop = blog_path + "\\blogpost\\Articles\\"
file_path_laptop_bp = blog_path + "\\blogpost\\"

file_path_laptop_image = blog_path + "\\assets\\custom\\images\\blog\\"
file_path_laptop_thumb = blog_path + "\\assets\\custom\\images\\blog\\"

Article.new_article(file_path_laptop, article_number, slug, key_words, further_info)
Post.new_post(file_path_laptop_bp, article_number, slug, key_words)
Image.new_image(file_path_laptop_image, file_path_laptop_thumb, article_number, slug, key_words, "Jan22")
IndexPage.add_blog(file_path_laptop_bp, article_number, slug, key_words, "Feb 01, 2025")


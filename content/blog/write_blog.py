import content.blog.BlogArticle as Article
import content.blog.BlogPost as Post
import content.blog.BlogIndex as IndexPage
import content.blog.BlogImage as Image
import content.blog.BlogArticleStyle as ArticleStyle
import content.prompts.Jacky1 as j1
import configparser
from datetime import date



def write(title):

    # Get today's Date
    today = date.today()
    formatted_date = today.strftime("%b %d, %Y")
    print("Processing " + formatted_date)

    # Get Reference to Properties
    config = configparser.ConfigParser()
    config.read('C:\\etc\\properties.ini')

    # blog path
    # blog_path = "C:\\dev\\godaddy\\vcard"
    # blog_path = "D:\\gd23\\vcard"
    blog_path = str(config['blog']['blog_path'])

    print("BlogPath " + blog_path)

    article_number = "040"
    key_words = title

    further_info = j1.get_prompt(key_words)

    slug = key_words.replace(" ", "_")

    file_path_laptop = blog_path + "\\blogpost\\Articles\\"
    file_path_laptop_bp = blog_path + "\\blogpost\\"
    file_path_laptop_image = blog_path + "\\assets\\custom\\images\\blog\\"
    file_path_laptop_thumb = blog_path + "\\assets\\custom\\images\\blog\\thumbs\\"

    Article.new_article(file_path_laptop, article_number, slug, key_words, further_info)
    Post.new_post(file_path_laptop_bp, article_number, slug, key_words)
    Image.new_image(file_path_laptop_image, file_path_laptop_thumb, article_number, slug, key_words, formatted_date)
    IndexPage.add_blog(blog_path, article_number, slug, key_words, formatted_date)

    ArticleStyle.replace_stype(file_path_laptop_bp, article_number, slug, key_words, formatted_date)
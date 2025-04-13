import blog.BlogArticle as Article
import blog.BlogPost as Post
import blog.BlogIndex as IndexPage
import blog.BlogImage as Image
import blog.BlogArticleStyle as ArticleStyle
import blog.update_index as BlogIndex

import prompts.aBlog as BlogPrompt
import prompts.Code_css as code_css
import godaddy.publish_blog as Gd

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
    blog_index = str(config['blog']['blog_index'])

    print("BlogPath " + blog_path)
    print("BlogIndex " + str(int(blog_index)+1))

    article_number = BlogIndex.convert_to_three_digit_string(int(blog_index)+1)
    key_words = title

    full_prompt = BlogPrompt.get_prompt(key_words) + code_css.get_css_prompt("nothing")

    slug = key_words.replace(" ", "_")

    file_path = blog_path + "\\blogpost\\Articles\\"
    file_path_bp = blog_path + "\\blogpost\\"
    file_path_image = blog_path + "\\assets\\custom\\images\\blog\\"
    file_path_thumb = blog_path + "\\assets\\custom\\images\\blog\\thumbs\\"

    Article.new_article(file_path, article_number, slug, key_words, full_prompt)
    Post.new_post(file_path_bp, article_number, slug, key_words, formatted_date)
    Image.new_image(file_path_image, file_path_thumb, article_number, slug, key_words, formatted_date)
    IndexPage.add_blog(blog_path, article_number, slug, key_words, formatted_date)
    ArticleStyle.replace_stype(file_path_bp, article_number, slug, key_words, formatted_date)

    BlogIndex.update_config_index(int(blog_index)+1)

    Gd.publish_blog(file_path, "Article")


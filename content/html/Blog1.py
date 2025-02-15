from content.html import BlogArticle as Article, BlogPost as Post, BlogIndex as IndexPage, BlogImage as Image
import content.prompts.Jacky2 as j2

article_number = "029"
key_words = "How to start a cracking youtube channel"

further_info = j2.get_prompt(key_words)

slug = key_words.replace(" ", "_")

file_path_dev = "../temp\\"
file_path_prod = "C:\\dev\\godaddy\\vcard\\blogpost\\Articles\\"

file_path_laptop = "D:\\gd23\\vcard\\blogpost\\Articles\\"
file_path_laptop_bp = "D:\\gd23\\vcard\\blogpost\\"

file_path_laptop_image = "D:\\gd23\\vcard\\assets\\custom\\images\\blog\\"
file_path_laptop_thumb = "D:\\gd23\\vcard\\assets\\custom\\images\\blog\\"

Article.new_article(file_path_laptop, article_number, slug, key_words, further_info)
Post.new_post(file_path_laptop_bp, article_number, slug, key_words)
Image.new_image(file_path_laptop_image, file_path_laptop_thumb, article_number, slug, key_words, "Jan22")
IndexPage.add_blog(file_path_laptop_bp, article_number, slug, key_words, "Feb 01, 2025")


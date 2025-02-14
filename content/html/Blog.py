
import BlogArticle as Article
import BlogPost as Post
import BlogIndex as IndexPage
import BlogImage as Image
import BlogArticleStyle as ArticleStyle
import content.prompts.Jacky1 as j1

article_number = "029"
key_words = "how to start a cracking youtube channel"

further_info = j1.get_prompt()

slug = key_words.replace(" ", "_")

file_path_dev = "../zappy\\"
file_path_prod = "C:\\dev\\godaddy\\vcard\\blogpost\\Articles\\"

file_path_laptop = "D:\\gd23\\vcard\\blogpost\\Articles\\"
file_path_laptop_bp = "D:\\gd23\\vcard\\blogpost\\"

file_path_laptop_image = "D:\\gd23\\vcard\\assets\\custom\\images\\blog\\"
file_path_laptop_thumb = "D:\\gd23\\vcard\\assets\\custom\\images\\blog\\thumbs\\"

#Article.new_article(file_path_laptop, article_number, slug, key_words, further_info)
#Post.new_post(file_path_laptop_bp, article_number, slug, key_words)
#Image.new_image(file_path_laptop_image, file_path_laptop_thumb, article_number, slug, key_words, "Feb 02, 2025")
#IndexPage.add_blog(file_path_laptop_bp, article_number, slug, key_words, "Feb 02, 2025")

ArticleStyle.replace_stype(file_path_laptop_bp, article_number, slug, key_words, "Feb 05, 2025")
import content.blog.BlogArticle as Article
import content.blog.BlogPost as Post
import content.blog.BlogIndex as IndexPage
import content.blog.BlogImage as Image
import content.blog.BlogArticleStyle as ArticleStyle
import content.prompts.Jacky1 as j1

def write(title):

    article_number = "035"
    # key_words = "how to get a post from notion via python api"
    key_words = title

    further_info = j1.get_prompt(key_words)

    slug = key_words.replace(" ", "_")

    file_path_dev = "../temp\\"
    file_path_prod = "C:\\dev\\godaddy\\vcard\\blogpost\\Articles\\"

    file_path_laptop = "D:\\gd23\\vcard\\blogpost\\Articles\\"
    file_path_laptop_bp = "D:\\gd23\\vcard\\blogpost\\"

    file_path_laptop_image = "D:\\gd23\\vcard\\assets\\custom\\images\\blog\\"
    file_path_laptop_thumb = "D:\\gd23\\vcard\\assets\\custom\\images\\blog\\thumbs\\"

    Article.new_article(file_path_laptop, article_number, slug, key_words, further_info)
    Post.new_post(file_path_laptop_bp, article_number, slug, key_words)
    Image.new_image(file_path_laptop_image, file_path_laptop_thumb, article_number, slug, key_words, "Mar 03, 2025")
    IndexPage.add_blog(file_path_laptop_bp, article_number, slug, key_words, "Mar 03 3, 2025")

    ArticleStyle.replace_stype(file_path_laptop_bp, article_number, slug, key_words, "Mar 03, 2025")
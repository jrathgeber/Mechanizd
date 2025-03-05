from content.blog import BlogImage as Image
import content.prompts.Jacky3 as j3

article_number = "030"
key_words = "What is VPN"

further_info = j3.get_prompt(key_words)

slug = key_words.replace(" ", "_")

file_path_dev = "../temp\\"
file_path_prod = "C:\\dev\\godaddy\\vcard\\blogpost\\Articles\\"

file_path_laptop = "D:\\gd23\\vcard\\blogpost\\Articles\\"
file_path_laptop_bp = "D:\\gd23\\vcard\\blogpost\\"

file_path_laptop_image = "D:\\gd23\\vcard\\assets\\custom\\images\\blog\\"
file_path_laptop_thumb = "D:\\gd23\\vcard\\assets\\custom\\images\\blog\\thumbs\\"

#Article.new_article(file_path_laptop, article_number, slug, key_words, further_info)
#Post.new_post(file_path_laptop_bp, article_number, slug, key_words)
Image.new_image(file_path_laptop_image, file_path_laptop_thumb, article_number, slug, key_words, "Jan22")
#IndexPage.add_blog(file_path_laptop_bp, article_number, slug, key_words, "Jan22")


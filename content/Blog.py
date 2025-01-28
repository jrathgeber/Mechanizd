
import BlogArticle as Article
import BlogPost as Post
import BlogIndex as IndexPage
import BlogImage as Image

article_number = "028"
key_words = "How to sell your stuff on ebay"

further_info = """

Make sure to include this info in the post: 
Some of the best AI detectors include: 
Originality.ai: A top overall AI detector that can highlight AI text 
GPTZero: An AI detector with writing analysis features that's good for educators 
Sapling: A free AI detector that's good for customer-facing teams 
Copyleaks: An AI detector that's good for content marketing agencies 
Winston AI: An AI detector that's good for businesses that want to detect AI-generated content in marketing and advertising 
ZeroGPT: An AI detector that's available on WhatsApp and Telegram 
TraceGPT: An AI detector that's known for its accuracy 
Hive: A free AI detector 
Smodin: An AI detector that offers unlimited use for an affordable price 

"""


slug = key_words.replace(" ", "_")

file_path_dev = "zappy\\"
file_path_prod = "C:\\dev\\godaddy\\vcard\\blogpost\\Articles\\"

file_path_laptop = "D:\\gd23\\vcard\\blogpost\\Articles\\"
file_path_laptop_bp = "D:\\gd23\\vcard\\blogpost\\"

file_path_laptop_image = "D:\\gd23\\vcard\\assets\\custom\\images\\blog\\"
file_path_laptop_thumb = "D:\\gd23\\vcard\\assets\\custom\\images\\blog\\"

#Article.new_article(file_path_laptop, article_number, slug, key_words, further_info)
#Post.new_post(file_path_laptop_bp, article_number, slug, key_words)
#Image.new_image(file_path_laptop_image, file_path_laptop_thumb, article_number, slug, key_words, "Jan22")
IndexPage.add_blog(file_path_laptop_bp, article_number, slug, key_words, "Jan22")


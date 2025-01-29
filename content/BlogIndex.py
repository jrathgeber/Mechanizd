# -*- coding: utf-8 -*-

import time
from shutil import copyfile


def copywrite(copy, article_number, slug, key_words, todaydate):

    copy.write('\n\n')
    copy.write('    			  <!-- ' + article_number + " " + key_words + ' -->\n')
    copy.write('    			  <div class="grid-item branding col-md-4 col-sm-6">\n')
    copy.write('    			    <div class="item-wrap">\n')
    copy.write('    			       <figure class="">\n')
    copy.write('    			          <div class="popup-call">\n')
    copy.write('    			             <a href="assets/custom/images/blog/' + article_number + '_' + slug + '.jpg" class="gallery-item"><i class="flaticon-arrows-4"></i></a>\n')
    copy.write('    			          </div>\n')
    copy.write('    			          <img src="assets/custom/images/blog/thumbs/' + article_number + '_' + slug + '.jpg" class="img-responsive" alt="img03"/>\n')
    copy.write('    			          <figcaption>\n')
    copy.write('    			             <div class="post-meta"><span>by <a href="#!">Jason Rathgeber</a>,</span> <span>' + todaydate + '</span></div>\n')
    copy.write('    			             <div class="post-header">\n')
    copy.write('    			                <h5><a href="blogpost/blogpost_' + article_number + '_' + slug + '.html">' + key_words + '</a></h5>\n')
    copy.write('    			             </div>\n')
    copy.write('    			             <div class="post-entry">\n')
    copy.write('    			                <p> ' + key_words + '</p>\n')
    copy.write('    			             </div>\n')
    copy.write('    			             <div class="post-tag pull-left">\n')
    copy.write('    			                <span><a href="#branding" data-filter=".branding">Branding</a>,</span>\n')
    copy.write('    			             </div>\n')
    copy.write('    			             <div class="post-more-link pull-right"><a href="blogpost/blogpost_' + article_number + '_' + slug + '.html">More<i class="fa fa-long-arrow-right right"></i></a></div>\n')
    copy.write('    			          </figcaption>\n')
    copy.write('    			       </figure>\n')
    copy.write('    			    </div>\n')
    copy.write('    			</div> \n')


def add_blog(file_path_laptop_bp, article_number, slug, key_words, todaydate):

    f = open(r"D:\\gd23\\vcard\\blog.html", "r")

    #copy = open("D:\\gd23\\vcard\\blog.html", "w")

    copy = open("zappy\\blog.html", "w")
    
    for line in f:

        copy.write(line)
        if '<div id="posts" class="row popup-container">' in line:

            copywrite(copy, article_number, slug, key_words, todaydate)
        
    print(line)

    f.close()
    copy.close()

    copyfile('zappy\\blog.html"',
             'D:\\gd23\\vcard\\blog.html')


    # Give it some time
    time.sleep(3)

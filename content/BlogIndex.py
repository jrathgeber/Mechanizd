# -*- coding: utf-8 -*-

import time
from shutil import copyfile


def copywrite(copy, todaydate, symbols):

    copy.write('			  <!-- 024 Personal Branding -->\n')
    copy.write('			  <div class="grid-item branding col-md-4 col-sm-6">\n')
    copy.write('			    <div class="item-wrap">\n')
    copy.write('			       <figure class="">\n')
    copy.write('			          <div class="popup-call">\n')
    copy.write('			             <a href="assets/custom/images/blog/024_influence.jpeg" class="gallery-item"><i class="flaticon-arrows-4"></i></a>\n')
    copy.write('			          </div>\n')
    copy.write('			          <img src="assets/custom/images/blog/thumbs/024_influence.jpeg" class="img-responsive" alt="img03"/>\n')
    copy.write('			          <figcaption>\n')
    copy.write('			             <div class="post-meta"><span>by <a href="#!">Jason Rathgeber</a>,</span> <span>December 16, 2024</span></div>\n')
    copy.write('			             <div class="post-header">\n')
    copy.write('			                <h5><a href="blogpost/blogpost_024_increase_your_impact.html">Scale Your Influence</a></h5>\n')
    copy.write('			             </div>\n')
    copy.write('			             <div class="post-entry">\n')
    copy.write('			                <p>Increase your impact online</p>\n')
    copy.write('			             </div>\n')
    copy.write('			             <div class="post-tag pull-left">\n')
    copy.write('			                <span><a href="#branding" data-filter=".branding">Branding</a>,</span>\n')
    copy.write('			             </div>\n')
    copy.write('			             <div class="post-more-link pull-right"><a href="blogpost/blogpost_024_increase_your_impact.html">More<i class="fa fa-long-arrow-right right"></i></a></div>\n')
    copy.write('			          </figcaption>\n')
    copy.write('			       </figure>\n')
    copy.write('			    </div>\n')
    copy.write('			</div> \n')


def add_blog(file_path_laptop_bp, article_number, slug, key_words, todaydate):

    f = open(r"D:\\gd23\\vcard\\blog.html", "r")
    
    copy = open("zappy\\blog.html", "w")
    
    x=0
    for line in f:
        x=x*2
        if x==4:
            copywrite(copy, todaydate)
        if 'MaxAlpha' in line:
            x=1     
        copy.write(line)

        
    print(line)
    f.close()
    copy.close()
    
    # Give it some time
    time.sleep(3)

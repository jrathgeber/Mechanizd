# -*- coding: utf-8 -*-

import time
from shutil import copyfile


def copywrite(copy, article_number, slug, key_words, todaydate):

    copy.write('\n\n')
    copy.write('    <link rel="stylesheet" href="./medium.css" type="text/css" />\n')
    copy.write('    <link rel="canonical" href="https://www.jasonrathgeber.com/vcard/blogpost/blogpost_' + article_number + '_' + slug + '.html" /> \n')
    copy.write('\n\n')


def replace_stype(blog_path, article_number, slug, key_words, today_date):

    f = open(blog_path + "\\articles\\article_" + article_number + '_' + slug + ".html", "r")
    copy = open("article.html", "w")

    for line in f:

        if '<style type="text/css">' in line:
            for _ in range(127):
                next(f)
            copywrite(copy, article_number, slug, key_words, today_date)
        else:
            copy.write(line)

    f.close()
    copy.close()

    copyfile('article.html', blog_path + '\\articles\\article_' + article_number + '_' + slug + '.html')

    # Give it some time
    time.sleep(3)

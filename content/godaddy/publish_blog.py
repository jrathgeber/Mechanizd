import time
import ftplib
import configparser
from shutil import copyfile

config = configparser.ConfigParser()
config.read('C:\etc\properties.ini')

gdurl = config['godaddy']['godaddy.url']
gduser = config['godaddy']['godaddy.user']
gdpass = config['godaddy']['godaddy.pass']

session = ftplib.FTP(gdurl, gduser, gdpass)

def publish_blog(from_file, blog_type):

    if blog_type == "post":
        post_file = open(from_file, 'rb')
        session.storbinary('STOR /mech/output/RightEdge/Live/RightEdgeResults.htm', post_file)  # send the file
        post_file.close()

    if blog_type == "article":
        article_file = open(from_file, 'rb')
        session.storbinary('STOR /mech/output/RightEdge/Live/RightEdgeResults.htm', article_file)  # send the file
        article_file.close()

    if blog_type == "image":
        image_file = open(from_file, 'rb')
        session.storbinary('STOR /mech/output/RightEdge/Live/RightEdgeResults.htm', image_file)  # send the file
        image_file.close()

    if blog_type == "thumb":
        thumb_file = open(from_file, 'rb')
        session.storbinary('STOR /mech/output/RightEdge/Live/RightEdgeResults.htm', thumb_file)  # send the file
        thumb_file.close()

    if blog_type == "blog":
        blog_file = open(from_file, 'rb')
        session.storbinary('STOR /mech/output/RightEdge/Live/RightEdgeResults.htm', blog_file)  # send the file
        blog_file.close()

    session.quit()

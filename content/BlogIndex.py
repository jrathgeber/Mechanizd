# -*- coding: utf-8 -*-

import time
from shutil import copyfile


def copywrite(copy, todaydate, symbols, maxdata):

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



def getSymbolConfig(tickers, todaydate, maxdata):

    #tickers = ['SPI', 'ICON', 'CNET', 'RIOT', 'HMNY']
    #todaydate = "20180127"
    
    f = open(r"C:\Users\Jason\AppData\Roaming\Yye Software\RightEdge\2010.1.0.0\SymbolConfig.xml", "r")
    #f = open(r"SymbolConfigStart.xml", "r")
    
    copy = open("SymbolConfig.xml", "w")
    
    x=0
    for line in f:
        x=x*2
        if x==4:
            copywrite(copy, todaydate, tickers, maxdata)
        if 'MaxAlpha' in line:
            x=1     
        copy.write(line)
        
        
        
    # print(line)
    f.close()
    copy.close()
    
    # Give it some time
    time.sleep(3)
    
    # Put the file in the right place
    copyfile('SymbolConfig.xml', 'C:\\Users\\Jason\\AppData\\Roaming\\Yye Software\\RightEdge\\2010.1.0.0\\SymbolConfig.xml') 
    
    #Backup
    copyfile('C:\\Users\\Jason\\AppData\\Roaming\\Yye Software\\RightEdge\\2010.1.0.0\\SymbolConfig.xml', 'F:\\RightEdge\\MaxAlpha\\SymbolConfig'+todaydate+'.xml') 
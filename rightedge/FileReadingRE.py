# -*- coding: utf-8 -*-
import glob
import re
import time


def fileReading(location, location1, link):

    timestr = time.strftime("%d%m%y")
    
    print (glob.glob("*.txt"))
    
    thelist = glob.glob(location)
    myFile = open(location1 ,'w')
    
    myFile.write('<!DOCTYPE html>\n')
    myFile.write('<html>\n')
    myFile.write("<style media='screen' type='text/css'>");
    myFile.write(".datagrid table { border-collapse: collapse; text-align: left; width: 100%; } .datagrid {font: normal 12px/150% Arial, Helvetica, sans-serif; background: #fff; overflow: hidden; border: 1px solid #006699; -webkit-border-radius: 3px; -moz-border-radius: 3px; border-radius: 3px; }.datagrid table td, .datagrid table th { padding: 3px 10px; }.datagrid table thead th {background:-webkit-gradient( linear, left top, left bottom, color-stop(0.05, #006699), color-stop(1, #00557F) );background:-moz-linear-gradient( center top, #006699 5%, #00557F 100% );filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#006699', endColorstr='#00557F');background-color:#006699; color:#FFFFFF; font-size: 15px; font-weight: bold; border-left: 1px solid #0070A8; } .datagrid table thead th:first-child { border: none; }.datagrid table tbody td { color: #00496B; border-left: 1px solid #E1EEF4;font-size: 12px;font-weight: normal; }.datagrid table tbody .alt td { background: #E1EEF4; color: #00496B; }.datagrid table tbody td:first-child { border-left: none; }.datagrid table tbody tr:last-child td { border-bottom: none; }.datagrid table tfoot td div { border-top: 1px solid #006699;background: #E1EEF4;} .datagrid table tfoot td { padding: 0; font-size: 12px } .datagrid table tfoot td div{ padding: 2px; }.datagrid table tfoot td ul { margin: 0; padding:0; list-style: none; text-align: right; }.datagrid table tfoot  li { display: inline; }.datagrid table tfoot li a { text-decoration: none; display: inline-block;  padding: 2px 8px; margin: 1px;color: #FFFFFF;border: 1px solid #006699;-webkit-border-radius: 3px; -moz-border-radius: 3px; border-radius: 3px; background:-webkit-gradient( linear, left top, left bottom, color-stop(0.05, #006699), color-stop(1, #00557F) );background:-moz-linear-gradient( center top, #006699 5%, #00557F 100% );filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#006699', endColorstr='#00557F');background-color:#006699; }.datagrid table tfoot ul.active, .datagrid table tfoot ul a:hover { text-decoration: none;border-color: #006699; color: #FFFFFF; background: none; background-color:#00557F;}div.dhtmlx_window_active, div.dhx_modal_cover_dv { position: fixed !important; }");
    myFile.write("</style>");
    myFile.write('<body>\n')
    
    myFile.write('<h2>')
    myFile.write(link)
    myFile.write('</h2>')
    
    myFile.write('<div class=\'datagrid\'><table>\n')
    myFile.write('<thead><tr><th>Model</th><th>Details</th><th>PL</th><th>Winner</th></tr></thead>\n')
    myFile.write('<tfoot><tr><td colspan="4"><div id="paging"><ul><li><a href=\'\#\'><span>Previous</span></a></li><li><a href="#" class="active"><span>1</span></a></li><li><a href="#"><span>2</span></a></li><li><a href="#"><span>3</span></a></li><li><a href="#"><span>4</span></a></li><li><a href="#"><span>5</span></a></li><li><a href="#"><span>Next</span></a></li></ul></div></tr></tfoot>\n')
    
    myFile.write('<tbody>\n') 
    
    profit = '<h2>Total Profit:1220.79</h2>';
    
    for item in thelist:
    
        with open(item) as f:
            
            lines_list = f.readlines()
                    
            for file_line in lines_list:
            
                if ('Total Profit' in file_line):
                    profit = re.findall(r'[-+]?\d+', file_line)
                    print(profit[1])
                    if (float(profit[1]) > 0) : 
                        status = 'Winner'
                    else :
                        status  = 'Loser'
      
        if (timestr in item ):
            myFile.write('<tr><td>\n')
            myFile.write(item[42:48].replace('/','').replace('_','').replace('1',''))
            myFile.write('</td>\n')
        
            myFile.write('<td>\n')
            myFile.write('<a href=./output/RightEdge/'+item[37:]+'>'+item[42:]+'</a>')
            myFile.write('</td>\n')
            
            myFile.write('<td  align="right">\n')
            myFile.write(profit[1])
            myFile.write('</td>\n')
            
            myFile.write('<td  align="right">\n')
            myFile.write(status)
            myFile.write('</td></tr>\n')
       
    myFile.write('</tbody>\n')      
    myFile.write('</table>\n')
    myFile.write('</div>\n')
    myFile.write('</body>\n')
    myFile.write('</html>\n')
      
    myFile.close()
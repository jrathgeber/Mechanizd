# -*- coding: utf-8 -*-
import glob
import re
import time

def fileReading(location, location1, link):

    timestr = time.strftime("%d%m%y")
    
    thelist = glob.glob(location)
    myFile = open(location1 ,'w')
    start = 2000
    
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
    myFile.write('<thead><tr><th>Model</th><th>Summary</th><th>Chart</th><th>Trades</th><th>OpenPositions</th><th>PnL</th><th>Log</th><th>Return</th><th>Winner</th></tr></thead>\n')
    myFile.write('<tfoot><tr><td colspan="10"><div id="paging"><ul><li><a href=\'\#\'><span>Previous</span></a></li><li><a href="#" class="active"><span>1</span></a></li><li><a href="#"><span>2</span></a></li><li><a href="#"><span>3</span></a></li><li><a href="#"><span>4</span></a></li><li><a href="#"><span>5</span></a></li><li><a href="#"><span>Next</span></a></li></ul></div></tr></tfoot>\n')
    
    myFile.write('<tbody>\n') 
    
    profit = 'Last Update:  03.04. 04:47 UTC (00:47 Local)<br>System State:  9473 +0 -14 /\\\\<br><p>';
    
    for item in thelist:
        print(item)
        if ('Z7' in item ):
            start = 1000
        else :
            start = 2000
            
        with open(item) as f:
            
            lines_list = f.readlines()
                    
            for file_line in lines_list:
            
                if ('Annual return ' in file_line):
                    profit = re.findall(r'[-+]?\d+', file_line)
                    print(profit[:])
                    if (float(profit[0]) > 0) : 
                        status = 'Winner'
                    else :
                        status  = 'Loser'
      
        if (timestr in item ):
            myFile.write('<tr><td>\n')
            myFile.write(item[38:42].replace('/','').replace('_',''))
            myFile.write('</td>\n')
        
            #myFile.write('<td>\n')
            #myFile.write('<a href=./'+item[20:]+'>'+item[38:]+'</a>')
            #myFile.write('</td>\n')

            myFile.write('<td>\n')
            myFile.write('<a href=./'+item[20:42]+'_'+timestr+'.txt>'+item[38:42]+'_'+ timestr +'.txt</a>')
            myFile.write('</td>\n')

            myFile.write('<td>\n')
            myFile.write('<a href=./'+item[20:42]+'_'+timestr+'.png>'+item[38:42]+'_'+ timestr +'.png</a>')
            myFile.write('</td>\n')
            
            myFile.write('<td>\n')
            myFile.write('<a href=./'+item[20:42]+'_'+timestr+'_testtrades.csv>'+item[38:42]+'_'+ timestr +'_testtrades.csv</a>')
            myFile.write('</td>\n')

            myFile.write('<td>\n')
            myFile.write('<a href=./'+item[20:42]+'_'+timestr+'.htm>'+item[38:42]+'_'+ timestr +'.htm</a>')
            myFile.write('</td>\n')
  
            myFile.write('<td>\n')
            myFile.write('<a href=./'+item[20:42]+'_'+timestr+'_test.log>'+item[38:42]+'_'+ timestr +'_test.log</a>')
            myFile.write('</td>\n')

            myFile.write('<td>\n')
            myFile.write('<a href=./'+item[20:42]+'_'+timestr+'_pnl.csv>'+item[38:42]+'_'+ timestr +'_pnl.csv</a>')
            myFile.write('</td>\n')
          
            myFile.write('<td  align="right">\n')
            myFile.write(str(profit[0])+'%')
            #myFile.write(str(float(profit[12])-start))
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



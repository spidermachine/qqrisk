import requests
import datetime
import dbi
text = requests.get("http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?cb=jQuery1124048101533078167114_1540388704225&type=CT&token=4f1862fc3b5e77c150a2b985b12db0fd&sty=FCOL&js=(%7Bdata%3A%5B(x)%5D%2CrecordsFiltered%3A(tot)%7D)&cmd=C.OP.SO.510050.SH&st=(ChangePercent)&sr=-1&p=1&ps=200&_=1540388704242").text
start = text.find('[')
end = text.find(']')

result = text[start+1:end].split('","')
dbi.insertTableStr('root', 'geuzkp012140', 'stock', 'qqrisk', result)

fo = open('50etfqqrisk' + datetime.datetime.now().strftime('%y%m%d_%H%M%S'), "w")
fo.write(text[start+1:end].replace('","', '\n').replace('"',''))
fo.close()
#!/usr/bin/python
#  -*- coding: UTF-8 -*-
import requests
import dbi
text = requests.get("http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=CT&sty=OCORA&st=(ChangePercent)&sr=-1&p=1&ps=500&token=44c9d251add88e27b65ed86506f6e5da&js=var%20WkYWzRHb={pages:(pc),data:[(x)]}&cmd=C.OP.SO.510050.SH&rt=51346303").text
start = text.find('[')
end = text.find(']')
PASSWD = 'zxcASDqwe123!@#'
S = 'istock'
result = text[start+1:end].split('","')
dbi.insertTableStr(S, PASSWD, S, 'qqrisk', result)

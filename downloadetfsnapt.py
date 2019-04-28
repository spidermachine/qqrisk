#!/usr/bin/python
#  -*- coding: UTF-8 -*-
import dbi
import sinaqq

PASSWD = 'zxcASDqwe123!@#'
S = 'istock'

codes = dbi.selectCodes(S, PASSWD, S)
data = sinaqq.get_50etf_price()
dbi.insertTableEtfSnapt(S, PASSWD, S, data)
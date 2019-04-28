#!/usr/bin/python
#  -*- coding: UTF-8 -*-
import dbi
import sinaqq

PASSWD = 'zxcASDqwe123!@#'
S = 'istock'

codes = dbi.selectCodes(S, PASSWD, S)
data = sinaqq.get_op_greek_alphabet_batch(codes)
dbi.insertTableAlpha(S, PASSWD, S, data)
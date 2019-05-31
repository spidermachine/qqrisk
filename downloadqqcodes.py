#!/usr/bin/python
#  -*- coding: UTF-8 -*-
import dbi
import sinaqq

dates = sinaqq.get_op_dates()
for opt_date in dates:
    expired_date = sinaqq.get_op_expire_day(opt_date)
    up_codes, down_codes = sinaqq.get_op_codes(opt_date)
    dbi.insertTableCodes('istock', 'zxcASDqwe123!@#', 'istock',  up_codes + down_codes, expired_date)

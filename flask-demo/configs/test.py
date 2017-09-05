#!/usr/bin/env python
import  ConfigParser

def getconfig(filenaame,section=''):
	cf = ConfigParser.ConfigParser()
	cf.read(filenaame)
	cf_items = dict(cf.items(section)) if cf.has_section(section) else {}

	return cf_items 

if __name__ == '__main__':
	conf = getconfig('test.conf','web')
	print conf
	print conf['port']
	print conf.get('paths','/data/test')

#!/bin/python
# -*- coding: utf-8 -*-

import os, zipfile

def translateUnicode(s):
	u = s.decode('utf-8')
	if len(u) == len(s):
		return s
	ret = u''
	for ch in u:
		ascii = ord(ch)
		if ascii > 0x7f:
			ret += hex(ascii).replace('0x', '\\u')
		else:
			ret += ch
	return ret.encode('utf-8')

def processPropertiesFile(path):
	f = open(path, 'r')
	assert f
	ret = ''
	for line in f.readlines():
		ret += translateUnicode(line) + '\n'
	f.close()
	return ret

def processFile(zip, path_in_zip, path_in_os):
	name, ext = os.path.splitext(path_in_os)
	if ext == '.properties':
		zip.writestr(path_in_zip, processPropertiesFile(path_in_os))
	else:
		zip.write(path_in_os, path_in_zip)

def processDir(zip, parent_path_in_zip, path_in_fs):
	for filename in os.listdir(path_in_fs):
		if os.path.isdir(path_in_fs + '/' + filename):
			processDir(zip, parent_path_in_zip + filename + '/', path_in_fs + '/' + filename)
		else:
			name, ext = os.path.splitext(filename)
			processFile(zip, parent_path_in_zip + name + '_zh_CN' + ext, path_in_fs + '/' + filename)

def main():
	if not os.path.exists('out'):
		os.mkdir('out')
	zip = zipfile.ZipFile('out/resources_zh_CN.jar', 'w', zipfile.ZIP_STORED)
	assert zip
	processDir(zip, '', 'resources')
	zip.close()

if __name__ == "__main__":
	main()

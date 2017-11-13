#! /usr/bin/env python3

import sys

def main(ldata, pdata, rdata, tdata, gwid):
	print('ldata: {}'.format(ldata))
	print('pdata: {}'.format(pdata))
	print('rdata: {}'.format(rdata))
	print('tdata: {}'.format(tdata))
	print('gwid: {}'.format(gwid))

if __name__ == '__main__':
	main(*sys.argv)

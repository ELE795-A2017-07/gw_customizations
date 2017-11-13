#! /usr/bin/env python3

import sys, os

HOST = 'hexadecimal'
PORT = '1884'
TOPIC = 'dioo-test'

def main(ldata, pdata, rdata, tdata, gwid):
	print("****TEST.PY****")
	print('ldata: {}'.format(ldata))
	print('pdata: {}'.format(pdata))
	print('rdata: {}'.format(rdata))
	print('tdata: {}'.format(tdata))
	print('gwid: {}'.format(gwid))

	MSG = ldata
	os.system('mosquitto_pub -h {} -p {} -t {} -m {}'.format(HOST, PORT, TOPIC, MSG))
	print("****END TEST.PY****")

if __name__ == '__main__':
	NB_MAIN_ARGS = 5
	sys.argv.extend(['' for x in range(max(0, (1 + NB_MAIN_ARGS) - len(sys.argv)))])
	main(*sys.argv[1:])

from argparse import ArgumentParser
from config   import config

def main():
	parser = ArgumentParser()
	args   = parser.parse_args()
	conf   = config()

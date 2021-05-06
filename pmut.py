import ast
import argparse
import sys
from copy import deepcopy

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Mutation Testing Tool.')
	parser.add_argument('-a', '--action', choices=["mutate", "execute"], required=True)
	parser.add_argument('-s', '--source', type=str, required=True)
	parser.add_argument('-m', '--mutants', type=str, required=False)
	parser.add_argument('-k', '--kill', type=str)

	args = parser.parse_args()
	if args.action == "execute" and not args.kill:
		parser.error("Mutant execution action requires -k/--kill")
	

	

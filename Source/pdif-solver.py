#!/usr/bin/env python
# -*- coding: utf-8 -*-

import graph as g
import args

# Retorna os nós fontes, os nós que são alcançado por ele
def getsrcwithwe_achieved(graph):
	size = graph.getsize() # Tamanho do dígrafo
	wesrc = graph.wesrc() # Nós fontes
	tra = graph.transitivity() # Transitividade do dígrafo

	x = 0 # Posição do nó
	for we in wesrc: # Percorre todos os nós fontes
		for y in range(size): # Um for do tamanho do dígrafo
			if tra[we['node']][y]: # Verifica se possui uma relação
				wesrc[x]['we_achieved'].append(y) # Coloca no conjunto de nós alcançado
				wesrc[x]['we_achieved_len'] += 1
		x += 1

	return wesrc

def unionlen(we1, we2):
	return  len(list(set(we1 + we2)))

def random_solution(graph, n_porce):
	pass

def greedy_solution(graph, n_porce):
	"""
		Retorna o tamanho do conjunto de nós alcançado
	"""
	def getwe_achievedlen(we): 
		return we['we_achieved_len']

	# Lista de todos os nós fontes já ordenado em ordem decrescente
	wesrc = sorted(getsrcwithwe_achieved(graph), key=getwe_achievedlen, reverse=True)

	listweSolution, listwe = [], []

	listwe = listwe + wesrc[0]['we_achieved']
	listweSolution.append(wesrc[0])

	if wesrc[0]['we_achieved_len'] >= n_porce:
		print(f'Melhor resultado encontrado\n {listweSolution}')
	else:
		for we in wesrc[1::]:
			l = unionlen(listwe, we['we_achieved']) 
			if l > len(listwe):
				listwe = listwe + we['we_achieved']
				listweSolution.append(we)
				if l >= n_porce:
					break
		print(f'Melhor resultado encontrado\n {listweSolution}')

def main():
	arguments = args.get()

	graph = g.Graph()
	graph.load(arguments.input)

	n_porce = int((graph.getsize() * arguments.percentage) / 100)

	if (arguments.method.lower() == 'g'): 
		greedy_solution(graph, n_porce)
	else:
		random_solution(graph, n_porce)

if __name__ == '__main__':
	main()

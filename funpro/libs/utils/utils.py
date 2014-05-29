# -*- encoding: utf-8 -*-
"""Utils."""
ACT_REF = [1,5,9,13,17,21,25,29,33,37,41]
SEN_INT = [2,6,10,14,18,22,26,30,34,38,42]
VIS_VRB = [3,7,11,15,19,23,27,31,35,39,43]
SEC_GLO = [4,8,12,16,20,24,28,32,36,40,44]

RULE = [11,9,7,5,3,1,-1,-3,-5,-7,-9,-11]

def check_answers(array, request, values):
	count_a = 0
	count_b = 0
	for item in array:
		option = request.POST.get(str(item))
		if option == 'a':
			count_a += 1
		elif option == 'b':
			count_b += 1
	
	if (count_a - count_b) > 0:
		return values[0]
	else:
		return values[1]
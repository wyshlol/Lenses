from error_calc import Rules
import math


if __name__ == '__main__':
	print('-------------- LENSES LAB --------------\n')
	# 1/f = 1/p + 1/i

### PART 1 ### --------------------------------------------------------------------------------
	print('-- PART 1 ------------------------------')
	# p ~ inf, find f
	# Arrow object at ~4f, ~2f, ~1.5f
	# δf: calculate one time for whole lab
	# f = (p * i) / (p + i) , Use Rule 4

	# 1.
	print(' 1.1:')
	# Object Distance
	p_1 = math.inf
	# Image Distance
	i = 0.15

	# Focal Length
	f_1 = 1 / ((1 / p_1) + (1 / i))
	print(f'  Focal Length: {f_1:20f} m') # 0.15

	# 2.
	print('\n 1.2:')
	# @ 4f
	# Object Distance
	p = 0.30
	# Image Distance
	i = 0.30

	# Focal Length
	f = 1 / ((1 / p) + (1 / i))
	print(f'  Focal Length at 4f: {f:14f} m') # 0.15

	# @ 2f
	# Object Distance
	p = 0.29
	# Image Distance
	i = 0.285

	# Focal Length
	f = 1 / ((1 / p) + (1 / i))
	print(f'  Focal Length at 2f: {f:14f} m') # 0.144

	# @ 1.5f
	# Object Distance
	p = 0.225
	# Image Distance
	i = 0.38

	# Focal Length
	f = 1 / ((1 / p) + (1 / i))
	print(f'  Focal Length at 1.5f: {f:12f} m') # 0.141

	print('----------------------------------------\n')
#----------------------------------------------------------------------------------------------


### PART 2 ### --------------------------------------------------------------------------------
	print('-- PART 2 ------------------------------')
	# 1.
	print(' 2.1:')
	# First Focal Length
	f_1 = f_1
	# Image Distance Combined
	i_c = 0.325
	# Focal Length Combined
	f_c = 1 / ((1 / p_1) + (1 / i_c))
	print(f'  Focal Length Combined: {f_c:11f} m') # 0.325

	# Focal Length Average
	f_2 = 1 / ((1 / f_c) - (1 / f_1))
	print(f'  Focal Length Average: {f_2:12f} m') # -0.279

	# 2.
	print('\n 2.2:')
	p_1 = 0.60
	f_1 = f_1
	i_1 = 1 / ((1 / f_1) - (1 / p_1))
	p_2 = -(i_1 - 0.08)
	i_2 = 0.22
	f_div = 1 / ((1 / p_2) + (1 / i_2))
	print(f'  Focal Length Divergent: {f_div:10f} m') # -0.264

	i_2 = 0.393
	p_2 = -(i_1 - 0.045)
	f_2 = 1 / ((1 / p_2) + (1 / i_2))
	print(f'  Focal Length 2: {f_2:18f} m') # -0.256

	print('----------------------------------------\n')
#----------------------------------------------------------------------------------------------


### ERROR ANALYSIS ### ------------------------------------------------------------------------
	print('------------ ERROR ANALYSIS ------------')

	# Object Distance
	p_errana = 0.30
	delta_p = 0.01
	# Image Distance
	i_errana = 0.30
	delta_i = 0.01

	err_denominator = Rules.rule3([delta_p, delta_i])

	f_errana = (p_errana * i_errana) / (p_errana + i_errana)

	delta_f = Rules.rule4([p_errana, i_errana, (p_errana + i_errana)], [delta_p, delta_i, err_denominator], [1, 1, -1], f_errana)
	print(f'  δf: {delta_f:30f} m') # 0.00791

	print('----------------------------------------\n')
#----------------------------------------------------------------------------------------------
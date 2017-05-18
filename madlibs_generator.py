# -*- coding: UTF-8 -*-

parts_of_speech  = ["PLACE", "PERSON", "PLURALNOUN", "NOUN"]

test_string = """This is PLACE, no NOUN named PERSON, We have so many PLURALNOUN around here."""

def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None

# def replace1(string1, sub_string1, r_string):#原始字符串，要被替换的字符串，替换的字符串
# 	''' 自定义的replace方法 '''
# 	len_sub = len(sub_string1)
# 	len_str = len(string1)
# 	new_string = []
# 	index = 0
# 	while index < len_str:
# 		my_sub = string1[index : index + len_sub]
# 		if my_sub == sub_string1:
# 			new_string.append(r_string)
# 			index += len_sub
# 		else:
# 			new_string.append(string1[index])
# 			index += 1
# 	new_string = ''.join(new_string)
# 	return new_string

# def rep_string(string1, string2):
# 	index = 0
# 	rep_str = []
# 	while index < len(string2):
# 		my_sub = string2[index:index + len(string1)]
# 		if my_sub == string1:
# 			rep_str.append('corgi')
# 			index += len(string1)
# 		else:
# 			rep_str.append(string2[index])
# 			index += 1
# 	replaced_string = ''.join(rep_str)
# 	return replaced_string

# def play_game(ml_string, parts_of_speech):    
#     replaced = []
#     # your code here
#     ml_word = ml_string.split()
#     for wd in ml_word:
#     	replacement = word_in_pos(wd, parts_of_speech)
#     	if replacement != None:
#     		wd = replace1(wd, replacement, 'corgi')
#     		replaced.append(wd)
#         else:
#             replaced.append(wd)
#     result = ' '.join(replaced)
#     return result
    
def play_game(ml_string, parts_of_speech):
	replaced = []
	ml_word = ml_string.split()
	for wd in ml_word:
		replacement = word_in_pos(wd, parts_of_speech)
		if replacement != None:
			user_input = raw_input('Type in a:' + replacement + ' ')
			wd = wd.replace(replacement, user_input)
			replaced.append(wd)
		else:
			replaced.append(wd)
	replaced = ' '.join(replaced)
	return replaced

print play_game(test_string, parts_of_speech)

raw_input('Press Enter to exit...')
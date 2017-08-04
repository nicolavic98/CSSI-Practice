arr = [2, 6, 3, 8, 4]
arr[0]

emoji_dic = {
':)' : 'happy',
':(' : 'sad',
'<3' : 'heart',
"lol" : 'laughing out loud',
'._.' : 'unimpressed',
}

user_emoji = raw_input("Identify an emoji ")
if user_emoji in emoji_dic:
    print "The definition is  " + emoji_dic[user_emoji]
else:
    print "Learn yo emojis"


#     #13 will print like command, 14/15 will print True/False
# print emoji_dic['lol']
# print '<3' in emoji_dic
# print ':P' in emoji_dic

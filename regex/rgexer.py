import re #import library re

# define or declare the pattern variables with the regex
pattern = '\S+\@\S+'
pattern2 = '\w+h\wn'
# define text
text = """Hey Mr. Bezos,

I hope its okay I message you in this unsecure email program. Sry about that!
Here the list of extremely confidential clients and close coworkers of you who actually visited Epsteins island. Oh boy how I hope no random Python Students extract this sensitive list with some kind of regular expressions! 

therealjeffbezos@bossnet.com
markzuckerbergtheman@facebookormetaidkmail.com
donaldtothatrump@getthatcapitolmail.com
2pacaintdeadandnowchillinonwrongislands@mail.com

Kind regards,
Tanisha"""
# define regex findall method in new variables 
emails = re.findall(pattern, text)
students_of = re.findall(pattern2, text)
#print found matches 
print('\n', 'Here are the emails: ', '\n')
for email in emails:
    print(email)

print('\n', 'Students of ', students_of, 'figured them out', '\n')
# python snake
print(
    '''
       ---_ ......._-_--.
      (|\ /      / /| \  
      /  /     .'  -=-'   `.
     /  /    .'             )
   _/  /   .'        _.)   /
  / o   o        _.-' /  .'
  \          _.-'    / .'*|
   \______.-'//    .'.' \*|
    \|  \ | //   .'.' _ |*|
     `   \|//  .'.'_ _ _|*|
      .  .// .'.' | _ _ \*|
      \`-|\_/ /    \ _ _ \*
       `/'\__/      \ _ _ \*
      /^|            \ _ _ \*
     '  `             \ _ _ \      ASH (+VK)
                       \_
                       '''
)
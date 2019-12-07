from fuzzywuzzy import fuzz
from jellyfish import soundex
from jellyfish import metaphone

    
text_file = open("name.txt", "r")
lines = text_file.read().split('\n')
#print (lines)
text_file.close()
list_size = len(lines)
print (str(list_size))
#print(lines)

for i in range(list_size):
    sub_lines=lines[i].split(',')
    #print(sub_lines[0],sub_lines[1])
    Ratio = fuzz.ratio(sub_lines[1].lower(),sub_lines[2].lower())
    Partial_Ratio = fuzz.partial_ratio(sub_lines[1].lower(),sub_lines[2].lower())
    Token_Sort_Ratio = fuzz.token_sort_ratio(sub_lines[1].lower(),sub_lines[2].lower())
    #print(sub_lines[0],",",sub_lines[1],",",Ratio)
    #print(sub_lines[0],",",sub_lines[1],",",Partial_Ratio)
    #print(sub_lines[0],sub_lines[1],Token_Sort_Ratio)
    x=max( Ratio,Partial_Ratio,Token_Sort_Ratio)
  
    if (60 <= x <= 90 and soundex(sub_lines[1]) == soundex(
                sub_lines[2])) or x > 90:
        print(sub_lines[0],",",sub_lines[1],",",sub_lines[2].lower(),",",x,",","match")
    else:
        print(sub_lines[0],",",sub_lines[1],",",sub_lines[2].lower(),",",x,",","not_match")
    
    

         
 



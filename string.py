str1 = "this is a string."
str2 = 'this is a string.'
str3 = """this is a string."""
print(str3)

str1 = "this is a string.\n we are creating a string in python."
print(str1)

str1 = "this is a string. \t we are creating a string in python."
print(str1)

str1 = "Mahima"
str2 = "Rawat"
print(str1 + " " + str2) #"" using this we can give space between two string
print(len(str1))
len2 = len(str2)
print(len2)

#indexing
str7 = "Mahima Rawat"
ch = str7[0]
print(ch)
#slicing
print(str7[1:4]) #last indexing is never counted
print(str7[7:13])
print(str7[7:len(str7)])
print(str7[:4]) #[0:4]
print(str7[5:]) #[5:len(str7)]
print(str7[-3:-1]) 

#string Functions
str = "i am a doctor."
print(str.endswith("or.")) #return true if string ends with substr
print(str.capitalize()) #capitalizes 1st char
str = str.capitalize() 
print(str.replace("doctor", "coder")) #replaces all occurrences of old to new
print(str.find("am")) #return 1st index of 1st occurrer
print(str.count("am")) #counts the occurrence of substr

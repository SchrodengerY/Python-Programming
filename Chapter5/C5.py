# 文件和异常

# Read It
# 读取文件

print("Open and close the file.")
text_file = open("read_it.txt","r")
text_file.close()

print("\nReading characters from the file.")
text_file = open("read_it.txt","r")
print(text_file.read(1))
print(text_file.read(5))
text_file.close()

print("\nReading the entire file at once.")
text_file = open("read_it.txt","r")
whole_thing = text_file.read()
print(whole_thing)
text_file.close()

print("\nReading characters from a line.")
text_file = open("read_it.txt","r")
print(text_file.readline(1))
print(text_file.readline(5))
text_file.close()

print("\nReading one line at a time.")
text_file = open("read_it.txt","r")
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())
text_file.close()

print("\nReading the entire file into a list.")
text_file = open("read_it.txt","r")
lines = text_file.readlines()
print(lines)
print(len(lines))
for line in lines:
	print(line)
text_file.close()

print("\nLooping through the file, line by line.")
text_file = open("read_it.txt","r")
for line in text_file:
	print(line)
text_file.close()

# 写入文本

print("Creating a text file with the write() method.")
text_file = open("write_it.txt","w")

text_file.write("Line 3\n")
text_file.write("This is Line 2\n")
text_file.write("That makes this Line 1\n")

text_file.close()
text_file = open("write_it.txt","r")
print("\nReading the newly created file.")
print(text_file.read())
text_file.close()

# pickle it
# 演示数据的序列化处理（pickle和shelve）

import pickle, shelve

print("Pickling lists.")
variety = ["sweet", "hot", "dill"]
shape = ["whole", "spear", "chip"]
brand = ["Claussen", "Heinz", "Vlassic"]
print(variety)
print(shape)
print(brand)

f = open("pickles1.dat", "wb")
pickle.dump(variety,f)
pickle.dump(shape,f)
pickle.dump(brand,f)
f.close()

print("\nUnpickling lists.")
f = open("pickles1.dat","rb")
variety = pickle.load(f)
shape = pickle.load(f)
brand = pickle.load(f)

print(variety)
print(shape)
print(brand)
f.close()

# 使用shelf
print("\nShelving lists.")
s = shelve.open("pickle2.dat")
s["variety"] = ["sweet","hot","dill"]
s["shape"] = ["whole","spear","chip"]
s["brand"] = ["Claussen","Heinz","Vlassic"]

s.sync()

print("\nRetrieving lists from a shelved file:")
print("brand -",s["brand"])
print("shape -",s["shape"])
print("variety -",s["variety"])
s.close()
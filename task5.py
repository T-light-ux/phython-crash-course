 # A list that contains at list on string,one int and one float
solution_to_question=["Lil wayne",49,0.5]
print(solution_to_question)

#Grab 2 from nested list
nested_list=[1,1,[1,2]]
print(nested_list[2][1])

#result of lst.pop()
lst=[0,1,2]
print(lst.pop())
 
# Yes

#result of lst[1:]
lst=["a","b","c"]
print(lst[1:])

"""list is used to hold or store sequence data type and dict is a key to value pair"""

#dictionary with three key-value pair
items_value={"rice":2000,"ball":200,"beans":2500}
print(items_value)

#dictionary where all key are strings and all values are integers
height_of_boys={"Drake":176,"Ronaldo":188,"Pogba":190,"Noyad":189}
print(height_of_boys)

# what is the output of d["k1"][1]
d={"k1":[1,2,3]}
print(d["k1"][1])

# N0,They are mutable

#grab hello
d={"simple_key":"hello"}
print(d["simple_key"])

#grab hello
my_dict={"k1":{"k2":"hello"}}
print(my_dict["k1"]["k2"])

#grab hello
my_dict={"k1":[{"nest_key":["this is deep",["hello"]]}]}
print(my_dict["k1"][0]["nest_key"][1][0])

#grab hello
my_dict={"k1":[1,2,{"k2":["this is tricky",{"tough":[1,2,["hello"]]}]}]}
print(my_dict["k1"][2]["k2"][1]["tough"][2])
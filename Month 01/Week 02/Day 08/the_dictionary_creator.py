
# def build_dict_from_list(list):
#     new_dict=allocate_memory()
    
#     for item in list:
#         hash_value=calculate_hash(item)
#         slot=find_empty_slot(hash_value)
#         new_dict[slot]=item
#     return new_dict
import random, time

list=[random.randint(1,100) for i in range(1000)]


start =time.time()

dict={}

for i in range(len(list)):
    for j in list:
        dict[i]=j
        
print(dict)
end=time.time()
time_taken=end-start

print(f"time taken to make dictionary {time_taken}")


start =time.time()

found=-5 in dict

end=time.time()
time_taken=end-start

print(f"time taken to find item in dictionary {time_taken}")
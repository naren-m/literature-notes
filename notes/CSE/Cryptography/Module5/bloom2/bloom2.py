#Import libraries
import hashlib
import hmac

def set_bit(value, bit):
#    print("Flag 2", value, value | (1<<bit))
    return value | (1<<bit)

def get_bit(value, bit):
    return value & ~(1<<bit)

def membership(filter, b1, b2):
    f1=bin(filter)[8-b1]
    f2=bin(filter)[8-b2]
    if (f1=='0') or (f2=='0'): 
        return False
    return True

def calculate_bits(data):
    my_hmac1 = hmac.new(data, b'1234', hashlib.md5)
    my_hmac2 = hmac.new(data, b'1234', hashlib.sha1)

    v1=int.from_bytes(
        my_hmac1.digest(), 'big')
    b1=v1%8

    v2=int.from_bytes(
        my_hmac2.digest(), 'big')
    b2=v2%8

#    print("calculate", b1, b2)
    return b1, b2

def add_to_bloom(filter, b1, b2):
    filter=set_bit(filter, b1)
    filter=set_bit(filter, b2)
    return filter


filter=0

data = b'bob young'
print("data", data)

b1, b2=calculate_bits(data)
filter=add_to_bloom(filter, b1, b2)
#print("Flag 12", filter, b1, b2)
result=membership(filter, b1, b2)
print(result)

data=b'data'
print(data)

b1, b2=calculate_bits(data)
result=membership(filter, b1, b2)
print(result)
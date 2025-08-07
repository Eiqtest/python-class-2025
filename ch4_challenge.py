_data = (1,7,3,7,5,3,2,1,4,5,6,7,8,9)
#sorting the tuple without sorting function
# Remove duplicates
# Convert to list
_data =list(set(_data)) # use "set" to detect duplicates
n = len(_data)
for i in range(n):
    for j in range(0, n-i-1):
        if _data[j] > _data[j+1]:
            _data[j], _data[j+1] = _data[j+1], _data[j]

print( _data)
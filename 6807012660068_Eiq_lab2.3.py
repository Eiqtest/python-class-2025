# Name = input("Enter your name: ")
# Surname = input("Enter your surname: ")
# Gender = input ('Enter your gender:')    
# Age = int(input("Enter your age: "))
# formatted_string = f"Name: {Name}, Surname: {Surname}, Gender: {Gender}, Age: {Age}"
# print(formatted_string)

# str = "perfectly#perfected#perfect#perfection"
# Cell = str.split("#")
# print(Cell)

dna = "CACGCCTAGTTTCAGACATAACCCTGGACATAGCCATAACGGAGTCAG"

print('Size of the dna string:', len(dna))


pos_tgga = dna.find("TGGA")
print('Position of "TGGA":', pos_tgga if pos_tgga != -1 else "Not found")


substr = "TCAG"
positions_tcag = []
start = 0
while True:
    idx = dna.find(substr, start)
    if idx == -1:
        break
    positions_tcag.append(idx)
    start = idx + 1
print('Positions of "TCAG":', positions_tcag if positions_tcag else "Not found")


pos_gacg = dna.find("GACG")
print('Position of "GACG":', pos_gacg if pos_gacg != -1 else "Not found")

# 4. Slice the dna string into substrings of 3 characters and print them all in one line
codons = [dna[i:i+3] for i in range(0, len(dna), 3)]
print(' '.join(codons))


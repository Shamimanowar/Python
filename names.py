import csv



header = ["Supplier Name", "CR Number", "UN Number"]

# Calculate the maximum length for the first column
max_len = max(len(item[0]) for item in li)

with open('supplier_with_un_but_unverified.txt', 'w', encoding='UTF-8') as file:
    file.write(f"{header[0].ljust(max_len + 4)}{header[1].ljust(max_len + 4)}{header[-1]}")
    file.write(f"\n{"-" * 100} \n\n\n")
    for item in li:
        file.write(f"{item[0].ljust(max_len + 4)}{item[1].ljust(max_len + 4)}{item[-1]}")
        file.write("\n\n")


    file.write(f"\n\n\n\n There are total {len(li)} entries in the file")
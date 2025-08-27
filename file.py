
with open(r"C:\Users\USER\Desktop\PERIS DOCUMENTS⁮\File handling\FileStruct\input.txt", "r") as file:
    content = file.read()
modified_content = content.upper()

with open("output3.txt", "w") as file:
    file.write(modified_content)

try:
    file_name = input("Enter file name:")
    with open (file_name, "r"):
        content = file.read()
        
        print(content)

except  FileNotFoundError:
    print("File not found")

finally:
    print("File operations closed!")
    file.close()
    print(content)



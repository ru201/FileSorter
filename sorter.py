import sys
import os

direc = input("Enter directory path: ")

if os.path.isdir(direc): 
    directory = os.fsencode(direc)
else:
    sys.stderr.write("Directory does not exist\n")
    exit()

print("Enter file types (e.g. .docx, .pdf): ")
for f_type in sys.stdin:
    if f_type != '\n':
        f_type = f_type.strip() #Remove new line char

        if not os.path.isdir(f_type):
            os.mkdir(os.path.join(f_type))

        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            if filename.endswith(f_type):
                os.rename(os.path.join(os.path.abspath(direc), filename), os.path.join(os.path.abspath(f_type), filename))
    else:
        break

"""import sys
import os

if (len(sys.argv) < 3):
    print("Usage: {directory_name} {file_type1} {file_type2} ...")

direc = os.fsencode(sys.argv[1])

for f_type in sys.argv[2:]:
    if not os.path.isdir(f_type):
        os.mkdir(os.path.join(f_type))

    for file in os.listdir(direc):
        filename = os.fsdecode(file)
        if filename.endswith(f_type):
            os.rename(os.path.join(os.path.abspath(sys.argv[1]), filename), os.path.join(os.path.abspath(f_type), filename))"""
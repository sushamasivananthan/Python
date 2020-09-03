filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
newfilenames=[]
# using as many lines of code as your chosen method requires.
for x in range(len(filenames)):
    old_name = filenames[x]
    if old_name.endswith(".hpp"):
      new_name = old_name.replace('.hpp','.h')
    else:
      new_name = old_name;
    newfilenames.append((new_name))



print(newfilenames) 

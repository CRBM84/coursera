def read_file(file_name):
   
    with open(file_name) as file:
        file_content = file.read()
        print(file_content)
        return file_content
    
    raise NotImplementedError()

def read_file_into_list(file_name):
   
    list_of_lines = []

    with open(file_name, "r") as file:
        for line in file:
            list_of_lines.append(line)
        return list_of_lines

    raise NotImplementedError()

def write_first_line_to_file(file_contents, output_filename):
    
    
    first_line = file_contents.split("\n")[0]

    with open(output_filename, "w") as file:
        file.write(first_line)
 


def read_even_numbered_lines(file_name):
    
    with open(file_name, "r") as file:
        even_lines = []
        counter = 0 
        for lines in file.readlines():
            if counter % 2 !=0:
                even_lines.append(lines)
            counter +=1
    return even_lines
    
    raise NotImplementedError()

def read_file_in_reverse(file_name):
      
    with open(file_name) as file:
        content = file.readlines()
        new_list = content[::-1]

    print(new_list)
    return new_list
    
    raise NotImplementedError()

'''
Here are some sample commands to help you run/test your implementations.
Feel free to uncomment/modify/add to them as you wish.
'''
def main():
    file_contents = read_file("sampletext.txt")
    # print(read_file_into_list("sampletext.txt"))
    # write_first_line_to_file(file_contents, "online.txt")
    # print(read_even_numbered_lines("sampletext.txt"))
    # print(read_file_in_reverse("sampletext.txt"))

if __name__ == "__main__":
    main()
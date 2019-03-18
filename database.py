def dollar(value_str):
    try:
        result = float(value_str)
        return result
    except Exception as e:
        if value_str[:1] == '$':
            try:
                result = float(value_str[1:])
            except Exception as e:
                print('NNNNOOOO', e)
        else:
            raise ValueError('could not convert string to float:', value_str)
            
    

def process_file(filename):
    # declare header variable
    headerValues = []
    # declare db variable
    database = []

    # read file in
    try:
        with open(filename) as f:
            for index, line in enumerate(f):
                if index == 0:
                    # parse header
                    headerValues = line.strip().split('\t')
                else:
                    list = []
                    currentLine = line.strip().split("\t")
                    if len(currentLine) != len(headerValues):
                        raise Exception('Line', index, 'Not enough or too many values in line')
                    # loop throw lines and attempt to parse lines
                    for index, value in enumerate(currentLine):
                        expectedType = headerValues[index]
                        if expectedType == "#":
                            list.append(int(value))
                        elif expectedType == "$":
                            list.append(dollar(value))
                        else:
                            list.append(value)
                    # append
                    database.append(list)
    except FileNotFoundError as e:
        print(e, '(╯°□°)╯︵ ┻━┻')
    except Exception as e:
        print(e, '(╯°□°)╯︵ ┻━┻')
    
    return database
    
    
    
   


# def dollar(value_str):

def main():
    # filename = Ask user for file name
    filename = input("Enter the name of a tsv file: ")
    # call process_file(filename)
    print(process_file(filename))


main()
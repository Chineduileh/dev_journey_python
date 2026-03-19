from typing import Union
import os
def safe_calculator(a: Union[int,float], b: Union[int,float], operation: str)-> Union[int,float]:
    """
    Perform a calculation on two numbers safely.

    Args:
        a: First number.
        b: Second number.
        operation: One of 'add', 'subtract', 'multiply', 'divide'.

    Returns:
        The result of the operation.
    """
   
   
    try:
        if operation=="add":
            result=a+b
        elif operation=="subtract":
            result=a-b
        elif operation=="multiply":
            result=a*b
        elif operation=="divide":
            result=a/b
        else:
            raise ValueError()
    except ZeroDivisionError:
            print("Division by 0 not supported")
            return None
    except TypeError:
            print("Invalid Input(s)")
            return None
    except ValueError:
            print(f'Invalid operation {operation}')
    else:
        return result

result1=safe_calculator(3,5,"add")
result2=safe_calculator(7,0,"divide")
result3=safe_calculator("Hello",0,"Heavy")
print(result1,result2,result3)


class EmptyFileError(Exception):
    def __init__(self, filename):
        self.filename=filename
        super().__init__(f'file in {filename} is empty')

def read_and_summarise(filename: str)->dict:
    """Read and summarise given file

        Args
            filename: path to file

        Returns
            A dictionary containing the relevant stats for the file.
    
    """
    line_count=0
    word_count=0
    character_count=0
    try:
        with open(filename,"r") as f:
            for line in f:
                line_count+=1
                word_count+=len(line.split())
                character_count+=len(line)
        if line_count==0:
            raise EmptyFileError(filename)
    except EmptyFileError as e:
        print(e)
        return None

    except FileNotFoundError:
        print(f'files does not exist')
        return None
    else:
        return {"filename":filename, 
        "lines": line_count,
         "words": word_count,
         "Characters":character_count}
    finally:
        print("Operation Complete")         
    

summarise_file1= read_and_summarise("new.txt")
summarise_file2= read_and_summarise("Empty.txt")
summarise_file3= read_and_summarise("new3.txt")


print(summarise_file1)
print(summarise_file2)
print(summarise_file3)

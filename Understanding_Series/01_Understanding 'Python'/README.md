# 01_Understanding  ${\color{aqua} 'Python'}$ 
##### Objective :- The ground plan is to understand and learn ${\color{aqua} Python}$ in a simpler manner.
### 01. Introduction :
* Programming is a way to instruct computer to perform various tasks.
* Why Python?
* Simple to use
* Easy to understand 
* Free  and  open source 
* Works on Windows/ MAC / Linux OS

### 02. Basic Data :
* No semicolon neeeded in Python.
* Module :
  - file having code
  - written by someone else
  - can be imported,used in our program
  - can be **Built-in** (pre installed in python)
  - can be **External** (need to be installed in python)
  - <code style="color : black">pip install *module_name</code>* : command for installing module
  - <code style="color : black">pip install *playsound </code>*  :  command for playing sound in python using module
* REPL : 
  - **read evaluate print loop**
  - works in terminal
  - can't save program in REPL 
  - used for faster evaluation
 
 ### 03. Key Info :
 * Comments :
   - lines of code 
   - want to write 
   - but don't want to execute
   - written for better understanding 
   - <code style="color : black"># single line comments</code> : used for single line comments
   - <code style="color : black">'''multi-line comments'''</code> : used for multi-line comments
   - ''' more than 1 line string ''' is called string literal 
             
 * Datatypes :
    1.  integers 
    2.  floating point
    3.  string
    4.  boolean 
    5.  None 
   - variable is name to any memory location
   - variable names are case sensitive i.e. 'ABC' and 'abc' are 2 different variables
   - in python, string can be in single or double or triple quotes
   - in python, datatype is identified by itself 
   - in python, datatype name can start with letters, underscore but not with digits & space 
   - in python, variable names are case sensitive i.e. 'ABC' and 'abc' are 2 different variables
   - in python,   <code style="color : black"> type(variable_name) </code>  is a built-in function which returns datatype of any variable
   - same rule applies for identifer (identifier is class or function or variable name )
  
  * Operators :
     1.  Arithmetic : +,-,*,/,**,//
     2.  Assignment : =,+=,-=,*=,/=
     3.  Comparison : ==,>=,<=,!=,>,<
     4.  Logical    : and , or , not
     
   * Typecasting :
     - Process of changing 1 datatype to another
     - **type(variable)** : syntax
  
  * Strings :
     - enclosed in single,double,triple quotes
     - string concantentation 
     - slicing ->  using index from 0 to n (where n is not considered , n-1 is endpoint)
     - slicing ->  -ve index used from -1 to -n (when last character is to be obtained & length is unknown)
     - slicing ->  slicing done using skip value  ( [l : m : n])
     - len(string) -> returns length of string
     - string.endswith(' ') -> returns with True or False if it ends with same character
     - string.count(' ') -> returns count of any letter or word
     - string.find(' ')  -> returns index of any letter or word and if not present then -1
     - string.replace(old,new) -> replacing of words
     
*   Escape Characters :
     - \t -> tab space
     - \n -> new line
 *  List :
     - to contain any & all kinds of datatypes
     - ordered and mutable kind 
     - has indexing just like strings
     - values can be changed in list using indexing 
     - list.sort()    -> sorting in ascending order, can't be stored in different variable
     - list.reverse() -> prints backward
     - list.append()  -> adds at end of list
     - list.insert(index,value)-> inserts value at that index
     - list.pop(index)    -> removes value at index and returns value
     - list.remove(value) -> removes value directly 
     - Example -> listNew = [ "name", 45, 175.36]   
  
  ### NOTE : 
        1.  By default in python , number is in float datatype.
        2.  <code style="color : black">os.listdir()</code> : used for listing all files in directory
        3.  Typecasting does not gurantee to change but it will try to change the dataype 
        4.  input is always as a string in Python
        5.  If  different datatype is required then it can be done using Typecasting 
        6. space is also counted as 1 character in a string 
        7. string.find returns only 1st occurence of that letter or word
        8. Python docs -> all in 1 info about Python
        
     
  
**:)**

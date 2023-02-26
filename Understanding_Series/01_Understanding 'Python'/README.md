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
     - ordered , mutable , indexed kind 
     - has indexing just like strings
     - values can be changed in list using indexing 
     - list.sort()    -> sorting in ascending order, can't be stored in different variable
     - list.reverse() -> prints backward
     - list.append()  -> adds at end of list
     - list.insert(index,value)-> inserts value at that index
     - list.pop(index)    -> removes value at index and returns value
     - list.remove(value) -> removes value directly 
     - Example -> listNew = [ "name", 45, 175.36]   
   
  *  Tuple :
     - stored in circular brackets ()
     - ordered , immutable , indexed kind 
     - has indexing just like strings
     - values can't be changed in tuple using indexing 
     - tuple.count(value) -> returns count of times that value is present
     - tuple.index(value) -> returns 1st occurence index of that value
     - Example -> tupleNew = (45,)  
    
 *  Dictionary :
     - to store data in key-value pair
     - un-ordered , mutable , indexed kind 
     - prints value corresponding to the key
     - key & value can be any dataype , even list,string or new dictionary 
     - keys are always UNIQUE and can't be duplicated
     - dict.keys    -> prints all keys
     - dict.value   -> prints all values
     - dict.items   -> prints all keys & values
     - dict.update  -> value added at end of dict , if key exists then key also updated
     - dict.get(key)-> returns value , if not exists then returns NONE
     - dictNew = {  "color" : "lilac" } 
  
  *  Sets :
     - stored in curly brackets {}
     - un-ordered , mutable , un-indexed kind 
     - items are unique and non-repetitve
     - repetitive items won't be displayed  
     - tuple can be added but list & dict can't be added in set
     - set.add(value)     -> value added in set, if same statement repeated, value added only once
     - len(set)           -> prints length of set
     - set.remove(value)  -> prints removed value
     - set.pop()          -> prints random removed value
     - set.clear          -> clears the set
     - set.union(set)     -> returns union of sets
     - set.intersection(set)-> returns intersection of sets
   
   
 *  if-elif-else() :
     - identation important
     - when many if-else statements, compiler stops as soon as 1st True condition recieved 
     - further statements won't be executed
     - when all statements are needed to be executed then use only 'if' for all conditions
     - else statement is optional in Python
    
  * while(condition) :
     - identation important
     - if condition true then goes inside loop else not
     - used for infinite loop
     
 * for item in list or tuple :
     - identation important
     - used for iterating through any data collection or datatype sequence
* range :
     - function for generating sequence of numbers from 0 to n-1
     - range(start,stop,step-size) : syntax

* Function :
     - identation important
     - to do a specific task
     - def func_name (parameter) :
          - body 
          - return
     
  ### NOTE : 
        1.  By default in python , number is in float datatype.
        2.  <code style="color : black">os.listdir()</code> : used for listing all files in directory
        3.  Typecasting does not gurantee to change but it will try to change the dataype 
        4.  input is always as a string in Python
        5.  If  different datatype is required then it can be done using Typecasting 
        6. space is also counted as 1 character in a string 
        7. string.find returns only 1st occurence of that letter or word
        8. Python docs -> all in 1 info about Python
        9. sum function sums all values in list
       10. Tuple always needs comma even if only 1 element is present
       11. Set treats float & int of number as same but string of that number different
       12. pass -> keyword or Null statement for doing nothing
       13. is -> keyword works like equal to
       14. in -> keyword works like finding inside any data collection
       15. while & for loop with else can be used when 'break' is not used and loop is executed totally
       16. 'break'     -> keyword to exit loop
       17. 'continue'  -> keyword to skip a specific value or step
       18. Recursion function is one which calls itself and can be used in any direct algorithm or formula
  
**:)**

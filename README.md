# Micro benchmark on Python

Iteration on data structures.


## Usage :

```
python3 src/main.py -h
Usage
python3 main.py -<opt>
Types:
	-o for object
	-i for integer
	-f for float
	-s for string
	The only types possible for an array are :
	integers, float and string
	(this last will be converted to python unicode character)
Data Structures:
	-L for list
	-S for set
	-D for dict
	-A for array
Loop type:
	-l for the for loop with range
	-r for the for loop without range
	-c for comprehension
	-w for while loop

```


## Example

```
python3 src/main.py -Lif 1000000
```

**In construction**
# Micro benchmarks on python data structures

## Usage

```
usage: main.py [-h] [--size SIZE] --data-structure {list,set,dict} --type
               {integer,float,str} --action
               {iteration-for,iteration-while,iteration-for-range,iteration-comp,insertion-beginning,insertion-middle,insertion-end,random-access,random-removal,clean,pop,extend,insertion,insertion-comp,iteration-key,iteration-kv,not-in,iteration,random-in}
               [--extra EXTRA]

optional arguments:
  -h, --help            show this help message and exit
  --size SIZE
  --data-structure {list,set,dict}
                        data strcture to do the test on
  --type {integer,float,str}
                        data type
  --action {iteration-for,iteration-while,iteration-for-range,iteration-comp,insertion-beginning,insertion-middle,insertion-end,random-access,random-removal,clean,pop,extend,insertion,insertion-comp,iteration-key,iteration-kv,not-in,iteration,random-in}
                        action to perform on the data structure
  --extra EXTRA         number of extra element to add in the data structure
```
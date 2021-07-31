runaway.py is a very simple tool that you provide input from stdin and an argument called label and you get on stdout a comma seperated output with a current generated timestamp, the label and the stdin converted to base64.

Example:

$ echo "this is a test" | ./runaway.py -l test
2021-07-31 10:20:13.115,test,dGhpcyBpcyBhIHRlc3QK

Uses:

* convert files / input from stdin to base64 strings and add timestamp and a label
* convert many files / input from stdin to base64 strings and add timestamp and a label and append them to a single file
* using the timestamp and the label you can with some clever grep|cut|uniq tricks to get results very easy if a file remains unchanged 

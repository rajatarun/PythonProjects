import urllib as a
b = a.urlopen("https://s3-us-west-2.amazonaws.com/tarunproject/3students.txt")
c = b.read();
d = c.replace("\r"," ").replace("\n"," ").strip().split(".")

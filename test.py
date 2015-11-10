import urllib as a
b = a.urlopen("https://s3-us-west-2.amazonaws.com/tarunproject/acne.txt");
c = b.read();
c = c.replace("\r","").replace("\r","");
import re
d = re.findall("[a-zA-Z0-9!? ,'""*;:-]*[^.\\r\\n,]",c);
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer();
tf = tfidf.fit_transform(d)
mat = cosine_similarity(tf,tf)
import numpy
m = numpy.array(mat).tolist();
sum = [];
for i in m:
    sum1 = 0;
	for j in i:
        sum1 = sum1+j;
	sum.append(sum1);
val = [];
for i in range(len(sum)):
	if(sum[i] >= round(numpy.median(sum))):
		val.append(i);
di = [];
for i in val:
	di.append(d[i]);




	








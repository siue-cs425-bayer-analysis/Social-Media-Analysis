 
Here is what I have so far:
migrations will need to be updated I have not done that yet cause I dont want to debug it 
tonight if there is a problem. I plan on making the migrations and updating the database tomorrow
afternoon and commit necessary changes by late evening on 9/12/2019.
	
Taylor if you could look over the migrations schema, I was not 100% on them, but went off what I remembered.  

My understanding of Django is that views should manipulate the content of the page and the template 
should hold the "html" that the content goes into, am I getting that right?

To run the project currently I am using:
	python 3.6.8
	nltk==3.4.5
	python-twitter==3.5
	vader-sentiment==3.2.1.1
	Django==2.2.4
	
	sentiment analysis also needs nltk_data downloaded 
	python3 shell
	>>>> import nltk
	>>>> nltk.download('punkt')


We need to talk about using Docker and a virtualenv to hold this togther.



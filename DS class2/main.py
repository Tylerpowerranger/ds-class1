#Exploring the pandas library
import pandas as pd
shoe_data={'brand name':['Nike','Adidas','Skechcers','Puma'],'model':['Phantom','F50','Razor','Future'],'origin':[' Phil Knight/Bill Bowerman','Adi Dassler','Robert Greenberg/ Michael Greenberg','Rudolf Dassler']}
df=pd.DataFrame(shoe_data)
print(df)
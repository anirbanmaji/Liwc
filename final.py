import mysql.connector
conn=mysql.connector.connect(user='root',password='',host='localhost',database='personality')
cursor=conn.cursor()
cursor.execute("Select * from traits")
data=cursor.fetchall()

traits=["Openness","Conscientiousness","Extraversion","Agreeableness","Neuroticism"]

frequency = [0,0,0,0,0]
dataset = open("trial.txt").read().splitlines()

for item1 in dataset:
    for item2 in data:
        try:
            frequency[item2.index(item1)]+=1
        except:
            pass

total = 0
percentage = [0,0,3,0,0]
for number in frequency:
    total+=number
percentage[0]=100*frequency[0]/total
percentage[1]=100*frequency[1]/total
percentage[2]=100*frequency[2]/total
percentage[3]=100*frequency[3]/total
percentage[4]=100*frequency[4]/total
print(traits,percentage)
   
conn.commit()
cursor.close()
conn.close

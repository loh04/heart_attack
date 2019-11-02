import pickle 
pickle_in=open('model.pickle','rb')
model= pickle.load(pickle_in)

age=int(input("enter the age of the person : "))
sex=input("enter the sex of the person as either 'male' or 'female' : ")
tres=int(input("enter the resting blood pressure of the person : "))
cp=int(input("enter the chest pain type of the person on a scale of 0 to 3 : "))
chol=int(input("enter the cholestrol of the person : "))

age_scaled=(age-54.366337)/9.082101
tres_scaled=(tres-131.623762)/17.538143
chol_scaled=(chol-246.264026)/51.830751
sex_0=0
sex_1=0
chol_0=0
chol_1=0
chol_2=0
chol_3=0
if sex== 'male':
	sex_1=1
else:
	sex_0=1

if chol==0:
	chol_0=1

elif chol==1:
	chol_1=1

elif chol==2:
	chol_2=1

else:
	chol_3=1

pred=model.predict([[age_scaled,tres_scaled,chol_scaled,sex_0,sex_1,chol_0,chol_1,chol_2,chol_3]])
print(pred) 


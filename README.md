# Heart Attack Prediction using Machine Learning 

Heart attacks are a major problem in and around the world. We have desinged an application that checks whether the person has the probablitly of having a heart attack by measuring various quantities such as age, gender, blood pressure, cholestrol levels.  

We had taken a dataset from Kaggle which is rated 9/10 and was very much suitable to use for this purpose. 


The problem we intend to solve with this is reducing the costs of checkups for the commo man as he/she isn't able to afford these types of checkups.

The data was cleaned and made ready for training. The model was initially trained using Logistic Regression and various other algorithms which were imported from the "sklearn" library. 

In the end we decied to use Random Forest Regression as it lead to the increase in overall output of the model. About 85%.

This trained model was then saved as a pickle file so as to be used later on.

The frontend was done using Django, where the user can enter his respected details and the output screen was generated based on the output ie. whether the user has the chance of getting a heart stroke or not.


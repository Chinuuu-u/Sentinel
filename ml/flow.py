import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("C:\\Users\\Chirag\\Desktop\\Sentinal\\tmp.csv")
dff = pd.read_csv("C:\\Users\\Chirag\\Desktop\\Sentinal\\data.csv")
new_flow = dff[[
   "Packets",
    "Duration",
    "Packet/sec",
    "Byte/sec",
    "Average Packet Size"
]]
X = df[[
    "Packets",
    "Duration",
    "Packet/sec",
    "Byte/sec",
    "Average Packet Size"
]]

Y = df["LABEL"]

X_train ,X_test ,Y_train ,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

model = RandomForestClassifier(n_estimators=100,random_state=42)

model.fit(X_train,Y_train)

predictions = model.predict(X_test)
prediction2 = model.predict(new_flow)

acc = accuracy_score(Y_test,predictions)

print("Accuracy:", predictions)
print("Accuracy:", prediction2)
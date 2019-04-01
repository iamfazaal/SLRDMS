from sklearn import tree
import xlrd

# Give the location of the file 
loc = ("C:\\Users\\nisal\\Documents\\Python\\demo.xlsx") 

# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 

# For row 0 and column 0 
#print(sheet.cell_value(0, 0))
#print(sheet.cell_value(1, 0))
          
# For row 0 and column 1 
#print(sheet.cell_value(1, 1))

w1 = sheet.cell_value(1, 0)
t1 = sheet.cell_value(1, 1)
t1 = 0

print (w1)
print (t1)

w2 = sheet.cell_value(2, 0)
t2 = sheet.cell_value(2, 1)
t2 = 0

print (w2)
print (t2)

w3 = sheet.cell_value(3, 0)
t3 = sheet.cell_value(3, 1)
t3 = 1

print (w3)
print (t3)

w4 = sheet.cell_value(4, 0)
t4 = sheet.cell_value(4, 1)
t4 = 1

print (w4)
print (t4)



#features = [[140,"smooth"], [130,"smooth"], [150,"Bumpy"],[170,"Bumpy"]]
#features = [[140,1], [130,1], [150,0],[170,0]]
features = [[w3,t3], [w4,t4], [w1,t1], [w2,w2]]

labels = ["apple","apple","orange","orange"]
#labels = [0,0,1,1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

print (clf.predict([[150,0]]))
#print (clf.predict([[150,1]]))

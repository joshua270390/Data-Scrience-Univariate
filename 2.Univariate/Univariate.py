class Univariate():
    def quanQual(dataset):
        quan = []
        qual = []

        for colName in dataset.columns:
            if dataset[colName].dtype == 'O':
                #print("qual:",colName)
                qual.append(colName)
            else:
                #print('quan:',colName)
                quan.append(colName)
        return quan, qual
    
    
    def univariate(quan,dataset):
        descriptive = pd.DataFrame(index=["Mean","Median","Mode","Q1:25%","Q2:50%",
                                          "Q3:75%","Q4:100%","IQR","1.5Rule","Lesser","Greater","Min","Max",
                                          "Skew","Kurtosis","Var","STD"],columns=quan)
        
        for colname in quan:
            descriptive[colname]["Mean"]=dataset[colname].mean()
            descriptive[colname]["Median"]=dataset[colname].median()
            descriptive[colname]["Mode"]=dataset[colname].mode()[0]
            descriptive[colname]["Q1:25%"]=dataset.describe()[colname]["25%"]
            descriptive[colname]["Q2:50%"]=dataset.describe()[colname]["50%"]
            descriptive[colname]["Q3:75%"]=dataset.describe()[colname]["75%"]
            descriptive[colname]["Q4:100%"]=dataset.describe()[colname]["max"] 
            descriptive[colname]["IQR"]=descriptive[colname]["Q3:75%"]-descriptive[colname]["Q1:25%"]
            descriptive[colname]["1.5Rule"]=1.5*descriptive[colname]["IQR"]
            descriptive[colname]["Lesser"]=descriptive[colname]["Q1:25%"]-descriptive[colname]["1.5Rule"]
            descriptive[colname]["Greater"]=descriptive[colname]["Q3:75%"]+descriptive[colname]["1.5Rule"]
            descriptive[colname]["Min"]=dataset[colname].min()
            descriptive[colname]["Max"]=dataset[colname].max()
            descriptive[colname]["Skew"]=dataset[colname].skew()
            descriptive[colname]["Kurtosis"]=dataset[colname].kurtosis()
            descriptive[colname]["Var"]=dataset[colname].var()
            descriptive[colname]["STD"]=dataset[colname].std()
        return descriptive
    
    
    def frequencyTable(colname, dataset):
        freqTable = pd.DataFrame(columns = ["Unique Value", "Frequency", "Relative Frequency", "CumSum"])
        freqTable["Unique Value"] = dataset[colname].value_counts().index
        freqTable["Frequency"] = dataset[colname].value_counts().values
        freqTable["Relative Frequency"] = freqTable["Frequency"]/103
        freqTable["CumSum"] = freqTable["Relative Frequency"].cumsum()
        return freqTable
    
    
    def columnOutlier(quan):
        descriptive = pd.DataFrame(index=["Mean","Median","Mode","Q1:25%","Q2:50%",
                                          "Q3:75%","Q4:100%","IQR","1.5Rule","Lesser","Greater","Min","Max"],columns=quan)
        lesser_outlier=[]
        greater_outlier=[]

        for colname in quan:
            if (descriptive[colname]["Min"] < descriptive[colname]["Lesser"]):
                #print("Lesser:",colname)
                lesser_outlier.append(colname)
            if (descriptive[colname]["Max"] > descriptive[colname]["Greater"]):
                #print("Lesser:",colname)
                greater_outlier.append(colname)
        return lesser_outlier, greater_outlier
    
    
    def replaceOutlier(lesser_outlier,greater_outlier):
        for colname in lesser_outlier:
            dataset[colname][dataset[colname]<descriptive[colname]["Lesser"]] = descriptive[colname]["Lesser"]
        for colname in greater_outlier:
            dataset[colname][dataset[colname]>descriptive[colname]["Greater"]] = descriptive[colname]["Greater"]
        return dataset
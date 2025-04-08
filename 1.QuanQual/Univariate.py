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
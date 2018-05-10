import pandas as pd
from sklearn.cross_validation import train_test_split

def executarLeitura():
    data = pd.read_csv("/desenvolvimento/marvin/data/diag.csv")
    data = data.drop("id", axis=1)
    data = data.rename(columns={"diagnosis": "label"})
    data['diagnosis_num'] = data.label.map({'B': 0, 'M': 1})
    data = data.drop("label", axis=1)
    train, test = train_test_split(data, test_size=0.3)
    train_x = train[train.columns[0:len(train.columns) -1]]
    train_y = train[train.columns[len(train.columns)-1:len(train.columns)]]

    test_x = test[test.columns[:len(test.columns) - 1]]
    test_y = test[test.columns[len(test.columns) - 1:len(test.columns)]]

    test_x = test_x.stack().str.replace(',', '.').unstack()

    print(train_y)

executarLeitura()
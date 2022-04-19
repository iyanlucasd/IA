import pandas as pd
from scipy.io import arff
import weka.core.jvm as jvm
from weka.classifiers import Classifier
from weka.core.converters import Loader

loader = Loader(classname="weka.core.converters.ArffLoader")
jvm.start()

def readDataset():
    data = arff.loadarff('weather.nominal.arff')
    df = pd.DataFrame(data[0])
    df = df.applymap(str)
    df = df.applymap(lambda x: x.split('\'')[1])
    return df

data = loader.load_file("weather.nominal.arff")
print(data)
cls = Classifier(classname="weka.classifiers.trees.J48", options=["-C", "0.3"])
cls.build_classifier(data)



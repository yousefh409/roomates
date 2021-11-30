import pandas as pd
import os
from models import Question

# Call twice to go up one directory
pre = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

def inputFormData(fileName):
    filePath = os.path.join(pre, "input", fileName)
    return pd.read_excel(filePath)
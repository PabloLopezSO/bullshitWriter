import json
import os
import pandas as pd


actualDir:str = os.path.dirname(__file__).replace('\\', '/')
excelFileDir:str = os.path.join(actualDir, 'ciceronData.xlsx').replace('\\', '/')


def jsonExcelData():
    readExcel:pd = pd.read_excel(excelFileDir)
    readJson:pd = readExcel.to_json(orient='records')
    loadedJson:json = json.loads(readJson)
    return loadedJson


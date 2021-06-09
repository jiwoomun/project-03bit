from crime_cctv.models import CctvDTO
from common.services import CommonService
import pandas as pd
import xlwings as xw
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

class CctvService(CommonService):
    dto = CctvDTO()

    # DF 생성하기
    def new_model(self, payload) -> object:
        this = self.dto
        this.context = './data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)


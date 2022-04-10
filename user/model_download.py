from sre_constants import CATEGORY_WORD
from sys import meta_path
from summarizer import Summarizer
import pickle
import os
dir_path = os.path.normpath(os.getcwd() + os.sep + os.pardir)
model_path = os.path.join(dir_path, "mlmodels/sum_bert.pkl")

print('started....')
model = Summarizer()
pickle.dump(model, open(model_path, 'wb'))
print('.....finished')
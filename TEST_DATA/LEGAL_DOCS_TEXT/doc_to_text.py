import textract
import pandas as pd 
# df_names = pd.read_csv('D:\\WORKSPACE\\CB_LIVE_PROJECT\\DOCUMENT_LEGALITY_IDENTIFIER\\TEST_DATA\\legal_file_names.csv')
df_names = pd.read_csv('/mnt/d/WORKSPACE/CB_LIVE_PROJECT/DOCUMENT_LEGALITY_IDENTIFIER/TEST_DATA/legal_file_names.csv')
names = list(df_names['FILE_NAMES'])
for each_name in names[:5]:
    # text = textract.process('D:\\WORKSPACE\\CB_LIVE_PROJECT\\DOCUMENT_LEGALITY_IDENTIFIER\\TEST_DATA\\LEGAL_DOCUMENTS\\' + each_name)
    text = textract.process('/mnt/d/WORKSPACE/CB_LIVE_PROJECT/DOCUMENT_LEGALITY_IDENTIFIER/TEST_DATA/LEGAL_DOCUMENTS/' + each_name)
    with open(each_name + '.txt', mode='w') as text_file:
        text_file.write(str(text))

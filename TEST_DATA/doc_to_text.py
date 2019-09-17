# import textract
# import pandas as pd 
# # df_names = pd.read_csv('D:\\WORKSPACE\\CB_LIVE_PROJECT\\DOCUMENT_LEGALITY_IDENTIFIER\\TEST_DATA\\legal_file_names.csv')
# df_names = pd.read_csv('/mnt/d/WORKSPACE/CB_LIVE_PROJECT/DOCUMENT_LEGALITY_IDENTIFIER/TEST_DATA/legal_file_names.csv')
# names = list(df_names['FILE_NAMES'])
# for each_name in names[:5]:
#     # text = textract.process('D:\\WORKSPACE\\CB_LIVE_PROJECT\\DOCUMENT_LEGALITY_IDENTIFIER\\TEST_DATA\\LEGAL_DOCUMENTS\\' + each_name)
#     text = textract.process('/mnt/d/WORKSPACE/CB_LIVE_PROJECT/DOCUMENT_LEGALITY_IDENTIFIER/TEST_DATA/LEGAL_DOCUMENTS/' + each_name)
#     with open(each_name + '.txt', mode='w') as text_file:
#         text_file.write(str(text))
import os, docx2txt
def get_doc_text(filepath, file):
    if file.endswith('.docx'):
       text = docx2txt.process(file)
       return text
    elif file.endswith('.doc'):
       # converting .doc to .docx
       doc_file = filepath + file
       docx_file = filepath + file + 'x'
       if not os.path.exists(docx_file):
          os.system('antiword ' + doc_file + ' > ' + docx_file)
          with open(docx_file) as f:
             text = f.read()
          os.remove(docx_file) #docx_file was just to read, so deleting
       else:
          # already a file with same name as doc exists having docx extension, 
          # which means it is a different file, so we cant read it
          print('Info : file with same name of doc exists having docx extension, so we cant read it')
          text = ''
       return text

# filepath = "D:\\WORKSPACE\\CB_LIVE_PROJECT\\DOCUMENT_LEGALITY_IDENTIFIER\\TEST_DATA\\test_doc_text\\"
filepath = "/mnt/d/WORKSPACE/CB_LIVE_PROJECT/DOCUMENT_LEGALITY_IDENTIFIER/TEST_DATA/LEGAL_DOCUMENTS/"
files = os.listdir(filepath)

for file in files:
   
   text = get_doc_text(filepath, file)
   with open('/mnt/d/WORKSPACE/CB_LIVE_PROJECT/DOCUMENT_LEGALITY_IDENTIFIER/TEST_DATA/LEGAL_DOCS_TEXT/' + file[:-4] + '.txt', mode='w') as text_file:
      text_file.write(text)
   # print(text)
   
   
# well it's done!!
# let's check for it now..
# seems like 672 of those were empty, now I'll have to delete them :<

# Code stub taken from https://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory

import os
import zipfile


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

base_dir = os.getcwd()
# I hate doing this but you need to actually change your working directory to the folder you need
# otherwise the zip will include subfolders for all folders between your current working directory
# and the directory you want to zip


os.chdir('layers/spacy')
zipf = zipfile.ZipFile('spacy_lambda.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir('python/', zipf)
zipf.close()

# os.chdir('./')
# zipf = zipfile.ZipFile('spacy_model_sm_lambda.zip', 'w', zipfile.ZIP_DEFLATED)
# zipdir('en_core_web_sm-1.2.0/', zipf)
# zipf.close()

# os.chdir('./')
# zipf = zipfile.ZipFile('spacy_model_lg_lambda.zip', 'w', zipfile.ZIP_DEFLATED)
# zipdir('en_core_web_lg/', zipf)
# zipf.close()


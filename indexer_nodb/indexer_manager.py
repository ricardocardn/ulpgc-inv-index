import os
import shutil

class indexer_manager:

    def create_directory():
        if not os.path.exists("datamart"):
            os.mkdir("datamart")
    
    def delete_directory():
        if os.path.exists("datamart"):
            shutil.rmtree("datamart")


        
from setuptools import setup, find_packages
REQUIREMENT_FILE_NAME='requirements.txt'
REMOVE_PACKAGE="_e ."
def get_requirements_list(requirement_file_name=REQUIREMENT_FILE_NAME) ->list:
    try:
        with open(requirement_file_name) as requirement_file:
            requirement_list=[requirement.replace("\n","r")for requirement in requirement_file]
            requirement_list.remove(REMOVE_PACKAGE)
        return requirement_list
    except Exception as e:
        raise e
    
setup(
    name="lstm-text-classification",
    version="0.0.1",
    description="LSTM based text classification project. Deployed at Digital Ocean",
    author="Kulakirti Chakma",
    package=find_packages(),
    install_requires=get_requirements_list()
)
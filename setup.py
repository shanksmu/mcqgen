from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='Shashank Bhardwaj',
    author_email='shanksmu@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2","langchain-community"],
    packages=find_packages()
)
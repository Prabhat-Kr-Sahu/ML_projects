from setuptools import find_packages,setup

def get_requirements(file_path ):
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if("-e ." in requirements):
            requirements.remove("-e .")
    return requirements


setup(
    name= "ML Project",
    version= "0.0.1",
    author = "Prabhat Kumar Sahu",
    author_email= "prabhatkr.sahu190@gmail.com",
    packages= find_packages(),
    install_requires= get_requirements("requirements.txt")
    
)
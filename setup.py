from setuptools import setup, find_packages
import os

os.chdir( os.path.dirname(__file__) )

VERSION = '0.1' 
DESCRIPTION = 'Utility for formatting ci/cd console output'
LONG_DESCRIPTION = 'Utility for producing beautiful formatted console output when running continous integration tests'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="cilogger", 
        version=VERSION,
        author="Helge Langen",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'testing', 'ci/cd', 'jenkins'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Intended Audience :: System Administrators",
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent",
            "Topic :: Software Development",
            "Topic :: Software Development :: Build Tools",
            "Topic :: Software Development :: Testing",
            "Topic :: System :: Logging",
            "Topic :: System :: Monitoring",
            "Topic :: Utilities",
        ]
)
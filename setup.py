
from setuptools import find_packages, setup
from typing import List


HYPHEN_E_DOT = '-e.'
def get_requirements(file_path: str)->List[str]:
    with open(file_path) as f:
        requirements = f.read().splitlines()
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
name='ML_project',
version='0.1.0',
author='Ankit',
author_email='ankit.sneh.ug22@gmail.com',
packages = find_packages(),
install_requires=get_requirements('requirements.txt')
)
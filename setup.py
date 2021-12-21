from setuptools import setup

setup(
    name='Asset Allocation',
    version='0.0.12',
    author='Yusuf Ismaila',
    author_email='iay2000@hw.ac.uk',
    packages=['cvxportfolio',
              'cvxportfolio.tests'],
    package_dir={'cvxportfolio': 'cvxportfolio'},
    package_data={'cvxportfolio': [
        'tests/returns.csv', 'tests/sigmas.csv', 'tests/volumes.csv']},
    url='http://github.com/cvxgrp/cvxportfolio/',
    license='Apache',
    zip_safe=False,
    description='Building Multiperiod Portfolio Optimization.',
    install_requires=["pandas",
                      "numpy",
                      "matplotlib",
                      "cvxpy>=1.0.6"],
    use_2to3=True,
)

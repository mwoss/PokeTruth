from setuptools import setup

setup(name='poke_truth_measurer',
      version='1.0',
      description='Truth validation program of pokemon world',
      url='https://github.com/AGHPythonCourse2017/zad3-mwoss',
      author='Mateusz Wos',
      author_email='wos.mateusz16@gmail.com',
      license='MIT',
      packages=['truthmeas', 'test', 'data'],
      install_requires=['requests', 'simplejson', 'pytest'])

from setuptools import setup, find_packages

description = 'Set of casual python utilities'
long_description = '{}, written standing on shoulders of giants'.format(description)

requirements = []
setup(
   name='pyjama',
   version='0.1',
   description=description,
   license="MIT",
   long_description=long_description,
   author='Karthik Rajasekaran',
   author_email='krajasek@gmail.com',
   url="http://github.com/krajasek/pyjama",
   install_requires=requirements,
   packages=find_packages(exclude=('pyjama.tests',)),
   python_requires='>=2.7'
)
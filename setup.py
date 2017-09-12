from distutils.core import setup

setup(name='qdict',
      version='1.1',
      description='A tool for query iterable of objects',
      author='Ohrlando',
      author_email='pythonicos@outlook.com',
      url='https://github.com/Pythonicos/qdict',
      py_modules=['qdict/__init__', 'qdict/exceptions', 'qdict/__version__'],
      license='MIT',
      classifiers=['Programming Language :: Python :: 3'],
      keywords='query list dictionary search tool',
      python_requires='>=3')

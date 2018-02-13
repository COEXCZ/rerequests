from distutils.core import setup

setup(
    name='rerequests',
    version='1.0.0b0',
    packages=['rerequests'],
    url='https://github.com/COEXCZ/rerequests',
    license='Apache License 2.0',
    author='Jan Češpivo',
    author_email='',
    description='Wrapper around requests library with automatic retry ability',
    install_requires=['requests']
)

from setuptools import find_packages, setup

setup(
    name='py_utils_linyz',
    version='0.1',
    description='Les petites utils cree par linyz',
    url='http://github.com/leegggg/py_utils_linyz',
    author='LIN Yizhou',
    author_email='yizhou.lin@outlook.com',
    license='Apache 2.0',
    packages=find_packages(),
    packages=['py_utils_linyz'],
    zip_safe=False,
    install_requires=[
        "requests",
        "bs4",
        "selenium",
        "clint",
        "htmlmin",
        "lxml"
    ]
)

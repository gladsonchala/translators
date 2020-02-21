# coding=utf-8
# author=UlionTse

from setuptools import setup,find_packages


PACKAGE = "translators"
NAME = "translators"
DESCRIPTION = "Free & Easy translators for Python, such as Google, Alibaba, Tencent, NetEase(Youdao), etc."
AUTHOR = "UlionTse"
AUTHOR_EMAIL = "shinalone@outlook.com"
URL = "https://github.com/uliontse/translators"
#VERSION = __import__(PACKAGE).__version__
VERSION = "4.3.0"

with open('README.md','r',encoding='utf-8') as file:
    long_description = file.read()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="MIT",
    url=URL,
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        # "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8"
    ],
    keywords=['translators','translate','translator','fanyi','Google','Baidu','Alibaba','Tencent','Youdao','NetEase'],
    install_requires=[
        'requests>=2.22.0',
        'PyExecJS>=1.5.1',
        'lxml>=4.5.0'
    ],
    zip_safe=False,
)

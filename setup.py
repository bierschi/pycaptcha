from setuptools import setup

from pycaptcha import __version__, __author__, __email__, __license__

install_requires = [
    "",
]

with open("README.md", encoding='utf-8') as f:
    readme = f.read()

with open("CHANGELOG.rst") as f:
    changelog = f.read()

setup(
    name="pycaptcha",
    version=__version__,
    description="solves different kind of captcha",
    long_description=readme + "\n\n" + changelog,
    long_description_content_type='text/markdown',
    license=__license__,
    author=__author__,
    author_email=__email__,
    url="https://github.com/bierschi/pycaptcha",
    packages=["pycaptcha"],
    install_requires=install_requires,
    keywords=["python", "captcha", "recaptcha", "bots", "captchasolver"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet :: Name Service (DNS)",
    ],
    entry_points={
        "console_scripts": [
            "pycaptcha = pycaptcha.pycaptcha:main",
        ],
    },
    zip_safe=True,
)

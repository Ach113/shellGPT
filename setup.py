from setuptools import setup

setup(
    name='shellGPT',
    version='0.1.0',
    description='chatGPT interface inside terminal',
    url='https://github.com/Ach113/shellGPT',
    author='Archil Beridze',
    author_email='archil.beridze@sjsu.edu',
    license='MIT',
    install_requires=['openai~=0.27.2'],

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: User Interfaces'
    ],
    packages=['src'],
    entry_points={
        'console_scripts': ['shellgpt=src.main:main'],
    },
)

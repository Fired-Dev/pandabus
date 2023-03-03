from setuptools import Extension, dist, find_packages, setup


"""try:
    from pypandoc import convert_text
    long_description = convert_text(open("README.md",encoding="utf8").read(),'rst',format="md")
except ModuleNotFoundError:
    long_description = "A Simple Event Bus."""
long_description=open("README.md",encoding="utf8").read()

setup(
    name='pandabus',
    version="0.0.5",
    description='A Simple Event Bus.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='eventbus',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Natural Language :: Chinese (Simplified)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries',
    ],
    url='https://github.com/fired-dev/simpleeventbus',
    author='Colin Xu',
    author_email='colinxu2020@gmail.com',
    python_requires='>=3',
)
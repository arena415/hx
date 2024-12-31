from setuptools import setup, find_packages

# Read the contents of README.md for the long description
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='hx',  # Replace with your desired package name
    version='1.0.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A helper package to retrieve code snippets based on keywords.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/helpx_package',  # Replace with your repository URL
    packages=find_packages(),
    include_package_data=True,  # Include data files specified in MANIFEST.in
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Choose your license
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        # List your package dependencies here
    ],
    entry_points={
        'console_scripts': [
            'helpx=helpx_package.helper:main',
        ],
    },
)


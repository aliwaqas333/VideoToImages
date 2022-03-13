import setuptools
import os

def read(rel_path):
    base_path = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(base_path, rel_path), 'r') as f:
        return f.read()

setuptools.setup(
    name="videoToImages",
    version="2.1.1",
    author="Ali Waqas",
    author_email="engrr.ali.waqas@gmail.com",
    description="A easy to use, video to images converter",
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    url="https://github.com/aliwaqas333/VideoToImages",
    project_urls={
        "Bug Tracker": "https://github.com/aliwaqas333/VideoToImages/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'videoToImages = videoToImages.videoToImages:main',
        ],
    },
)

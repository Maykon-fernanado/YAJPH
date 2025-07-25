from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="yajph",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="The Anti-Black-Box Engine - GitHub's First Explainable Decision Framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/yajph",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "PyYAML>=6.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "black>=22.0",
            "isort>=5.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "yajph=yajph:main",
        ],
    },
    keywords="ai explainable decisions yaml json transparency audit",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/yajph/issues",
        "Source": "https://github.com/yourusername/yajph",
        "Documentation": "https://yajph.readthedocs.io/",
    },
)

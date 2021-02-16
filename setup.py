import pathlib
from setuptools import setup, find_packages


base_packages = [
    "scikit-learn>=0.24.0",
    "altair>=4.0.1",
    "matplotlib>=3.2.0",
    "fasttext>=0.9.1",
    "bpemb>=0.3.0",
    "gensim>=3.8.3",
]

spacy_packages =[
    "spacy>=3.0.1",
    "spacy-lookups-data>=0.3.2",
]

s2v_packages = ["sense2vec>=1.0.2"] + spacy_packages

tf_packages = [
    "tensorflow>=2.3.0",
    "tensorflow-text>=2.3.0",
    "tensorflow-hub>=0.8.0",
]

transformers_dep = [
    "transformers>=3.0.0",
]

sentence_tfm_dep = ["sentence-transformers>=0.3.8"]

docs_packages = [
    "mkdocs==1.1",
    "mkdocs-material==4.6.3",
    "mkdocstrings==0.8.0",
    "jupyterlab>=0.35.4",
    "nbstripout>=0.3.7",
    "nbval>=0.9.5",
]

test_packages = [
    "torch>=1.6.0",
    "flake8>=3.6.0",
    "pytest>=4.0.2",
    "black>=19.3b0",
    "pytest-cov>=2.6.1",
    "nbval>=0.9.5",
    "pre-commit>=2.2.0",
]

extra_deps = (
    tf_packages
    + transformers_dep
    + s2v_packages
    + sentence_tfm_dep
)
dev_packages = docs_packages + test_packages + extra_deps


setup(
    name="whatlies",
    version="0.5.10",
    author="Vincent D. Warmerdam",
    packages=find_packages(exclude=["notebooks", "docs"]),
    description="Tools to help uncover `whatlies` in word embeddings.",
    long_description=pathlib.Path("readme.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://rasahq.github.io/whatlies/",
    project_urls={
        "Documentation": "https://rasahq.github.io/whatlies/",
        "Source Code": "https://github.com/RasaHQ/whatlies/",
        "Issue Tracker": "https://github.com/RasaHQ/whatlies/issues",
    },
    install_requires=base_packages,
    extras_require={
        "base": base_packages,
        "docs": docs_packages,
        "dev": dev_packages,
        "test": test_packages,
        "tfhub": tf_packages,
        "sense2vec": s2v_packages,
        "spacy": spacy_packages,
        "transformers": transformers_dep,
        "sentence_tfm": sentence_tfm_dep,
        "all": extra_deps,
    },
    classifiers=[
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)

from setuptools import setup, find_packages

setup(
    name="proyecto_ia_amazon_reviews",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pandas",
        "scikit-learn",
        "transformers",
        "fastapi",
        "streamlit"
    ],
)

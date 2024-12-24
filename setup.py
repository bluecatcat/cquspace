from setuptools import setup, find_packages

setup(
    name="bmn",
    version="0.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["Click", "selenium"],
    entry_points="""
        [console_scripts]
        bmn=bmn.scripts.bmn:bmn
    """,
)

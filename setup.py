from setuptools import find_packages, setup

setup(
    name='webapp',
    version='1.0.0',
    description="Flask web application",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask','waitress'
    ],
)

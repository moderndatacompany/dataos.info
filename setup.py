from setuptools import setup, find_packages

VERSION = '1.1'

setup(
    name = "mkdocs-material",
    version = VERSION,
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: JavaScript",
        "Programming Language :: Python",
        "Topic :: Documentation",
        "Topic :: Software Development :: Documentation",
        "Topic :: Text Processing :: Markup :: HTML"
    ],
    packages = find_packages(exclude = ["src"]),
    include_package_data = True,
    install_requires=['mkdocs>=1.1'],
    # entry_points = {
    #     "mkdocs.themes": [
    #         "material = material",
    #     ]
    # },
    zip_safe = False
)
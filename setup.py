from setuptools import setup
setup(
    name = "pycard",
    packages = ["pycard"],
    test_suite = "tests",
    version = "0.1",
    description = "Object interface to vCards.",
    author = "Joris Picot",
    author_email = "joris.picot@aquilenet.fr",
    url = "http://jpilot.fr",
    keywords = ["carddav", "vcard"],
    classifiers = [
        "Development Status :: 1 - Alpha",
        "Environment :: Console",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Communications :: Email :: Address Book",
    ])
 

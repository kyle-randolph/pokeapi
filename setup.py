import setuptools

def readme_text():
    with open('README.md') as f:
        return f.read()

setuptools.setup(
    name="pokeapi",
    version="0.1.0",
    packages=['pokeapi'],
    install_requires=[
        "requests",
    ],
    author="Kyle Randolph",
    author_email="randolphkylea@gmail.com",
    description="""A humble beginning to catalogging all of the Pokemon. This SDK 
    leverages pokeapi. More information about this api may be found here https://pokeapi.co/docs/v2#info""",
    url="https://github.com/kyle-randolph/pokeapi",
)

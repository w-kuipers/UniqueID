import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simpleuid",
    version="2.0.0a0",
    author="Wibo Kuipers",
    author_email="wibokuip@gmail.com",
    description="A simple and intuitive Python package for generating unique IDs written in Rust.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/w-kuipers/simpleuid",
    project_urls={
        "Bug Tracker": "https://github.com/w-kuipers/simpleuid/issues", },
    package_dir={"": "python"},
    packages=setuptools.find_packages(where="python"),
)

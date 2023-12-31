
import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name = "sckinetics",
    version = "1.0",
    author = "author",
    author_email = "author@example.com",
    description = "short package description",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/Lalit-shaktawat/scKINETICS",
    project_urls = {
        "Bug Tracker": "package issues URL",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
 	"Programming Language :: Python :: 3",
    	"Programming Language :: Python :: 3.7",
    	"Programming Language :: Python :: 3.8",
    	"Programming Language :: Python :: 3.9",
    	"Programming Language :: Python :: 3.10",
    	"Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.9"
)

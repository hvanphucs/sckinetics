
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
     install_requires=[
	"os",
	"time",
	"scanpy",
	"pandas",
	"numpy",
	"ceil",
	"njit",
	"norm",
	"sr_matrix",
	"cosine",
	"LabelEncoder",
	"DBSCAN",
	"sklearn",
	"tqdm",
	"contextlib",
	"joblib",
	"check_is_fitted",	
	"csr_matrix",
	"quiver_autoscale",
	"compute_velocity_on_grid",
	"collections",
	"seaborn",
	"matplotlib",
	"sklearn",
	"MOODS",
	"GC",
	"Genome",
	"read_motifs",
	"pandas2ri",
	"rpackages",
	"StrVector",
	"rpy2",
	"mygene",	
	"sparse" ],
	python_requires = ">=3.7"
)

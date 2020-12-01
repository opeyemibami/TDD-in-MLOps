from setuptools import setup, find_packages

setup(name="insurance_classification",
      version="0.1.0",
      description="practise of tdd in mlops",
      author="Opeyemi bamigbade",
      packages=find_packages("src"),
      package_dir={"": "src"},
      author_email="bamigbadeopeyemi@gmail.com",
      install_requires=["jupyter==1.0.0",
                        "pandas==1.0.5",
                        "numpy==1.18.5",
                        "joblib==0.16.0",
                        "pytest==5.4.3",
                        "pathlib",
                        "lightgbm==3.0.0",
                        ],
      )
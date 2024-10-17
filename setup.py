from setuptools import setup, find_packages

setup(
    name="morning_greetings",  # The package name
    version="0.1",
    packages=find_packages(),  # Automatically find all packages in your project
    include_package_data=True,  # Include non-Python files specified in MANIFEST.in (if any)
    description="Simulate sending greeetings to your contacts",
    author="Fredrik Andersen Langsem",
    author_email="s354392@oslomet.no",
    install_requires=[
        # List your project's dependencies here, if any
    ],
    install_requires=[
          'pkgutil',
          'schedule',
          'pandas'
      ],
    entry_points={
        'console_scripts': [
            'morning_greetings=morning_greetings.main:main',  # Points directly to the main function in main.py
        ],
    },
)

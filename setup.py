from setuptools import setup, find_packages

setup(
        name = 'feeed',
        version = '1.0.0',
        description = 'Feature Extraction from Event Data',
        author = 'Andrea Maldonado, Gabriel Tavares',
        author_email = 'andreamalher.works@gmail.com, gabrielmrqstvrs@gmail.com',
        license = 'MIT',
        url='https://github.com/lmu-dbs/feeed.git',
        install_requires=[
            'pandas==2.0.0',
            'tqdm==4.65.0',
            'pm4py==2.7.2',
            'scipy>=1.10.1',
            ],
        packages = ['feeed', 'feeed.utils'],
        classifiers=[
            'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
            'Intended Audience :: Science/Research',      # Define that your audience are developers
            'Topic :: Software Development',
            'License :: OSI Approved :: MIT License',   # Again, pick a license
            'Programming Language :: Python :: 3.9',
    ],
)
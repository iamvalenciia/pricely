from setuptools import setup, find_packages

setup(
    name='prcicely_bot_x',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests>=2.20',
        'numpy',
        'tweepy',
        'python-dotenv'
    ],
    entry_points={
        'console_scripts': [
            'mi_script=mi_proyecto.mi_modulo:mi_funcion',
        ],
    },
    author='Juan Pablo Valencia',
    author_email='alguienop@ejemplo.com',
    license='MIT'
)
from setuptools import setup, find_packages

setup(
    name='Stackoverflow-lite',
    version='1.0.0',
    description='StackOverflow-lite is a platform where people can ask questions and provide answers',
    url='https://github.com/jeffandeko/Stackoverflow-lite',
    author='Jeff Andeko',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Andela kenya',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    keywords='rest restful api flask swagger openapi flask-restplus',

    packages=find_packages(),

    install_requires=['flask-restplus==0.9.2', 'Flask-SQLAlchemy==2.1'],
)

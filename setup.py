from setuptools import setup, find_packages

setup(
    name='dockerflow',
    version='2016.11.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    description="Python tools and helpers for Mozilla's Dockerflow",
    author='Mozilla Foundation',
    author_email='dev-webdev@lists.mozilla.org',
    url='https://github.com/mozilla-services/python-dockerflow',
    license='MPL 2.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment :: Mozilla',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
    ],
    zip_safe=False,
)

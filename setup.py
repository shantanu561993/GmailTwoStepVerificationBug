#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup
setup(
    name='GmailTwoStepVerificationBug',
    version='1.0',
    description="This package checks if two step verification exists on a Gmail id without sending the user an SMS or any kind of notification.. :D",
    author="Shantanu Khandelwal",
    author_email='shantanu561993@gmail.com',
    url='https://github.com/shantanu561993/GmailTwoStepVerificationBug',
    download_url = 'https://github.com/shantanu561993/FAndR/tarball/0.1.2',
    packages=[
        'GmailTwoStepVerificationBug',
    ],
    package_dir={'GmailTwoStepVerificationBug':
                 'GmailTwoStepVerificationBug'},
    license="BSD",
    keywords=['GmailTwoStepVerificationBug','GMAIL','BUG','GMAIL BUG','two step verification'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
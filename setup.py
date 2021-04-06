from setuptools import setup, find_packages

setup(
	name='nx-django-dbtunnel',
	version='2.0.0',
	description='Connect to and use a remote database over an SSH tunnel in Django & Python3',
	url='https://github.com/NextiaDev/django-dbtunnel',
	author='mvx24',
	author_email='cram2400@gmail.com',
	license='MIT',
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Environment :: Console',
		'Framework :: Django',
		'License :: OSI Approved :: MIT License',
		'Operating System :: MacOS :: MacOS X',
		'Operating System :: POSIX',
		'Operating System :: Unix',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3 :: Only',
		'Topic :: System :: Systems Administration'
	],
	keywords='ssh tunnel production database django paramiko mysql postgresql python3',
	packages=find_packages(),
	install_requires=['django', 'paramiko'],
)

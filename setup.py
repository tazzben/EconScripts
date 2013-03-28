try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

long_desc = """
	By using a simulation of firm sizes (using a lognormal distribution) and specified geographic regions, standard deviations and employee head count, we can compute the critical regions for the Ellison & Glaeser statistic. In the process, it also calculates herfindahl values and provides critical regions.
"""


setup(name="EGSimulation",
      version=1.0,
      description="Simulate the Ellison & Glaeser statistic using randomness alone",
      author="Ben Smith",
      author_email="tazz_ben@ad.wsu.edu",
      url="https://github.com/tazzben/EconScripts/tree/master/Simulations/Python/EG%20Statistic",
      license="Public Domain",
      packages=[],
	  scripts=['EGSimulation'],
	  package_dir={},
      long_description=long_desc,
      classifiers=[
          'Topic :: Scientific/Engineering',
          'Environment :: Console',
          'Development Status :: 5 - Production/Stable',
          'Operating System :: POSIX',
          'Intended Audience :: Science/Research'
      ]
     )
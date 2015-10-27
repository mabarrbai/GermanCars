from setuptools import setup

setup(name='TusPachangas',
      version='0.1',
      description='Aplicación web para gestionar peñas de fútbol',
      url='https://github.com/mabarrbai/TusPachangas',
      author='Manuel Alejandro Barranco Bailón',
      author_email='mabarranco@correo.ugr.es',
      license='GNU GENERAL PUBLIC LICENSE',
      packages=['TusPachangas'],
      install_requires=[
          'django','wheel'
      ],
      zip_safe=False)

#!/usr/bin/env python3
from setuptools import setup


PLUGIN_ENTRY_POINT = 'jarbas_precise_ww_plug=jarbas_wake_word_plugin_precise:PreciseHotwordPlugin'
setup(
    name='jarbas-wake-word-plugin-precise',
    version='0.2.1',
    description='A wake word plugin for mycroft',
    url='https://github.com/JarbasLingua/jarbas-wake-word-plugin-precise',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='Apache-2.0',
    packages=['jarbas_wake_word_plugin_precise'],
    install_requires=["precise-runner>=0.2.1",
                      "ovos-plugin-manager>=0.0.1a2",
                      "petact>=0.1.2",
                      "pyxdg>=0.26"],
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='mycroft plugin wake word',
    entry_points={'mycroft.plugin.wake_word': PLUGIN_ENTRY_POINT}
)

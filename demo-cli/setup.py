from setuptools import setup

setup(
    name = "demo-cli",
    entry_points = {
        'console_scripts': [
            'demo = app.__main__:main'
        ]
    },
)

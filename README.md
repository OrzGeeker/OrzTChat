# OrzPyPi

A personal PyPi package template project for developing tools.

## Usage

If you want to develop a tool named `DemoTool`, you can init the template with command following:

```bash
$ git clone https://github.com/OrzGeeker/OrzPyPi.git  DemoTool
```

After you clone the template project into your local disk file system, you should change the information
of `README.md` and `setup.py` to fit your need.

You can use the script `make_env` to create python2 or python3 virtual environment.

activate virtual env with command follow after you created python virtual environment: 

```bash
$ source py2/bin/activate

or

$ source py3/bin/activate
```

You can write you code under `src` directory.

When publish you package, you can use the `publish` script to automation this process if you have register your account on Pypi.org

## How to write README.md

This is a simple example package. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.

## How to Publish

[publish tutorial](https://packaging.python.org/tutorials/packaging-projects/)

## Choose you license

[Choose a License for your self](https://choosealicense.com)

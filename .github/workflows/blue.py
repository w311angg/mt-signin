# This workflow will install Python dependencies, run tests and lint with a single version of Python
# For more information see: https://help.github.com/actions/language-and-framework-guides/using-python-with-github-actions

name: Blue

on:
  push:
    branches: [ main ]
    paths:
      - 'blue.py'
  watch:
    types: started
  schedule:
    - cron: '0 2 * * *'
  workflow_dispatch:

jobs:
  build:

    runs-on: ubuntu-latest
    if: github.event.repository.owner.id == github.event.sender.id
    environment: Production

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python 3.9
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    - name: Setup timezone
      uses: zcong1993/setup-timezone@master
      with:
        timezone: Asia/Shanghai
    - name: Run
      env:
        cookie: ${{ secrets.blue_cookie }}
      run: |
        python blue.py

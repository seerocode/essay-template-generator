# essay-template-generator
I spent a night and a half making an app to build a 3,000 word essay template because I didn't want to manually copy and paste a sample paragraph 30 times.

Even worse, I wrote 50 LINES OF CODE only to realize all I needed were three lines.

This is very brute force so it's not pretty but it works!

Try it out yourself by following these instructions:
- Open your terminal or command line and navigate to the folder you would like to copy this project to using the `cd` command
- Clone the repo by typing: 
```git clone git@github.com:seerocode/essay-template-generator.git```
- Install virtualenv via pip:
```pip install virtualenv```
- Create a virtual environment for the project:
```virtualenv paper_generator```
- Activate the virtual environment:
```source paper_generator/bin/activate```
- Install the project requirements:
```pip install -r requirements.txt```
- Run the app:
```python paper_generator.py```

To deactive the virtual environment, type: `deactivate`

### TOC:
- templates/index.html = the landing page
- templates/get_essay.html = the resulting essay template
- paper_generator.py = the Flask app file
- test.py = tester python file
- 50_lines_of_code_when_i_only_needed_three.py = all that work for nothing

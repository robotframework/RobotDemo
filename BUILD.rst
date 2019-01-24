Instructions to create releases
===============================

1. Test that everything works with Python 2 and Python 3. Exactly one test
   ought to fail::

     python2 -m robot .
     python3 -m robot .

2. Regenerate log and report if needed using the command documented in wiki::

     robot --name Robot --loglevel DEBUG keyword_driven.robot data_driven.robot gherkin.robot

3. Regenerate also library docs if needed::

     python -m robot.libdoc CalculatorLibrary.py CalculatorLibrary.html

4. Move regenerated log, report and library doc to
   https://github.com/robotframework/RobotDemo/docs
   to make them visible online.

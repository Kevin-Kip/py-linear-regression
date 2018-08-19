## Linear Regression (in Python)
This is a basic implementation  of Linear Regression.

The basic formula is `y = mx + b`, where:
1. y is the output,
2. m is the slope of the line,
3. x is the input and
4. b is the y-intercept.

## Easy, Right?
Yes, Linear Regression is the most basic of all.

## Solving mysteries
Since `x` is what the user inputs, and `y` is what the algorithm spits out, "what is m and b" you may ask?

Well:
`m = sum of (eachX - meanOfX)*(eachY - sumOfY) / sum of(square of (eachX - meanOfX))`
`b = meanOfY - (m * meanOfX)`

## You wanna try code?
1. CLone download the repo
2. navigate to the root directory
3. run in terminal `python main.py`

You will be prompted to input a number and you will receive a prediction(float).
import statsmodels.api as sm
X = [1, 2, 3]
Y = [1, 2, 3]
X = sm.add_constant(X)  # Adds an intercept to the model
model = sm.OLS(Y, X).fit()
print(model.summary())

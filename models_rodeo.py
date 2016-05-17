import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm
from sklearn.cross_validation import train_test_split
from sklearn import linear_model
from sklearn.cross_validation import cross_val_predict


def load_data(wdir):
    filename = wdir + 'clean_cards.csv'
    df_cards = pd.DataFrame.from_csv(filename, sep='\t', encoding='utf-8')
    df_minions = df_cards[df_cards['type'].isin(['minion'])]
    return df_minions


def train_cv_test_split(df, split_sizes=[1.0, 0.0, 0.0]):
    assert sum(split_sizes) == 1
    train_size = split_sizes[0]
    cv_size = split_sizes[1]
    test_size = split_sizes[2]
    train, test = train_test_split(df, test_size=test_size)
    train, cv = train_test_split(train, test_size=cv_size)
    return train, cv, test


def human_readable_coefficients(df, predictor):
    return pd.DataFrame(
        zip(df.columns, predictor.coef_),
        columns=['features', 'predicted_coefficients']
    )


def helper_info(df):
    x = set(df.columns)
    for i in x:
        print i
    loatheb = df[df.name == 'loatheb']

# def main():
wdir = '/Users/dwhitehead/Documents/github/hearthstone_analytics/'
df = load_data(wdir)
df['intercept'] = 1
dep_var = ['cost']
indep_vars = [
    'attack',
    'health',
    'charge',
    'taunt',
    'stealth',
    'divine_shield',
    'intercept'
]
lr = linear_model.LinearRegression(
    fit_intercept=False,
    normalize=False,
    copy_X=True,
    n_jobs=1
    )
lr.fit(
    df[dep_var],
    df[indep_vars]
)

df_coefficients = human_readable_coefficients(
    df[indep_vars],
    lr
)

y = df[indep_vars].as_matrix()
print y.shape
lr.predict(y)

y = lr.predict(df[indep_vars])
y = lr.predict([1,1,1,1,1,1,1])
print y

x = lr.coef_
print x
x.transpose()
lr.predict(x.transpose())
y = df[:1][indep_vars].transpose()
lr.predict(y)
print y
print lr.coef_.shape
print lr.coef_
print df[:1][indep_vars]
print sum(x*y.values)

df = pd.DataFrame(lr.predict(df[indep_vars]))
print lr.predict(df[:1][indep_vars].reshape())
df['predicted_cost'] = df[indep_vars].apply(lambda x: sum(x.values*lr.coef_))

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean square error
print("Residual sum of squares: %.2f"
      % np.mean((regr.predict(diabetes_X_test) - diabetes_y_test) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr.score(diabetes_X_test, diabetes_y_test))

# Plot outputs
plt.scatter(diabetes_X_test, diabetes_y_test,  color='black')
plt.plot(diabetes_X_test, regr.predict(diabetes_X_test), color='blue',
         linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
# # for x in indep_vars:
# plt.scatter(
#     df['cost'],
#     df['charge'],
    

# # set up figure
# fig, ax1 = plt.subplots()
# # ax1
# ax1.scatter(
#     x=temp.index,
#     y=temp['rpdeliveries'],
#     color=temp['color'],
#     marker=markers[idx]
# )
# ax1.set_xlabel('Conditional Sort')
# ax1.set_ylabel('Rpdelivery ($)')
# # ax2
# ax2 = ax1.twinx()
# ax2.scatter(
#     x=temp.index,
#     y=temp['deliveries_cumsum'],
#     color='green',
#     marker=markers[idx]
# )
# ax2.set_ylabel('Cumulative Deliveries')

# Y = df[dep_var]
# X = df[indep_vars]
# result = sm.OLS( Y, X ).fit()
# result.summary()


# train, cv, test = train_cv_test_split(df, [0.75, 0.15, 0.1])

# if __name__ == '__main__':
# 	main()
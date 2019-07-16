'''
https://qiita.com/physics303/items/e062d94fb529f6a42b3e
'''
import random

import numpy as np
import matplotlib.pyplot as plt

def generate_data(coef, num_points, ndim, noise_variance, xmin=-1.5, xmax=1.5):
    '''
    Generate training data.

    Parameters
    ----------
    coef : list
        coefficients of the polynomial

    num_points : int
        number of points in the data

    n_dim : int
        number of dimention of the data

    noise_variance: float
        variance of additional noise

    xmin : float
        minimum value of the input data

    xmax : float
        maximum value of the input data
    '''

    X = np.zeros(num_points)
    Y = np.zeros(num_points)
    noised_Y = np.zeros(num_points)

    for i in range(num_points):
        X[i] = random.uniform(xmin, xmax)

        for j in range(ndim + 1):
            Y[i] += coef[j]*X[i]**j

        noised_Y[i] = np.random.normal(loc=Y[i], scale=noise_variance)

    return X, noised_Y

def fit_predict(X, Y, pred_ndim, m, lamb, num_data, noise_variance):
    '''
    Fit data to estimate parameter w, and predict y for each x.

    Parameters
    ----------
    X: array_like
        training data (input)

    Y: array_like
        training data (output)
    pred_ndim: int
       dimention of the polynomial model
    coef: list
        coefficients of the polynomial
    m: array_like
        expectation vector of the prior distribution

    lamb: array_like
        precision matrix of the prior distribution

    num_data: int
        number of training data
    noise_variance: float
        variance of additional noise
    '''
    #set of input vector represented as (1, x, x^2, x^3...)
    input_vecs = np.zeros((num_data, pred_ndim+1))
    #sigma_{n=1}^N x_n x_n^T for new precision matrix
    sum1 = np.zeros((pred_ndim+1, pred_ndim+1))
    #sigma_{n=1}^N y_n x_n for new expectation vector
    sum2 = np.c_[np.zeros(pred_ndim+1)]

    #create input_vecs
    for i in range(num_data):
        for j in range(pred_ndim+1):
            input_vecs[i][j] = X[i]**j
        #use each input vector to calculate sum1 and sum2
        sum1 = sum1 + np.dot(input_vecs[[i]].T, input_vecs[[i]])
        sum2 = sum2 + Y[i] * input_vecs[[i]].T
    #new precision matrix
    lamb_hat = noise_variance * sum1 + lamb
    #new expectation vector
    m_hat = np.linalg.inv(lamb_hat).dot(noise_variance * sum2 + lamb.dot(m.T))

    xmin_pred = -1.5
    xmax_pred = 1.5

    pred_x = np.linspace(xmin_pred, xmax_pred, 100)
    pred_y = np.zeros(100)
    for i in range(100):
        for j in range(pred_ndim+1):
            pred_y[i] = pred_y[i] + m_hat[j] * pred_x[i]**j

    #plot predicted function and training data
    plt.scatter(X, Y, label="Training data")
    plt.plot(pred_x, pred_y, c='red', label="Predicted y")
    plt.legend()
    plt.title("Number of data=" + str(num_data) + " variance of noise=" + str(noise_variance))
    plt.xlabel("x")
    plt.ylabel("y")
    plt.xlim(xmin_pred, xmax_pred)
    plt.ylim(0, 3.5)
    plt.grid()
    plt.show()

    return lamb_hat, m_hat

def probability(pred_ndim, num_data, noise_variance, lamb_hat, m_hat):
    '''
    Calculate probabity of predicted y.

    Parameters
    ----------
    pred_ndim: int
       dimention of the polynomial model
    noise_variance: float
        variance of additional noise
    lamb_hat: array_like
        precision matrix of posterior distribution
    m_hat: array_like
        expectation vector of posterior distribution
    '''

    xmin_probability_density = -1.5
    xmax_probability_density = 1.5

    N = 30 #levels of color plot
    x = np.linspace(xmin_probability_density, xmax_probability_density, N)
    y = np.linspace(0, 3.5, N)
    probability = np.zeros((N, N))

    for i in range(N):
        predicted_input_vector = np.zeros(pred_ndim+1)

        for k in range(pred_ndim+1):
            predicted_input_vector[k] = x[i]**k

        m_ast = np.dot(m_hat.T, predicted_input_vector.T)
        lamb_ast = 1.0/noise_variance \
                + predicted_input_vector.dot(np.linalg.solve(lamb_hat, predicted_input_vector))

        for j in range(N):
            probability[j][i] = normal_distribution(y[j], m_ast, lamb_ast)

    # color plot probability
    x, y = np.meshgrid(x, y)
    plt.pcolor(x, y, probability)
    cbar = plt.colorbar(ticks=[]) #no ticks for colorbar
    cbar.set_label('Probability')
    plt.title("Number of data=" + str(num_data) + " variance of noise=" + str(noise_variance))
    plt.clim(0, 100)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(xmin_probability_density, xmax_probability_density)
    plt.ylim(0, 3.5)
    plt.show()

def normal_distribution(x, mu, lamb):
    '''
    One dimentional normal distribution

    Parameters
    ----------
    x: float
        input value
    mu: float
        expectation
    lamb: float
        precision
    '''

    cov = 1.0 / lamb

    return 1.0/(np.sqrt(2.0*np.pi)*cov**2)*np.exp(-(x-mu)**2/(2.0*cov**2))

def main():
    pred_ndim = 4
    data_ndim = 4

    coef = [2, 0.5, -2, 0, 1] #Ground truth coefficients

    num_data = 1000
    noise_variance = 0.1

    #Hyper parameters for prior distribution
    mu = np.ones(pred_ndim+1)
    lamb = np.zeros(pred_ndim+1)

    #Generate training data
    X, Y = generate_data(coef, num_data, data_ndim, noise_variance)

    lamb_hat, mu_hat = fit_predict(X, Y, pred_ndim, mu, lamb, num_data, noise_variance)

    probability(pred_ndim, num_data, noise_variance, lamb_hat, mu_hat)

if __name__ == "__main__":
    main()


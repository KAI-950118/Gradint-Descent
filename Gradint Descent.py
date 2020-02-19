import numpy as np

# y = w * x + b
def Computer_loss_to_show(w, b, points):
    total_error = 0
    for i in range(0, len(points)):
        x = points[i][0]
        y = points[i][1]
        loss = (w * x + b - y) ** 2
        total_error += loss
    return total_error / float(len(points))

def Gradint_descent(w, b, points, learning_rate):
    w_gd = 0
    b_gd = 0
    n = float(len(points))
    for i in range(0, len(points)):
        x = points[i][0]
        y = points[i][1]
        w_gd += 2 / n * x * (w * x + b - y)
        b_gd += 2 / n * (w * x + b - y)
    w_new = w - w_gd * learning_rate
    b_new = b - b_gd * learning_rate
    return [w_new, b_new]

def Iterations(w_starting, b_starting, points, learning_rate, running_times):
    w = w_starting
    b = b_starting
    for i in range(0, running_times):
        w, b = Gradint_descent(w, b, points, learning_rate)
    return [w, b]

def run():
    points = np.genfromtxt("TrainData.csv", delimiter=",")
    learning_rate = 0.02
    w_starting = 0
    b_starting = 0
    running_times = 10000
    print("initial w={0}, b={1}, error={2}".format(w_starting, b_starting,
                                               Computer_loss_to_show(w_starting, b_starting, points))
          )
    w_new, b_new = Iterations(w_starting, b_starting, points, learning_rate, running_times)
    print("after {0} times iterations w={1}, b={2}, error={3}".format(running_times, w_new, b_new,
                                                                  Computer_loss_to_show(w_new, b_new, points))
          )

if __name__ == '__main__':
    run()

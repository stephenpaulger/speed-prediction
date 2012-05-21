import csv
import numpy
import pylab
import scipy

from scipy.optimize import fmin


def runkeeper_import(filename, activity):
    """
    Import data series from RunKeeper's data export.
    """
    def to_minutes(duration):
        """
        Convert duration "hh:mm:ss" to minutes.
        """
        (h, m, s) = map(int, duration.split(":"))
        return (h*60.0) + m + (s/60.0)

    rk_csv = csv.DictReader(open(filename))
    x = []
    y = []
    for row in rk_csv:
        if row["Type"] != activity:
            continue
        x.append(float(row["Distance (mi)"]))
        y.append(to_minutes(row["Duration"]))

    return (numpy.array(x), numpy.array(y))


fp = lambda c, x: c[0]*x*x + c[1]*x


def calculate_params(x, y):
    err = lambda p, x, y: (abs((fp(p,x)-y))).sum()
    initial_params = numpy.array([1, 1])
    return fmin(err, initial_params, args=(x, y))


def text_output(params):
    print "t = time in minutes; d = distance in miles"
    print "t = %f*d*d + %f*d" % (params[0], params[1])
    print "   5k = %d minutes" % fp(params, 5 * 0.621371192)
    print "  10k = %d minutes" % fp(params, 10 * 0.621371192)
    print "26.2m = %d minutes" % fp(params, 26.2)


def chart_output(params):
    xx = scipy.linspace(0, max(x), 30)
    pylab.plot(x, y, "bo", xx, fp(params, xx), "r")
    pylab.show()


if __name__ == "__main__":
    (x, y) = runkeeper_import("cardioActivities.csv", "Running")
    params = calculate_params(x, y)
    text_output(params)
    chart_output(params)

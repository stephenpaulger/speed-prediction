speed-prediction
================

Predicting speed based on activity history.

Note that the results from this program are highly likely to be wrong
by a significant margin and have not been tested. The margin of error
will be greater for greater extrapolations so please be realistic about
the limitations of the technique being used to generate the predictions.

The prediction works by assuming that the line of best fit ona chart of
distance vs time will be of the form

![y = ax^2 + bx](http://www.sciweavers.org/tex2img.php?eq=y%20%3D%20ax%5E2%20%2B%20bx&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)

The program just has to find the correct values of a and b.

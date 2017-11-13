# Autonomous-Garbage-Collector


Autonomous Garbage Collection System
Boga Vishal (ECE Dept, MIT Manipal), Abhijeet Kumar Sinha(EEE Dept, MIT Manipal), Anubhav Apurva(CCE Dept, MIT Manipal), and Mudit Malpani (ECE Dept, MIT Manipal)

 
Abstract—Autonomous cleaning is a progressive step towards better future.Autonomous Garbage collection system like Roomba fails to establish a closed-loop system and performs autonomous routine cleaning. In this paper, we will like to propose a closed loop garbage collection autonomous cleaning system which will identify garbage and direct a rover to the garbage to collect it.
Keywords—Image Processing, Deep Neural Networks, LATEX, Aruco Markers, A star Algorithm.
	I.	INTRODUCTION
The closed-loop garbage collection autonomous cleaning system identifies garbage and directs a rover to the garbage to collect it. The detection of garbage is done in a controlled environment using image processing, so is the detection of obstacle done to map the shortest path between the targeted garbage and rover. The data is collected from the webcam, which is placed over the ceiling and connected to a mini computer. And finally, an Image Classifier is used to label images as garbage and non-garbage. If it is labeled garbage, rover follows the shortest path which is decided by A star algorithm avoiding all obstacles to collect it.
A. Garbage detection
To detect a garbage we first take a reference image (image without garbage) and a goal image (image with garbage).Then we perform filtering to remove noises from both of these images, these images were taken from a surveillance camera and so we expect gaussian noise in images.
1)	Gaussian noise: Gaussian noise is formed by impulse noises which has a probability distribution of a normal distribution. It has impulse at origin and then the signal decays in all other dimensions Probability density function P of a Gaussian Random Variable (z)
2)	Gaussian Blur Filter: We apply Gaussian filter on both images.It is a linear filter. It blurs the image and thus reduce impulse noise. Subtracting two gaussian filtered images gives a un-sharp image. The Gaussian filter alone will blur edges and reduce contrast. Gaussian filters are faster than median filter because of less multiplications required but it cannot filter the salt and pepper noises.
 
Reference images after Gaussian filtering
 
Goal images after Gaussian filtering
3)	BGR image to GrayScale image: Converting image to grayscale eliminates the hue and saturation information while keeping the luminance.
4)	Absolute difference : The noise-free grayscale images are then subtracted to get the new object.
 
Absolute differene
5)	Closed binary image: The noise-free grayscale images are then subtracted to get the new object.
6)	Contour mapping: To identify closed contours we have used a openCv function for which we need to perform thresholding to convert grayscale to binary and then dilation to convert open shapes to closed contours.
JOURNAL OF LATEX OCTOBER 2017	2
New Detected object
7)	Image Classifier: The images of these objects are then sent to an Image classifier to label it as garbage or nongarbage.One suck classifier is Google Cloud Api,it helps in classifying image on cloud hence reducing processing cost.
B. Obstacle detection
Reference image after changing to grayscale is then subjected to canny edge detection and the closed contours are then obtained using the above process and obstacles are recognized.
C. Rover detection
An Aruco marker is placed above the rover. Aruco marker is an identification marker which can be identified in any orientation and angle.The codification employed on Aruco Marker is a slight modification of the Hamming Code. So in a 5 bit Aruco marker 2 bits are information bit and 3 bits are used for error detection
 
Detected Aruco
D. Grid Division
The Reference image is then divided into grids using in multiples of the size of rover. And then the image grid is converted into matrix grid with the following notation.
Free Space = Zero
Obstacles = Negative One
Goal Image = Two
Detected Path = Positive One
 
Original Matrix
E. Shortest path
The shortest path between origin(position of rover) and goal (garbage) is found using A star algorithm. A star is a heuristic search algorithm which means it works on principle of reducing distance from goal. Though this is not the most efficient algorithm for path detection as Graphs but its accuracy is still promising.
 
Path Matrix
And the detected path is:
 
Found path
	II.	CONCLUSION
This closed-loop autonomous system is very precise as the closed loop direct feedback applied in real time by camera over the environment makes sure that rover is in the right direction. This system is highly advisable for Commercial places such as malls, hospitals and especially in public places like parks.
REFERENCES
[1]	Inderpreet Singh and P. W. Daly, Performance Comparison of Various Image Denoising Filters Under Spatial Domain , International Journal of Computer Applications (0975 8887) Volume 96-No.19, June 2014.
[2]	Gaussian	Noise	[Online].	Available: https://www.cs.auckland.ac.nz/courses/Gaussian

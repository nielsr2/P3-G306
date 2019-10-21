import cv2
import numpy as np
from matplotlib import pyplot as plt
import PIL


def semiCircle:
    #cv2.Mat img = cv2.imread("iris_test.jpeg")
    img = cv2.imread("iris_test.jpeg")
    
    gray=cv2.cvtColor(img,cv2.COLOR_GRAY2BGR )
    
    

int main()
{
    cv::Mat color = cv::imread("../houghCircles.png");
    cv::namedWindow("input"); cv::imshow("input", color);

    cv::Mat canny;

    cv::Mat gray;
    # Convert it to gray
    cv::cvtColor( color, gray, CV_BGR2GRAY );

    # compute canny (don't blur with that image quality!!)
    cv::Canny(gray, canny, 200,20);
    cv::namedWindow("canny2"); cv::imshow("canny2", canny>0);

    std::vector<cv::Vec3f> circles;

    # Apply the Hough Transform to find the circles
    cv::HoughCircles( gray, circles, CV_HOUGH_GRADIENT, 1, 60, 200, 20, 0, 0 );

    # Draw the circles detected
    for( size_t i = 0; i < circles.size(); i++ ) 
    {
        Point center(cvRound(circles[i][0]), cvRound(circles[i][1]));
        int radius = cvRound(circles[i][2]);
        cv::circle( color, center, 3, Scalar(0,255,255), -1);
        cv::circle( color, center, radius, Scalar(0,0,255), 1 );
    }

    #compute distance transform:
    cv::Mat dt;
    cv::distanceTransform(255-(canny>0), dt, CV_DIST_L2 ,3);
    cv::namedWindow("distance transform"); cv::imshow("distance transform", dt/255.0f);

    # test for semi-circles:
    float minInlierDist = 2.0f;
    for( size_t i = 0; i < circles.size(); i++ ) 
    {
        # test inlier percentage:
        # sample the circle and check for distance to the next edge
        unsigned int counter = 0;
        unsigned int inlier = 0;

        cv::Point2f center((circles[i][0]), (circles[i][1]));
        float radius = (circles[i][2]);

        # maximal distance of inlier might depend on the size of the circle
        float maxInlierDist = radius/25.0f;
        if(maxInlierDist<minInlierDist) maxInlierDist = minInlierDist;

        #TODO: maybe paramter incrementation might depend on circle size!
        for(float t =0; t<2*3.14159265359f; t+= 0.1f) 
        {
            counter++;
            float cX = radius*cos(t) + circles[i][0];
            float cY = radius*sin(t) + circles[i][1];

            if(dt.at<float>(cY,cX) < maxInlierDist) 
            {
                inlier++;
                cv::circle(color, cv::Point2i(cX,cY),3, cv::Scalar(0,255,0));
            } 
           else
                cv::circle(color, cv::Point2i(cX,cY),3, cv::Scalar(255,0,0));
        }
        std::cout << 100.0f*(float)inlier/(float)counter << " % of a circle with radius " << radius << " detected" << std::endl;
    }

    cv::namedWindow("output"); cv::imshow("output", color);
    cv::imwrite("houghLinesComputed.png", color);

    cv::waitKey(-1);
    return 0;
}
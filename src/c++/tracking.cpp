#include <fstream>
#include <iostream>
#include <opencv2/core/ocl.hpp>
#include <opencv2/opencv.hpp>
#include <opencv2/tracking.hpp>
#include <string>

using namespace cv;
using namespace std;

int main(int argc, char** argv) {
    // Set up video path
    std::string homedir = getenv("HOME");
    std::string projpath =
        "/Documenti/università/sistemi_complessi/pendolum_sync";
    std::string relvideopath =
        "/media/video/video_ste/video_ste_cut_finale.mp4";
    std::string videopath = homedir + projpath + relvideopath;

    // Choose which object to track and run number
    std::string relobjpath;
    int run_number;

    std::cout << "Input p or c followed by sx or dx to choose which object to "
                 "track \n";
    std::string sceltaobj;
    std::cin >> sceltaobj;

    std::cout << "Input the run number \n";
    std::cin >> run_number;

    if (sceltaobj == "psx") {
        relobjpath = "/data/sxpendolum_";
    }
    if (sceltaobj == "pdx") {
        relobjpath = "/data/dxpendolum_";
    }
    if (sceltaobj == "csx") {
        relobjpath = "/data/sxcart_";
    }
    if (sceltaobj == "cdx") {
        relobjpath = "/data/dxcart_";
    }
    relobjpath = relobjpath + std::to_string(run_number) + ".txt";

    // Set up output data files paths
    std::string objpath = homedir + projpath + relobjpath;

    // Create tracker object
    Ptr<Tracker> tracker;
    tracker = TrackerKCF::create();

    // Read video
    VideoCapture video(videopath);

    // Exit if video is not opened
    if (!video.isOpened()) {
        cout << "Could not read video file" << endl;
        return 1;
    }

    Mat frame;
    Rect bbox;

    // Open and reset files for writing
    ofstream fobj;
    fobj.open(objpath, ios::out | ios::trunc);

    // Read first frame
    bool ok = video.read(frame);

    // Resizing window dimension
    namedWindow("selectionwindow", WINDOW_NORMAL);

    // Select and create a bounding box, showing crosshair, starting from
    // center
    bbox = selectROI("selectionwindow", frame, true, true);
    rectangle(frame, bbox, Scalar(255, 0, 0), 2, 1);

    // Load center position coordinates in file
    fobj << bbox.x + bbox.width / 2 << " " << bbox.y + bbox.height / 2 << "\n";

    // Resizing window dimension
    namedWindow("Tracking", WINDOW_NORMAL);

    // Display all box.
    imshow("Tracking", frame);

    // Start tracking
    tracker->init(frame, bbox);

    // Iterate
    while (video.read(frame)) {
        // Start timer
        double timer = (double)getTickCount();

        // Update the tracking result
        bool ok = tracker->update(frame, bbox);

        // Load center position coordinates in file
        fobj << bbox.x + bbox.width / 2 << " " << bbox.y + bbox.height / 2
             << "\n";

        // Calculate Frames per second (FPS)
        float fps = getTickFrequency() / ((double)getTickCount() - timer);

        if (ok) {
            // Tracking success : Draw the tracked
            // object
            rectangle(frame, bbox, Scalar(255, 0, 0), 2, 1);
        } else {
            // Tracking failure detected.
            putText(frame, "Tracking failure detected", Point(100, 80),
                    FONT_HERSHEY_SIMPLEX, 0.75, Scalar(0, 0, 255), 2);
        }

        // Display tracker type on frame
        putText(frame, " Tracker", Point(100, 20), FONT_HERSHEY_SIMPLEX, 0.75,
                Scalar(50, 170, 50), 2);

        // Resizing window dimension
        namedWindow("Tracking", WINDOW_NORMAL);

        // Display frame.
        imshow("Tracking", frame);

        // Exit if ESC pressed.
        int k = waitKey(1);
        if (k == 27) {
            break;
        }
    }

    // Close file
    fobj.close();
}
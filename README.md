# Welcome to the ROS -> ROS2 Guide wiki!

This repository has been primarily created as a platform to host a wiki for topics involving ROS1 to ROS2 migration. Please navigate to the Wiki tab of this repository or click the links below for moreinformation. Some code for examples will be included in the repository and I will read and update issues as they are posted, but their focus should be primarily on the Wiki itself. I hope this guide is useful to you. Thanks for visiting.

## Purpose

The goal of this wiki is to provide a starting point for ROS1 users to start updating packages to ROS2 and provide some useful information to aid in the transition. In May 2023 ROS1 [Melodic](http://wiki.ros.org/melodic) reaches its end of life and with it future support for python2 in ROS projects. In May 2025, ROS1 [Noetic](http://wiki.ros.org/noetic) reaches its end of life ending ROS1 support. For ROS users who wish to continue to develop their projects in conjunction with the ROS community, migrating to ROS2 is inevitable. This guide hopes to ease that transition before that time.

### ros.org

My intent in this guide was to address some of the resources I thought were missing in the current documentation on Ros.org as I learned ROS2. As I began writing I realized there were quite a few more resources than I initially anticipated. I aim to be as minimally redundant as possible in this guide, but inevitably there will be some overlap (and I suppose there is something to be said about having all the required resources in one place). To that end here are a few links that address some ROS1 -> ROS2 topics that I certainly haven't covered, especially when it comes to the build system and converting various file formats I haven't dealt with yet.

- [Migrating guide from ROS1](https://docs.ros.org/en/foxy/Contributing/Migration-Guide.html)
- [Launch file migration guide](https://docs.ros.org/en/foxy/How-To-Guides/Launch-files-migration-guide.html)
- [YAML Parameters migration guide](https://docs.ros.org/en/foxy/How-To-Guides/Launch-files-migration-guide.html)

## Organization

There are three main sections in this guide as well as some supplementary material and in the future a step-by-step tutorial to deliberately migrate a ROS1 package to ROS2. The three sections are as follows:

### -[Code Formatting](https://github.com/ninjajoe9/ROS-ROS2-Guide/wiki/Code-Formatting) and Migration

ROS2 has a specific object-oriented manner of organizing nodes, topics and communication so examples how to transition specific lines of code from one version to the other, as well as information on how to organize code in the file system is included here.

### -[ROS CLI](https://github.com/ninjajoe9/ROS-ROS2-Guide/wiki/ROS-CLI)

Manipulating ROS in the command line is significantly different in ROS2 and, while the names of things remain similar, the syntax and many of the arguments have changed. ROS2 CLI also includes functionalities that didn't previously exist in ROS1 so these additions will be covered.

### -Additional [ROS2 Features](https://github.com/ninjajoe9/ROS-ROS2-Guide/wiki/ROS2-Features) and their implementation

ROS2 offers many built in features and capabilities that were not implemented with the base ROS1 installation so some of these new features and information on how to use them will be included here.

### [Turtlesim](https://github.com/ninjajoe9/ROS-ROS2-Guide/wiki/Turtlesim-Full-Project-Example) Full Project Example

This section outlines how you would combine all of these aspects together into a full project using the built in Tutlesim package within both ROS1 and ROS2. The goal is to show how ROS2 can fully replicate your ROS1 packages and hopefully implement additional features with ease.  

## Notes and ROS Wiki

This guide assumes familiarity with ROS1. Additionally, ROS2 relies heavily on OOP concepts and assumes the reader has familiarity with this paradigm of programing. If you have worked in Python3 or C++ (the two most used ROS programing languages) it is likely you are already familiar, however the structure of some of ROS2 code can be difficult without it. Additionally I aim to avoid reproducing anything the currently exists on the ROS.org wiki, but it's quite large and I certainly have not read all of it. Where applicable I will link ROS.org resources and will only replicate when I feel it detracts from the flow of the wiki to ask you to go to another link. If major redundancies are found, by all means notify me and I will endeavor to rectify the duplication.

__Acknowledgements__

Thanks to Dr. Baillieul's Research Group and the Boston University Robotics Lab for allowing me to present this guide and asking me many questions that helped me identify errors and places for improvement.

Thank you to Edouard Renard of 'Robotics Back-end' on [YouTube](https://www.youtube.com/channel/UCelRThOKlWMnpjqr5EBq6tg) and 'ROS for Beginners' on [Udemey](https://www.udemy.com/course/ros-for-beginners/). Much of the code you see here is based on his instruction and recommendations for styling as good practice for developers in the ROS community. The format for the templates is from his examples and used with permission given in the tutorials I used in my personal learning journey, although the entirety of this work has been developed or independently recreated by me. Thank you.  

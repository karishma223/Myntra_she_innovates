# Myntra_she_innovates

![Screenshot 2024-07-16 001108](https://github.com/user-attachments/assets/fbc63853-8c2b-4701-944e-4fbf7e2861c9)
Data Collection :<br> 
Instagram posts are collected using Instagram's API, including:<br> 

Post's image<br> 
Number of likes<br> 
Number of comments<br> 
A sample of 20 comments per post<br> 
Image Segmentation :<br> 
Images are processed using YOLO (You Only Look Once) and SAM (Segment Anything Model) to isolate clothing items from the background.<br> 

Feature Extraction and Dimensionality Reduction :<br> 
Feature Extraction: The segmented images are passed through an autoencoder to extract compact representations (latent space) of the clothing items.<br> 
Dimensionality Reduction: Principal Component Analysis (PCA) is applied to reduce the dimensionality of the latent space.<br> 
Clustering<br> 
The PCA-transformed latent spaces are clustered using the K-Means algorithm. Each cluster represents a distinct fashion style.<br> 

Sentiment Analysis : <br> 
User comments associated with each post are analyzed using the AdaBoost algorithm to gauge public sentiment towards the fashion styles represented in the posts.<br> 

![Screenshot 2024-07-16 001128](https://github.com/user-attachments/assets/893f35a0-fe5f-4c0d-a7d5-b9f939d241b3)


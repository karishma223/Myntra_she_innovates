# Myntra_she_innovates

![Screenshot 2024-07-16 001108](https://github.com/user-attachments/assets/fbc63853-8c2b-4701-944e-4fbf7e2861c9)
Data Collection
Instagram posts are collected using Instagram's API, including:

Post's image
Number of likes
Number of comments
A sample of 20 comments per post
Image Segmentation
Images are processed using YOLO (You Only Look Once) and SAM (Segment Anything Model) to isolate clothing items from the background.

Feature Extraction and Dimensionality Reduction
Feature Extraction: The segmented images are passed through an autoencoder to extract compact representations (latent space) of the clothing items.
Dimensionality Reduction: Principal Component Analysis (PCA) is applied to reduce the dimensionality of the latent space.
Clustering
The PCA-transformed latent spaces are clustered using the K-Means algorithm. Each cluster represents a distinct fashion style.

Sentiment Analysis
User comments associated with each post are analyzed using the AdaBoost algorithm to gauge public sentiment towards the fashion styles represented in the posts.

![Screenshot 2024-07-16 001128](https://github.com/user-attachments/assets/893f35a0-fe5f-4c0d-a7d5-b9f939d241b3)


# 445_HW10

SVM with linear kernel:  
Accuracy: 0.9993  
  
Classification Report:  

              precision    recall  f1-score   support
           0       1.00      1.00      1.00      1200
           1       1.00      0.99      1.00       148

    accuracy                            1.00      1348
    macro avg       1.00      1.00      1.00      1348
    weighted avg    1.00      1.00      1.00      1348

--------------------------------------------------
SVM with poly kernel:  
Accuracy: 0.9866  
  
Classification Report:  

              precision    recall  f1-score   support
           0       0.99      1.00      0.99      1200
           1       0.99      0.89      0.94       148

    accuracy                           0.99      1348
    macro avg       0.99      0.95     0.96      1348
    weighted avg    0.99      0.99     0.99      1348

--------------------------------------------------
SVM with rbf kernel:  
Accuracy: 0.9941  
  
Classification Report:  

              precision    recall  f1-score   support
           0       1.00      1.00      1.00      1200
           1       0.99      0.96      0.97       148

    accuracy                           0.99      1348
    macro avg      0.99      0.98      0.98      1348
    weighted avg   0.99      0.99      0.99      1348

--------------------------------------------------

Conclusion: The accuracy metrics for all of these different options were surprisingly high, especially when I could make zero sense of the data myself. Thankfully, working with SVM was fairly simple, and the accuracy, recall, precision, and f1 score were very simple to get using methods we've worked with before.

# Captcha-Recognizer
Use deep learning techniques to recognize distorted characters in images.

Objective:
- To understand important concepts and enhance understandings in machine learning.
- To familiar with data collection, model creation and training procedures, such that to be able to apply knowledge practically within a short time.

Requirements:
- PyTorch (https://pytorch.org/get-started/locally/)
- matplotlib (pip install matplotlib)
- PySimpleGUI (pip install PySimpleGUI)
- requests (pip install requests)
- numpy (pip install numpy)
- cv2 (pip install opencv-python)


This project gives machine learning beginners a glimpse to:
- Fetch data from the Internet
- Label data
- Split data
- Pre-process data
- Train and finetune a model from nothing
- Visualize training progress and results.

Execution Order:
1. Clone / Download all files and unzip.
2. Execute "getData.py". Modify its content if you want to download more / less images each time.
3. Execute "label_helper.py". Browse, select files, click "Next". Then label.
4. Execute "split_data.py". Modify its content if you split images in another way.
5. Execute "train_script.py". This trains a neural network to recognize characters in images. Modify it content for more functionalities.

Things I've learnt:
- Transforming data into scalable things eg numbers.
- Principles behind different loss functions.
- Finding out reasons that why a neural network might not work.
- Finetuning a model and hyper-parameters.

Rooms for Improvements:
- Using other more advanced techniques such as Attention-based OCR (https://github.com/emedvedev/attention-ocr) for higher accuracy while having smaller datasets.
- Accuracy could be higher if more data are available.

Possible next steps:
- Could first use model to predict characters in unlabeled data, then manually correct labels if there're errors to speed up the process of data preparation.
- Do more web scraping to collect different forms of data online. Web-scraping task this time is way too easy.
- Perform Cluster Analysis / Unsupervised Learning on captchas to group similar images / characters together for easier labeling work. (Let the computer discover internal structure of data and do some initial labeling, then manually correct label of each clusters to reduce human intervene and repetitive labeling work.)

-------------------------------------------------------------------------------------------------------------------------------------

**Day 0**: Practice on easy datasets first, eg MNIST, CIFAR10.

**Day 1**: Define aim, wrote a crawler to collect data and labelling them.

**Day 2**: Wrote helper functions and model structures. Failed. Debug. Find documentations and understand them.

**Day 3**: Keep writing helper functions. Had deeper understanding on how do loss functions, optimizer, kernel, over-fit, under-fit, CNN, fully connected layers, multi-variable calculus (finally met something I learnt in school! :D), probability model etc. work and their effects. In the past I thought I have understood them all, but failure in implementation proved I'm not ready yet)

**Day 4**: Debug. Wrote visualizing tools to ensure programs are doing what I want. Pytorch Documentations. YouTube lessons. Stack Overflow. Kaggle. TowardsDataScience. Many more different webpages that I cannot name...

**Day 5**: After many times of debug, the model finally gave out something meaningful! Keep testing different combinations. The prediction rised from 10% to around 30% at the end of the day.

**Day 6**: Achieved satisfying result! Model achieved accuracy of 85% on characters and 54% on whole images.

**Day 7**: Good news! Achieved even more encouraging result! After a day of finetuning model structure and parameters, the model achieved accuracy of 96% on characters and 90% on whole images!! This is absolutely a milestone for a beginner :)
Previous version of this project: https://github.com/Hayden2018/Captcha-Recognizer

**Day 8-9**: Cleaning everything up to make them look nicer and upload codes.

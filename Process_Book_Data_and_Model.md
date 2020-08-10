#Data and Model
---

- **Week 1** Steven and Bobby assigned to data and model.  Two proposals are made for the project: 1. create a CNN for image classification as well as an RNN to generate text dynamically 2. Build new features on top of a pre-built model for number reading, and work on developing interesting application features (https://nanonets.com/blog/deep-learning-ocr/).
<img src="https://github.com/TREXKS/Image-to-Text/blob/master/Process%20Book%20Images/Week%201.png" title="Nanonet Tool" >

- **Week 2** .ipynb and dataset uploaded to GitHub as placeholders.  Decision made to make a simpler model which partners a CNN with a systematic text generator on the application side.  Decision also not to use any software for developing the model outside of Tensorflow, pandas, and PIL.</li>
	
- **Week 3** Many .csv’s received holding Real Estate data. As the project goal becomes finalized, a decision is made to move towards Keras wrapper for the rest of model development.</li>

- **Week 4** 14GB zip received holding Real Estate images.  New plan is to use a much larger dataset in order to more strongly train CNN.
<img src="https://github.com/TREXKS/Image-to-Text/blob/master/Process%20Book%20Images/Week%204.png" title="Raw Real Estate Images" >

- **Week 5** Return to .csv’s due to greater uniformity of images (outside shots of full buildings) and more easily parsed categories (shown below).
<img src="https://github.com/TREXKS/Image-to-Text/blob/master/Process%20Book%20Images/Week%205.png" title=".csv Real Estate Data" >

- **Week 6** A Keras CNN was built from the ground up predicting categories listed in .csv [SOLDPRICE, ZIP, BEDS, BATHS, etc.], data was cleaned (month by month files combined, rows with missing images removed, nonsensical and NA-items removed or replaced).
<img src="https://github.com/TREXKS/Image-to-Text/blob/master/Process%20Book%20Images/Week%206.png" title="Keras Google Colab" >

- **Week 7** VGGnet-16 keras model used for transfer learning. Current model generates feature-vec to be compared to feature-vec of dataset images in order to present similar real estate images. Model finally connected to application routes.
<img src="https://github.com/TREXKS/Image-to-Text/blob/master/Process%20Book%20Images/Week%207.png" title="Model Results" >

Link to Heroku: https://mysterious-river-00331.herokuapp.com/

#Postgres, Frontend, Backend
---
-**Week 1** Heroku, Flask, AWS planned as tech stack.  Backend/compling tasked to Bulti and Application tasked to Talis.  GitHub repo set up, CSS/Scripts uploaded, initial heroku url pushed.

-**Week 2** Project scope evaluated, and jupyter notebook connected to Flask app

-**Week 3** Moved away from the idea of using AWS.  Routes written and uploaded to GitHub.

-**Week 4** D3 set up.

-**Week 5** img2txt_db created in PostgreSQL database which includes three tables username, list of condos and list of photos. Once created, 5,276 lists of condos were imported using pandas read csv, photo features generated from the model were also imported using pandas csv import function. Username are stored once the user registered to the platform.
<img src="https://github.com/TREXKS/Image-to-Text/blob/master/Process%20Book%20Images/condos%20table.png" title="Formatted Condo Data">
<img src="https://github.com/TREXKS/Image-to-Text/blob/master/Process%20Book%20Images/variables%20in%20phonos%20table.png" title="List of variables in the phonos table">

-**Week 6** Once the database and tables were created, the configuration was added to app.py to link the database & tables with front-end where the results of the search are displayed.

-**Week 7** Frontend, backend, and model all connected.  Flavor text changed, errors fixed with logins and image uploading.    Updated flavor text of landing page. Fixed a bug with accessing database from search page, allowing final project video to be completed.
<img src="https://github.com/TREXKS/Image-to-Text/blob/master/Process%20Book%20Images/Landing%20Page.png" title="Landing Page">
<img src="https://github.com/TREXKS/Image-to-Text/blob/master/Process%20Book%20Images/Fixed%20image%20loading.png" title="Search Function">


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
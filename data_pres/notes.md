# DS105M Presentation Notes

Please find accompanying notes for our presentation here.

## Introduction

This presentation will outline how we are managing our data, some early summary statistics of our data and finally and indication of the next steps of our project.

Some information on our presentation:

* Our presentation is coded in the R Markdown language (.Rmd). You can find the raw code in this repository under the `slides` folder. The file is called `rmdslides.Rmd`. When compiled in RStudio, the file converts the markdown language we have imputted into an HTML file (which you can find in the same folder). This is what you will see.

* The advantage of this approach is that it allows us to run code live in the markdown which updates each time it is compiled. Any of the summary statistics are code rather than text. This means that if one person makes a change to the data, the related slide does not have to be rewritten.

* If you want to run the presentation on your own machine consult the `README.md` file for the overall repository.

## Slide 1: Brief summary

Our project is aiming to visualise gender biases in Scottish Parliamentary debates. We know from other contexts that women generally tend to contribute less in professional and legislative settings because of gender discrimination in these environments. Our project aims to quantify and visualise this so as to inform people of the problem.

## Slide 2: Organisation

We thought carefully about how to organise our project. Our guiding principle is reproducibility. This is because we want to be fully transparent in our procedures and furthermore we want to make everything we do open-source so that others can improve it in the future.

We define reproducibility as any user on any machine being able to run our full project using only the materials contained in our GitHub repository. There should be no financial cost to them and they should be able to edit and create their own project without restriction.

Because of this, we needed to make sure that everything we do to the data is programmatically done. For example, we use the HTTPS protocol to download our data in code rather than asking each user to download a copy manually. Furthermore all of our data wrangling is done programmatically so that anyone can get the same results as us simply by running our code.  

This also has the advantage of others being able to view and check  our code so that if there are mistakes, they can be more easily flagged 

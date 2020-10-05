This is a read me file and been created as part of git session dated on 04-10-2020

git init	: is used to make local directory as a git folder

git clone 	<link> 	: helps in dumping all the development remote directory on your machine

git add 	: is used to add changed files to the git
				git add .	-> will add all modified files

				git add templates/filename1.html templates/css/filename2.css routes/filename3.py

git commit 	: leaves a message 

git pull 	: will fetches the latest updated code to your local repository

git push 	: will push your changes to the global repository

git status	: will bring you the recent changed/ modified files


#BRANCH:

				whatsapp live
				|		\	
				|+++++++++++BETA version
				|				|			
				|				|+++++++++UAT Testing
		hot fix	|								|
	+++++++++++	|								|++++++internal whatsapp tesing team
				|											|
				|											|+++++ development Master
				|											|			|
				|											|			|+++++++|
																				| feature branch
																						|
																						|++++++sundeep
																								|sundeep branch
																										|
																										|++local code    
																						|++++++swathi
																								|
																								|++local code    
																						|++++++kusumanjali
																								|					
																								|++local code


git branch 	<branchname> :	will create a new branch

git checkout <branchname>: will take you to the respective branch
	eg: git branch orderreport

	git checkout orderreport

	git checkout master


git pull origin <branchname>

git push origin <sundeep>

git log will give you the history of the previous actions

git config --global user.name = <yourname>
git config --global user.email = <email>
git config --global user.password = <password>

git stash	: will clear the recent added files to the git all changes will be reverted



#by developer
git init

git clone / initial pull

git fetch 
git pull

git push
git status

git add <filenames>

git stash

git checkout


#by superior
git merge
git log



add file extensions to .gitignore
.sql\
.log
.csv

git status




# bookbot
Welcome to bookbot! With this simple program you can get the contents of a book and generate a report to get its word, character, and letter counts. You can also see a breakdown of how many times each letter was used in the book. 

## Setuping your Dev Environment
The easiest way for you to run this project on MacOS or Windows is to use the Dev Environments feature of Docker Desktop. This allows you to get an instant Python enironment up and running instantly. To use it, you just need to have "Git", "VSCode", and "Docker Desktop" installed, and make sure you also install the "Dev Containers" plugin for VSCode. For more information on how this works, go to https://docs.docker.com/desktop/dev-environments/create-dev-env/. 

If you don't want to run it in a Docker container, you can always clone this repo to your machine and get Python up and running. The python version used for this project is version 3.11.2.

## Running the Program
Once you have your dev environment setup, its time to run the program. To get started, you must first have a book or other text file you would like to use. You can provide it your own or use the one this program was tested with by going to https://raw.githubusercontent.com/asweigart/codebreaker/master/frankenstein.txt.

Once you have added your chosen book to the project directory, all you need to do for the program to work is create an instance of a book class and specify the path of the book. Then you can either get the books contents or generate a report based on its content.


# Setup SonarQube to analyse a unity project

> On a MacOs computer I will install SonarQube inside docker then setup the scanner and launch an analysis on a projects
>
>

You need brew installed

> 2022/01/21 Added a script to always output the url at the end

### Install docker and the SonarQube image then run the container
```sh
brew install docker

docker pull sonarqube

docker run -d --name sonarqube -p 9000:9000 -p 9092:9092 sonarqube

```
sonarqube is the official image but you can install others

### Launch the admin site and create a project
The container takes a few seconds to launch the you can open the admin page
>  http://127.0.0.1:9000

The login and password will be admin but you will be asked to change it.

On the main page  
select create manually  
put a name (like UnityTest) ***I will use this name later***  
click Setup  
click locally
enter a text to generate a token ***note the name as you cannot use it later***  
Copy it for later use  
Click continue  
select .NET then .NET Framework  
***you can copy the 3 commands but we will use a variation of it***

### Install a good version of java
> Unless you work on java your default sdk is certainly old and will generate errors when closing the analysis.
>
>You can try without updating your java then come back if needed

 ```sh
 brew install java

 echo 'export PATH="/usr/local/opt/openjdk/bin:$PATH"' >> ~/.bash_profile
 source ~/.bash_profile #needed to reload the PATH

  ```

### Download the right scanner
use https://github.com/SonarSource/sonar-scanner-msbuild/releases/download/4.7.1.2311/sonar-scanner-msbuild-4.7.1.2311-net46.zip
>If you try using the latest version (in my case version 5)
>
>you will have error at the first command  : get_http() not found

Unzip the folder and store wherever you want.
inside a terminal go to the folder then do
 ```
cd sonar-scanner-4.1.0.1829/bin/
chmod +x *
 ```
You are ready to analyse your project

### Analyse you project
*Start the analysis*
```sh
cd path to your project #where your .sln file is stored
mono /<path to sonar scan>/SonarScanner.MSBuild.exe begin /k:"UnityTest" /d:sonar.host.url="http://127.0.0.1:9000"  /d:sonar.login="<your token>"
```
>UnityTest here is the name of the project we entered before.

*Build*
```sh
msbuild <yourprojectfilename>.sln /t:Rebuild
```

*End the analysis*
```sh
mono /<path to sonar scan>/SonarScanner.MSBuild.exe end  /d:sonar.login="<your token>"
```

> You can now return to your admin page and explore the result of the analysis  

### Références

```
Some references used
https://numeriquement.fr/tutoriels/tutoriel_sonarqube.php

https://medium.com/xrpractices/static-code-analysis-for-unity3d-part-1-a17e8e2a6c03

https://medium.com/w-logs/installing-java-11-on-macos-with-homebrew-7f73c1e9fadf

```

# Docker containers for forecasting
<li>Portable and deliverable Docker containers have been created</li>
<li>All the files related to model building are in notebooks folder   </li>
<li> run the project by typing     

      sudo docker-compose up -d      
<li> pump state is forecasted for the next 10 timestamps using the past 20 timestamps </li>

<li> The variables and function names in the code files provide relevant information  </li>

<li> While building the docker container image file, final weight file(.h5 file) is copied instead of building model at runtime </li>


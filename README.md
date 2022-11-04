# Dockerfiles for DNAsensor
To run docker-compose.yml file, run this cmd on cmd prompt-
  `docker compose build`
  
This cmd will create image files of z_put, z_get, z_pub, z_storage.

## z_put
This file is to put data on all running subscriber or queryable. You need to pass a key and a value as argument to put data on subscriber. Default key value is 'Genotyper/1/DNAsensor/1/health' and default value is 'dead'

## z_get
This file is to get data from running subscriber or queryable. You need to pass a selector as argument to get data from subscriber or queryable. Default selector value is 'Genotyper/1/DNAsensor/**'

## z_pub
This file is to put continuous data on running subscriber. You need to pass a key and a value as argument to put data on subscriber. Default key value is 'Genotyper/1/DNAsensor/1/status' and default value is '0%'.

## z_storage
This file is to store data of all running subscriber and queryable and declares the subscriber and queryable. You need to pass a key as argument to put data on subscriber. Default key value is 'Genotyper/1/DNAsensor/** '.


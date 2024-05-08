#### Setup supabase
The database provider we will use is Supabase and we need to install the [Supabase CLI](https://supabase.com/docs/guides/cli/getting-started?queryGroups=platform&platform=npx). For ease of use, we are using npm to install this cli tool. 

The following command will install the tool and start supabase.

NOTE: This assumes that docker is running on your machine

`$ npm i && cd supabase && npx supabase start`

You can visit the Supabase Studio once supabase is up at `http://localhost:54423/project/default/editor`

#### DB Seed
You should see seed data populated in the `organizations` and `users` tables from the Supabase Studio above.

In case you don't see the seed data, you can run the reset command below which will trigger the `supabase/seed.sql` script.

`$ npx supabase db reset`

#### Build FastAPI application

Build the container using the following command

`$ docker-compose build --no-cache`

#### Run FastAPI application

Bring up the container using this

`$ docker-compose up --build`


#### Dashboard simulation - creating announcements
We will use [Postman](https://www.postman.com/downloads/) or similar [tool](https://insomnia.rest/download) to create `announcements`.

The following curl can be use to create an announcement in the database. You can update the `publish_at` field to specify the time you want the
announcement to go out.

```
curl --location 'http://localhost:8002/announcement' \
--header 'Content-Type: application/json' \
--data '{
    "body": "Our end of year party is on Saturday evening!",
    "organization_id": "11116e73-1c03-5de6-9130-5f9925ae8ab4",
    "publish_at": "2024-05-08T09:30:00Z"
}'
```

The seed data has the following organizations with the corresponding UUID to use in the curl above
- Jem: 11116e73-1c03-5de6-9130-5f9925ae8ab4
- Root: 1087ebe8-1ef8-5d97-8873-735b4949004d

Project: Queuing System in JS
Author: Samuel Atiemo

Project Tasks:

0. Install a redis instance
mandatory

1. Node Redis Client
mandatory
Install node_redis using npm

Using Babel and ES6, write a script named 0-redis_client.js. It should connect to the Redis server running on your machine:

2. Node Redis client and basic operations
mandatory
In a file 1-redis_op.js, copy the code you previously wrote (0-redis_client.js).

3. Node Redis client and async operations
mandatory
In a file 2-redis_op_async.js, let’s copy the code from the previous exercise (1-redis_op.js)

Using promisify, modify the function displaySchoolValue to use ES6 async / await

4. Node Redis client and advanced operations
mandatory
In a file named 4-redis_advanced_op.js, let’s use the client to store a hash value

5. Node Redis client publisher and subscriber
mandatory
In a file named 5-subscriber.js, create a redis client:

6. Create the Job creator
mandatory
In a file named 6-job_creator.js:

7. Create the Job processor
mandatory
In a file named 6-job_processor.js:

8. Track progress and errors with Kue: Create the Job creator
mandatory
In a file named 7-job_creator.js:

Create an array jobs with the following data inside:

9. Track progress and errors with Kue: Create the Job processor
mandatory
In a file named 7-job_processor.js:

Create an array that will contain the blacklisted phone numbers. Add in it 4153518780 and 4153518781 - these 2 numbers will be blacklisted by our jobs processor.

10. Writing the job creation function
mandatory
In a file named 8-job.js, create a function named createPushNotificationsJobs:

It takes into argument jobs (array of objects), and queue (Kue queue)

11. Writing the test for job creation
mandatory
Now that you created a job creator, let’s add tests:

12. In stock?
mandatory
Data
Create an array listProducts containing the list of the following products:

13. Can I have a seat?
#advanced
Redis
Create a Redic client:

Create a function reserveSeat, that will take into argument number, and set the key available_seats with the number



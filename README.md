## Inspiration
Companies producing long written content like papers, e-books and blogs need to break down this content and make it quickly shareable on social media sites like Twitter or Facebook.

## What it does
"Succinct" produces a concise summary of text/website/file while preserving key information and overall meaning.
It is also flexible enough to provide support for text input, pdf, doc, and txt files.

Succinct can monetize analyses of its user data to track social media trends, which would provide valuable insights for financial investment businesses

## How we built it
Succinct is powered by a Back-End API that is open for queries and built with Flask and Hosted on Azure.
We build the server API using flask, to get a text summary we used the "Sumy" ​python module as a black box.
We also worked with sqlAlchemy to store users' previous queries.
For the front-end, we used react, material UI and typescript.

## Challenges we ran into
It was pretty hard to send/receive files for out server, but we figured it out. 
Now our app supports pdf, docs, and text files.

## Accomplishments that we're proud of
Creating the whole application in 2 days.
Learning new technologies in a record time.

## What we learned
Restful APIs, Flask application structure, React native

## What's next for Succinct
Implementing data analytics on user's queries to find trends.
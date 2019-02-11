# Django Graphql Movies
**GraphQL** is a query language and server runtime that 
allows us to retrieve and manipulate data.
We leverage GraphQL's strongly-typed system to define the data we want available to the API. We then create a schema 
for the API - the set of allowed queries to retrieve and alter data.

### Designing a Movie Schema

#### Creating Types
Types describe the kind of data that's available in the API.we can define our own custom types.

Consider the following types for actors and movies:
```.env
type Actor {  
  id: ID
  name: String
}

type Movie {  
  id: ID
  title: String
  actors: [Actor]
  year: Int
}
```
#### Creating Queries
A query specifies what data can be retrieved and what's required to get to it:
```.env
type Query {  
  actor(id: ID): Actor
  movie(id: ID): Movie
  actors: [Actor]
  movies: [Movie]
}
```
#### Creating Mutations
What operations can be done to change data on the server that explained by **Mutaions**

Mutations rely on two things: **Input** & **Payload**
```.env
input ActorInput {  
  id: ID
  name: String!
}

type ActorPayload {  
  ok: Boolean
  actor: Actor
}
```
**Mutation** type brings it all together:
```.env
type Mutation {  
  createActor(input: ActorInput) : ActorPayload
  createMovie(input: MovieInput) : MoviePayload
  updateActor(id: ID, input: ActorInput) : ActorPayload
  updateMovie(id: ID, input: MovieInput) : MoviePayload
}
```
#### Defining the Schema
Map the queries and mutations we've created to the **schema**:
```.env
schema {  
  query: Query
  mutation: Mutation
}
```

Update Ongoing


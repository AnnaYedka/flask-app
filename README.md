# db-coursework
# Anna Yedka, 153501
# Recipe manager

## Functional requirements
- role system(client, recipe author/creator)
- authentication/authorization
- admin:
  - give author permission
  - CRUD meal categories
  - CRUD diets
- creator:
  - CRUD recipes
  - CRUD ingredients
- user:
  - CRUD reviews
  - add ingredients to shopping list
  - add recipes to favourites
  - store a diet & filter recipes by diet


## Entities
1. `User`
  - id BIGSERIAL PRIMARY KEY NN
  - username VARCHAR(50) UQ NN
  - password VARCHAR(50) NN
  - FOREIGN KEY role_id REFERENCES role(id) NN

2. `Role`
  - id SERIAL PRIMARY KEY NN
  - name VARCHAR(50) UQ NN

3. `Client`
  - id BIGSERIAL PRIMARY KEY NN
  - FOREIGN KEY user_id REFERENCES User(id) NN
  - FOREIGN KEY diet_id REFERENCES diet(id) NULL

4. `Diet`
  - id SERIAL PRIMARY KEY NN
  - name VARCHAR(50) UQ NN

5. `Review`
  - id BIGSERIAL PRIMARY KEY NN
  - FOREIGN KEY client_id REFERENCES Client(id) 
  - FOREIGN KEY recipe_id REFERENCES Recipe(id) NN
  - rating SMALLINT NN
  - commnent VARCHAR(255)

6. `Recipe`
  - id BIGSERIAL PRIMARY KEY NN
  - FOREIGN KEY author_id REFERENCES User(id) NN
  - FOREIGN KEY category_id REFERENCES MealCategory(id)
  - time DECIMAL(2,2) NN
  - title VARCHAR(50) NN
  - description TEXT NN

7. `MealCategory`
  - id SERIAL PRIMARY KEY NN
  - name VARCHAR(50) UQ NN

8. `ShoppingItem`
  - id BIGSERIAL PRIMARY KEY NN
  - FOREIGN KEY client_id REFERENCES Client(id) NN
  - FOREIGN KEY ingredient_id REFERENCES Ingredient(id) NN
  - amount INTEGER NN


9. `Ingredient`
  - id BIGSERIAL PRIMARY KEY NN
  - product_name VARCHAR(50) UQ NN
  - is_allergen BOOL NN

10. `RecipeIngredient`
  - id BIGSERIAL PRIMARY KEY NN
  - FOREIGN KEY recipe_id REFERENCE Recipe(id) NN
  - FOREIGN KEY ingredient_id REFERENCES Ingredient(id) NN
  - amount INTEGER NN

![db.pdf](https://github.com/AnnaYedka/db/files/12793723/db.pdf)

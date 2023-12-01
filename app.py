from lib.database_connection import DatabaseConnection
from lib.recipe_repository import RecipeRepository

connection = DatabaseConnection()
connection.connect()

connection.seed("seeds/recipes.sql")

recipe_repo = RecipeRepository(connection)
recipe = recipe_repo.find(3)

print(recipe)
